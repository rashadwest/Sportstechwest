using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;

/// <summary>
/// Main manager for Story Mode in BallCODE game
/// Handles page turning, audio narration, and transitions to game modes
/// </summary>
public class StoryModeManager : MonoBehaviour 
{
    [Header("Story Mode UI")]
    public GameObject storyModeCanvas;
    public GameObject pageTurnerContainer;
    public Image leftPageImage;
    public Image rightPageImage;
    public Text leftPageText;
    public Text rightPageText;
    public Button nextPageButton;
    public Button previousPageButton;
    public Button playExerciseButton;
    public Text pageIndicator;
    
    [Header("Audio")]
    public AudioSource narrationSource;
    public AudioClip[] episode1AudioClips;
    public AudioClip[] episode2AudioClips;
    public AudioClip[] episode3AudioClips;
    
    [Header("Story Data")]
    public StoryEpisode[] episodes;
    
    [Header("Game Mode Integration")]
    public GameModeManager gameModeManager;
    
    [Header("Metrics Collection")]
    public MetricsCollector metricsCollector;
    
    private int currentEpisode = 0;
    private int currentSpread = 0;
    private bool isPlayingAudio = false;
    private Coroutine pageTurnCoroutine;
    private Coroutine audioProgressCoroutine;
    private float pageViewStartTime;
    private float episodeStartTime;
    
    // Game mode mapping
    private Dictionary<int, string> episodeToGameMode = new Dictionary<int, string>
    {
        { 0, "Training" },      // Episode 1 → Training Mode
        { 1, "Prediction" },   // Episode 2 → Opponent Prediction
        { 2, "Math" }           // Episode 3 → Math Version
    };
    
    void Start() 
    {
        SetupUI();
        
        // Check if story mode was launched from URL parameter
        CheckURLParameters();
    }
    
    void CheckURLParameters()
    {
        #if UNITY_WEBGL && !UNITY_EDITOR
        string url = Application.absoluteURL;
        if (url.Contains("story"))
        {
            if (GetURLParameter("episode", out string episodeStr))
            {
                int episode = int.Parse(episodeStr) - 1; // Convert to 0-indexed
                EnterStoryMode(episode);
            }
        }
        #endif
    }
    
    bool GetURLParameter(string paramName, out string value)
    {
        value = "";
        #if UNITY_WEBGL && !UNITY_EDITOR
        string url = Application.absoluteURL;
        if (string.IsNullOrEmpty(url)) return false;
        
        int startIndex = url.IndexOf(paramName + "=");
        if (startIndex == -1) return false;
        
        startIndex += paramName.Length + 1;
        int endIndex = url.IndexOf("&", startIndex);
        if (endIndex == -1) endIndex = url.Length;
        
        value = url.Substring(startIndex, endIndex - startIndex);
        return true;
        #else
        return false;
        #endif
    }
    
    public void EnterStoryMode(int episodeIndex = 0) 
    {
        storyModeCanvas.SetActive(true);
        episodeStartTime = Time.time;
        LoadEpisode(episodeIndex);
        ShowSpread(0);
    }
    
    public void ExitStoryMode()
    {
        storyModeCanvas.SetActive(false);
        if (narrationSource.isPlaying)
        {
            narrationSource.Stop();
        }
    }
    
    void LoadEpisode(int episodeIndex) 
    {
        currentEpisode = episodeIndex;
        currentSpread = 0;
        
        if (episodeIndex < episodes.Length) 
        {
            StoryEpisode episode = episodes[episodeIndex];
            Debug.Log($"Loaded Episode {episodeIndex + 1}: {episode.title}");
        }
    }
    
    void ShowSpread(int spreadIndex) 
    {
        if (currentEpisode >= episodes.Length) return;
        
        StoryEpisode episode = episodes[currentEpisode];
        if (spreadIndex >= episode.spreads.Count) return;
        
        // Track time spent on previous page (if not first page)
        if (spreadIndex > 0 && metricsCollector != null)
        {
            float timeOnPage = Time.time - pageViewStartTime;
            metricsCollector.OnStoryPageView(currentEpisode, currentSpread, timeOnPage);
        }
        
        StorySpread spread = episode.spreads[spreadIndex];
        currentSpread = spreadIndex;
        pageViewStartTime = Time.time; // Start tracking time for this page
        
        // Update left page
        leftPageText.text = spread.leftPageText;
        if (spread.leftPageImage != null) 
        {
            leftPageImage.sprite = spread.leftPageImage;
            leftPageImage.gameObject.SetActive(true);
        }
        else
        {
            leftPageImage.gameObject.SetActive(false);
        }
        
        // Update right page
        if (spread.rightPageImage != null) 
        {
            rightPageImage.sprite = spread.rightPageImage;
            rightPageImage.gameObject.SetActive(true);
        }
        else
        {
            rightPageImage.gameObject.SetActive(false);
        }
        
        // Update navigation buttons
        previousPageButton.interactable = spreadIndex > 0;
        nextPageButton.interactable = spreadIndex < episode.spreads.Count - 1;
        
        // Show/hide play exercise button
        playExerciseButton.gameObject.SetActive(spread.hasExercise);
        
        // Load and play audio
        PlayNarration(currentEpisode, spreadIndex);
        
        // Update page indicator
        UpdatePageIndicator();
        
        // Track page view (for first page or when returning)
        if (metricsCollector != null && spreadIndex == 0)
        {
            metricsCollector.OnStoryPageView(currentEpisode, spreadIndex, 0f);
        }
    }
    
    public void NextPage() 
    {
        if (currentEpisode >= episodes.Length) return;
        
        StoryEpisode episode = episodes[currentEpisode];
        if (currentSpread < episode.spreads.Count - 1) 
        {
            StartPageTurnAnimation(() => {
                ShowSpread(currentSpread + 1);
            });
        }
        else 
        {
            // End of episode - offer to play exercise
            if (episode.hasFinalExercise)
            {
                TransitionToGame();
            }
        }
    }
    
    public void PreviousPage() 
    {
        if (currentSpread > 0) 
        {
            StartPageTurnAnimation(() => {
                ShowSpread(currentSpread - 1);
            });
        }
    }
    
    void StartPageTurnAnimation(System.Action onComplete) 
    {
        if (pageTurnCoroutine != null) 
        {
            StopCoroutine(pageTurnCoroutine);
        }
        pageTurnCoroutine = StartCoroutine(PageTurnAnimation(onComplete));
    }
    
    IEnumerator PageTurnAnimation(System.Action onComplete) 
    {
        // Pause audio during page turn
        bool wasPlaying = narrationSource.isPlaying;
        if (wasPlaying)
        {
            narrationSource.Pause();
        }
        
        // 3D page turn effect (simplified - you can enhance with actual 3D page models)
        float duration = 0.6f;
        float elapsed = 0f;
        
        // Simple fade effect
        CanvasGroup canvasGroup = pageTurnerContainer.GetComponent<CanvasGroup>();
        if (canvasGroup == null)
        {
            canvasGroup = pageTurnerContainer.AddComponent<CanvasGroup>();
        }
        
        while (elapsed < duration) 
        {
            elapsed += Time.deltaTime;
            float progress = elapsed / duration;
            
            // Fade out
            if (progress < 0.5f)
            {
                canvasGroup.alpha = 1f - (progress * 2f);
            }
            // Fade in
            else
            {
                canvasGroup.alpha = (progress - 0.5f) * 2f;
            }
            
            yield return null;
        }
        
        canvasGroup.alpha = 1f;
        onComplete?.Invoke();
        
        // Resume audio if it was playing
        if (wasPlaying)
        {
            narrationSource.UnPause();
        }
        
        pageTurnCoroutine = null;
    }
    
    void PlayNarration(int episode, int spread) 
    {
        if (narrationSource == null) return;
        
        narrationSource.Stop();
        
        AudioClip clip = GetNarrationClip(episode, spread);
        if (clip != null) 
        {
            narrationSource.clip = clip;
            narrationSource.Play();
            isPlayingAudio = true;
            StartCoroutine(UpdateAudioProgress());
        }
    }
    
    AudioClip GetNarrationClip(int episode, int spread) 
    {
        AudioClip[] clips = episode switch 
        {
            0 => episode1AudioClips,
            1 => episode2AudioClips,
            2 => episode3AudioClips,
            _ => null
        };
        
        if (clips != null && spread < clips.Length) 
        {
            return clips[spread];
        }
        return null;
    }
    
    IEnumerator UpdateAudioProgress() 
    {
        while (narrationSource.isPlaying) 
        {
            yield return null;
        }
        isPlayingAudio = false;
    }
    
    public void ToggleAudio() 
    {
        if (isPlayingAudio) 
        {
            narrationSource.Pause();
            isPlayingAudio = false;
        }
        else 
        {
            narrationSource.UnPause();
            isPlayingAudio = true;
        }
    }
    
    public void PlayExercise() 
    {
        // Track play exercise click
        if (metricsCollector != null)
        {
            metricsCollector.OnPlayExerciseClick(currentEpisode, currentSpread);
        }
        TransitionToGame();
    }
    
    void TransitionToGame() 
    {
        // Hide story mode UI
        storyModeCanvas.SetActive(false);
        
        // Get the exercise for current episode
        StoryEpisode episode = episodes[currentEpisode];
        
        // Get corresponding game mode
        string gameMode = episodeToGameMode.ContainsKey(currentEpisode) 
            ? episodeToGameMode[currentEpisode] 
            : "Training";
        
        // Load the corresponding game exercise
        if (gameModeManager != null)
        {
            gameModeManager.LoadGameMode(
                gameMode,
                currentEpisode + 1, // Episode number (1-indexed)
                episode.codingConcept,
                episode.monsterName
            );
        }
        else
        {
            Debug.LogError("GameModeManager not assigned!");
        }
    }
    
    public void OnExerciseComplete(bool success, float score)
    {
        // Track return to story from game
        if (metricsCollector != null)
        {
            metricsCollector.OnReturnToStory(currentEpisode, success, score);
        }
        
        // Called when player completes exercise and returns to story
        if (success)
        {
            // Unlock next spread or episode
            StoryEpisode episode = episodes[currentEpisode];
            if (currentSpread < episode.spreads.Count - 1)
            {
                // Move to next spread
                ShowSpread(currentSpread + 1);
            }
            else
            {
                // Episode complete - unlock next episode
                if (currentEpisode < episodes.Length - 1)
                {
                    // Track episode completion
                    if (metricsCollector != null)
                    {
                        float totalTime = Time.time - episodeStartTime;
                        metricsCollector.OnEpisodeComplete(currentEpisode, totalTime, episode.spreads.Count);
                    }
                    // Show completion screen
                    ShowEpisodeComplete();
                }
            }
        }
        
        // Show story mode again
        storyModeCanvas.SetActive(true);
    }
    
    void ShowEpisodeComplete()
    {
        // Show completion UI
        // You can create a completion panel here
        Debug.Log($"Episode {currentEpisode + 1} complete!");
    }
    
    void UpdatePageIndicator() 
    {
        if (currentEpisode < episodes.Length) 
        {
            StoryEpisode episode = episodes[currentEpisode];
            pageIndicator.text = $"Page {currentSpread + 1} of {episode.spreads.Count}";
        }
    }
    
    void SetupUI() 
    {
        nextPageButton.onClick.AddListener(NextPage);
        previousPageButton.onClick.AddListener(PreviousPage);
        playExerciseButton.onClick.AddListener(PlayExercise);
    }
}


