using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using TMPro;

/// <summary>
/// Manages the Book menu UI - Shows Book 1, 2, 3 selection
/// Opens when user clicks "Book" button on main menu
/// </summary>
public class BookMenuManager : MonoBehaviour
{
    [Header("UI References")]
    public GameObject bookMenuPanel;              // Main panel for book selection
    public GameObject mainMenuPanel;              // Main menu panel (to hide when book menu is open)
    public Button backButton;                     // Button to return to main menu
    
    [Header("Book Buttons")]
    public Button book1Button;
    public Button book2Button;
    public Button book3Button;
    
    [Header("Book Info")]
    public Component book1Title;  // Can be Text or TextMeshProUGUI
    public Component book1Description;  // Can be Text or TextMeshProUGUI
    public Component book2Title;  // Can be Text or TextMeshProUGUI
    public Component book2Description;  // Can be Text or TextMeshProUGUI
    public Component book3Title;  // Can be Text or TextMeshProUGUI
    public Component book3Description;  // Can be Text or TextMeshProUGUI
    
    // Book level IDs (matching JSON filenames)
    private const string BOOK1_LEVEL_ID = "book1_foundation_block";
    private const string BOOK2_LEVEL_ID = "book2_decision_crossover";
    private const string BOOK3_LEVEL_ID = "book3_pattern_loop";
    
    void Start()
    {
        // Auto-find UI elements if not assigned
        AutoFindUIElements();
        
        // Hide book menu initially
        if (bookMenuPanel != null)
        {
            bookMenuPanel.SetActive(false);
        }
        
        // Setup button listeners
        if (book1Button != null)
        {
            book1Button.onClick.AddListener(() => LoadBook(1));
        }
        
        if (book2Button != null)
        {
            book2Button.onClick.AddListener(() => LoadBook(2));
        }
        
        if (book3Button != null)
        {
            book3Button.onClick.AddListener(() => LoadBook(3));
        }
        
        if (backButton != null)
        {
            backButton.onClick.AddListener(CloseBookMenu);
        }
        
        // Set book info text
        UpdateBookInfo();
    }
    
    /// <summary>
    /// Auto-find UI elements if not assigned in Inspector
    /// </summary>
    void AutoFindUIElements()
    {
        // Find BookMenuPanel
        if (bookMenuPanel == null)
        {
            GameObject found = GameObject.Find("BookMenuPanel");
            if (found != null)
            {
                bookMenuPanel = found;
                Debug.Log("[BookMenuManager] Auto-found BookMenuPanel");
            }
        }
        
        // Find Main Menu Panel
        if (mainMenuPanel == null)
        {
            // Try common names
            string[] possibleNames = { "MainMenuPanel", "MainMenu", "MenuPanel", "MainMenuCanvas" };
            foreach (string name in possibleNames)
            {
                GameObject found = GameObject.Find(name);
                if (found != null)
                {
                    mainMenuPanel = found;
                    Debug.Log($"[BookMenuManager] Auto-found MainMenuPanel: {name}");
                    break;
                }
            }
        }
        
        // Find buttons
        if (backButton == null)
        {
            GameObject found = GameObject.Find("BackButton");
            if (found != null)
            {
                backButton = found.GetComponent<Button>();
                if (backButton != null)
                {
                    Debug.Log("[BookMenuManager] Auto-found BackButton");
                }
            }
        }
        
        if (book1Button == null)
        {
            GameObject found = GameObject.Find("Book1Button");
            if (found != null)
            {
                book1Button = found.GetComponent<Button>();
                if (book1Button != null)
                {
                    Debug.Log("[BookMenuManager] Auto-found Book1Button");
                }
            }
        }
        
        if (book2Button == null)
        {
            GameObject found = GameObject.Find("Book2Button");
            if (found != null)
            {
                book2Button = found.GetComponent<Button>();
                if (book2Button != null)
                {
                    Debug.Log("[BookMenuManager] Auto-found Book2Button");
                }
            }
        }
        
        if (book3Button == null)
        {
            GameObject found = GameObject.Find("Book3Button");
            if (found != null)
            {
                book3Button = found.GetComponent<Button>();
                if (book3Button != null)
                {
                    Debug.Log("[BookMenuManager] Auto-found Book3Button");
                }
            }
        }
        
        // Find text components
        if (book1Title == null)
        {
            Transform book1Transform = book1Button?.transform.parent;
            if (book1Transform != null)
            {
                Transform titleTransform = book1Transform.Find("Title");
                if (titleTransform != null)
                {
                    book1Title = titleTransform.GetComponent<Text>();
                    if (book1Title == null)
                    {
                        book1Title = titleTransform.GetComponent<TextMeshProUGUI>();
                    }
                }
            }
        }
        
        if (book2Title == null)
        {
            Transform book2Transform = book2Button?.transform.parent;
            if (book2Transform != null)
            {
                Transform titleTransform = book2Transform.Find("Title");
                if (titleTransform != null)
                {
                    book2Title = titleTransform.GetComponent<Text>();
                    if (book2Title == null)
                    {
                        book2Title = titleTransform.GetComponent<TextMeshProUGUI>();
                    }
                }
            }
        }
        
        if (book3Title == null)
        {
            Transform book3Transform = book3Button?.transform.parent;
            if (book3Transform != null)
            {
                Transform titleTransform = book3Transform.Find("Title");
                if (titleTransform != null)
                {
                    book3Title = titleTransform.GetComponent<Text>();
                    if (book3Title == null)
                    {
                        book3Title = titleTransform.GetComponent<TextMeshProUGUI>();
                    }
                }
            }
        }
    }
    
    /// <summary>
    /// Open the book menu (called from main menu Book button)
    /// </summary>
    public void OpenBookMenu()
    {
        if (bookMenuPanel != null)
        {
            bookMenuPanel.SetActive(true);
        }
        
        if (mainMenuPanel != null)
        {
            mainMenuPanel.SetActive(false);
        }
        
        Debug.Log("[BookMenuManager] Book menu opened");
    }
    
    /// <summary>
    /// Close the book menu and return to main menu
    /// </summary>
    public void CloseBookMenu()
    {
        if (bookMenuPanel != null)
        {
            bookMenuPanel.SetActive(false);
        }
        
        if (mainMenuPanel != null)
        {
            mainMenuPanel.SetActive(true);
        }
        
        Debug.Log("[BookMenuManager] Book menu closed");
    }
    
    /// <summary>
    /// Load a book level (1, 2, or 3)
    /// </summary>
    public void LoadBook(int bookNumber)
    {
        string levelId = GetBookLevelId(bookNumber);
        
        if (string.IsNullOrEmpty(levelId))
        {
            Debug.LogError($"[BookMenuManager] Invalid book number: {bookNumber}");
            return;
        }
        
        Debug.Log($"[BookMenuManager] Loading Book {bookNumber} - Level ID: {levelId}");
        
        // Load the level using GameModeManager (if available)
        // Note: GameModeManager may not exist in all projects
        var gmType = System.Type.GetType("GameModeManager");
        if (gmType != null)
        {
            var instanceProp = gmType.GetProperty("Instance");
            if (instanceProp != null)
            {
                var instance = instanceProp.GetValue(null);
                var method = gmType.GetMethod("LoadGameModeFromLevel");
                if (method != null && instance != null)
                {
                    method.Invoke(instance, new object[] { levelId });
                    return;
                }
            }
        }
        
        // Fallback: Use SceneManager to load level scene directly
        Debug.LogWarning($"[BookMenuManager] GameModeManager not found, loading level directly: {levelId}");
        // Alternative: Load scene by name or use URL parameters
    }
    
    /// <summary>
    /// Get level ID for a book number
    /// </summary>
    string GetBookLevelId(int bookNumber)
    {
        return bookNumber switch
        {
            1 => BOOK1_LEVEL_ID,
            2 => BOOK2_LEVEL_ID,
            3 => BOOK3_LEVEL_ID,
            _ => null
        };
    }
    
    /// <summary>
    /// Update book info text from level data
    /// </summary>
    void UpdateBookInfo()
    {
        // Check if LevelDataManager exists (may not be in all projects)
        var levelDataManagerType = System.Type.GetType("LevelDataManager");
        if (levelDataManagerType == null)
        {
            Debug.LogWarning("[BookMenuManager] LevelDataManager not found, using default book info");
            SetDefaultBookInfo();
            return;
        }
        
        // Try to get Instance via reflection
        var instanceProp = levelDataManagerType.GetProperty("Instance");
        if (instanceProp == null)
        {
            SetDefaultBookInfo();
            return;
        }
        
        var instance = instanceProp.GetValue(null);
        if (instance == null)
        {
            SetDefaultBookInfo();
            return;
        }
        
        // Try to get level data via reflection
        var getLevelMethod = levelDataManagerType.GetMethod("GetLevel");
        if (getLevelMethod == null)
        {
            SetDefaultBookInfo();
            return;
        }
        
        // Get level data for each book (using reflection to avoid compilation errors)
        var book1 = getLevelMethod.Invoke(instance, new object[] { BOOK1_LEVEL_ID });
        var book2 = getLevelMethod.Invoke(instance, new object[] { BOOK2_LEVEL_ID });
        var book3 = getLevelMethod.Invoke(instance, new object[] { BOOK3_LEVEL_ID });
        
        // Get LevelData type for property access
        var levelDataType = System.Type.GetType("LevelData");
        if (levelDataType == null)
        {
            SetDefaultBookInfo();
            return;
        }
        
        // Update Book 1 info (using reflection)
        if (book1 != null)
        {
            var levelNameProp = levelDataType.GetProperty("levelName");
            var descProp = levelDataType.GetProperty("description");
            if (levelNameProp != null)
            {
                var levelName = levelNameProp.GetValue(book1)?.ToString();
                SetTextOnComponent(book1Title, levelName);
            }
            if (descProp != null)
            {
                var description = descProp.GetValue(book1)?.ToString();
                SetTextOnComponent(book1Description, description);
            }
        }
        
        // Update Book 2 info (using reflection)
        if (book2 != null)
        {
            var levelNameProp = levelDataType.GetProperty("levelName");
            var descProp = levelDataType.GetProperty("description");
            if (levelNameProp != null)
            {
                var levelName = levelNameProp.GetValue(book2)?.ToString();
                SetTextOnComponent(book2Title, levelName);
            }
            if (descProp != null)
            {
                var description = descProp.GetValue(book2)?.ToString();
                SetTextOnComponent(book2Description, description);
            }
        }
        
        // Update Book 3 info (using reflection)
        if (book3 != null)
        {
            var levelNameProp = levelDataType.GetProperty("levelName");
            var descProp = levelDataType.GetProperty("description");
            if (levelNameProp != null)
            {
                var levelName = levelNameProp.GetValue(book3)?.ToString();
                SetTextOnComponent(book3Title, levelName);
            }
            if (descProp != null)
            {
                var description = descProp.GetValue(book3)?.ToString();
                SetTextOnComponent(book3Description, description);
            }
        }
    }
    
    /// <summary>
    /// Helper method to set text on Component (Text or TextMeshProUGUI)
    /// </summary>
    void SetTextOnComponent(Component comp, string text)
    {
        if (comp == null || string.IsNullOrEmpty(text)) return;
        var textProp = comp.GetType().GetProperty("text");
        if (textProp != null)
            textProp.SetValue(comp, text);
    }
    
    /// <summary>
    /// Set default book info if level data not available
    /// </summary>
    void SetDefaultBookInfo()
    {
        SetTextOnComponent(book1Title, "Book 1: Foundation Block");
        SetTextOnComponent(book1Description, "Learn sequences with Block 1 (Pound Dribble)");
        SetTextOnComponent(book2Title, "Book 2: Decision Crossover");
        SetTextOnComponent(book2Description, "Learn conditionals with Block 2 (Crossover)");
        SetTextOnComponent(book3Title, "Book 3: Pattern Loop");
        SetTextOnComponent(book3Description, "Learn loops with pattern recognition");
    }
}

