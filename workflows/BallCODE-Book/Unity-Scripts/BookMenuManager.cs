using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

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
    public Text book1Title;
    public Text book1Description;
    public Text book2Title;
    public Text book2Description;
    public Text book3Title;
    public Text book3Description;
    
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
        
        // Load the level using GameModeManager
        if (GameModeManager.Instance != null)
        {
            GameModeManager.Instance.LoadGameModeFromLevel(levelId);
        }
        else
        {
            Debug.LogError("[BookMenuManager] GameModeManager.Instance is null!");
        }
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
        if (LevelDataManager.Instance == null)
        {
            Debug.LogWarning("[BookMenuManager] LevelDataManager not found, using default book info");
            SetDefaultBookInfo();
            return;
        }
        
        // Get level data for each book
        LevelData book1 = LevelDataManager.Instance.GetLevel(BOOK1_LEVEL_ID);
        LevelData book2 = LevelDataManager.Instance.GetLevel(BOOK2_LEVEL_ID);
        LevelData book3 = LevelDataManager.Instance.GetLevel(BOOK3_LEVEL_ID);
        
        // Update Book 1 info
        if (book1Title != null && book1 != null)
        {
            book1Title.text = book1.levelName;
        }
        if (book1Description != null && book1 != null)
        {
            book1Description.text = book1.description;
        }
        
        // Update Book 2 info
        if (book2Title != null && book2 != null)
        {
            book2Title.text = book2.levelName;
        }
        if (book2Description != null && book2 != null)
        {
            book2Description.text = book2.description;
        }
        
        // Update Book 3 info
        if (book3Title != null && book3 != null)
        {
            book3Title.text = book3.levelName;
        }
        if (book3Description != null && book3 != null)
        {
            book3Description.text = book3.description;
        }
    }
    
    /// <summary>
    /// Set default book info if level data not available
    /// </summary>
    void SetDefaultBookInfo()
    {
        if (book1Title != null)
        {
            book1Title.text = "Book 1: Foundation Block";
        }
        if (book1Description != null)
        {
            book1Description.text = "Learn sequences with Block 1 (Pound Dribble)";
        }
        
        if (book2Title != null)
        {
            book2Title.text = "Book 2: Decision Crossover";
        }
        if (book2Description != null)
        {
            book2Description.text = "Learn conditionals with Block 2 (Crossover)";
        }
        
        if (book3Title != null)
        {
            book3Title.text = "Book 3: Pattern Loop";
        }
        if (book3Description != null)
        {
            book3Description.text = "Learn loops with pattern recognition";
        }
    }
}

