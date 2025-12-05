using UnityEngine;

/// <summary>
/// Handles return flow from Unity game to website after book exercise completion
/// Uses JavaScript communication for WebGL builds
/// </summary>
public class BookReturnHandler : MonoBehaviour
{
    public static BookReturnHandler Instance;
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    /// <summary>
    /// Called when book exercise is completed
    /// Communicates completion status to website via JavaScript
    /// </summary>
    public void OnExerciseComplete(int bookNumber, bool success, float score)
    {
        Debug.Log($"[BookReturnHandler] Exercise complete: Book {bookNumber}, Success: {success}, Score: {score}");
        
        #if UNITY_WEBGL && !UNITY_EDITOR
        // Send message to parent window (if in iframe) or current window
        SendExerciseCompleteToWebsite(bookNumber, success, score);
        
        // Also try URL redirect as fallback
        string returnUrl = PlayerPrefs.GetString("BookReturnUrl", $"/books/book{bookNumber}");
        string redirectUrl = $"{returnUrl}?exercise=complete&success={(success ? 1 : 0)}&score={score}";
        
        // Redirect after short delay to allow message to be sent
        StartCoroutine(DelayedRedirect(redirectUrl, 1.0f));
        #else
        // Editor/Standalone: Just log
        Debug.Log($"[BookReturnHandler] Would send completion: Book {bookNumber}, Success: {success}, Score: {score}");
        #endif
    }
    
    #if UNITY_WEBGL && !UNITY_EDITOR
    /// <summary>
    /// Send exercise completion message to website via JavaScript
    /// </summary>
    void SendExerciseCompleteToWebsite(int bookNumber, bool success, float score)
    {
        // Use Application.ExternalCall for WebGL
        try
        {
            // Try to call JavaScript function
            Application.ExternalCall("SendExerciseComplete", bookNumber, success ? 1 : 0, score);
            Debug.Log($"[BookReturnHandler] Sent completion message via ExternalCall");
        }
        catch (System.Exception e)
        {
            Debug.LogWarning($"[BookReturnHandler] ExternalCall failed: {e.Message}. Using postMessage fallback.");
            
            // Fallback: Use postMessage directly
            string message = $"{{\"type\":\"exerciseComplete\",\"book\":{bookNumber},\"success\":{(success ? "true" : "false")},\"score\":{score}}}";
            Application.ExternalEval($"if(window.parent && window.parent !== window) {{ window.parent.postMessage({message}, '*'); }}");
        }
    }
    
    /// <summary>
    /// Delayed redirect coroutine
    /// </summary>
    System.Collections.IEnumerator DelayedRedirect(string url, float delay)
    {
        yield return new WaitForSeconds(delay);
        
        // Only redirect if message communication might have failed
        // In practice, you might want to check if message was received
        Application.ExternalEval($"window.location.href = '{url}';");
    }
    #endif
}


