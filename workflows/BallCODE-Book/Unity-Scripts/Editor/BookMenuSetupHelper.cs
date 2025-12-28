#if UNITY_EDITOR
using UnityEngine;
using UnityEditor;
using UnityEngine.UI;
using TMPro;

/// <summary>
/// Editor helper to automatically set up Book menu UI
/// Right-click in Hierarchy → UI → Book Menu Setup
/// </summary>
public class BookMenuSetupHelper : EditorWindow
{
    [MenuItem("GameObject/UI/Book Menu Setup", false, 10)]
    static void CreateBookMenu()
    {
        // Get or create Canvas
        Canvas canvas = FindObjectOfType<Canvas>();
        if (canvas == null)
        {
            GameObject canvasObj = new GameObject("Canvas");
            canvas = canvasObj.AddComponent<Canvas>();
            canvas.renderMode = RenderMode.ScreenSpaceOverlay;
            canvasObj.AddComponent<CanvasScaler>();
            canvasObj.AddComponent<GraphicRaycaster>();
        }
        
        // Create Book Menu Panel
        GameObject bookMenuPanel = new GameObject("BookMenuPanel");
        bookMenuPanel.transform.SetParent(canvas.transform, false);
        
        RectTransform panelRect = bookMenuPanel.AddComponent<RectTransform>();
        panelRect.anchorMin = Vector2.zero;
        panelRect.anchorMax = Vector2.one;
        panelRect.sizeDelta = Vector2.zero;
        panelRect.anchoredPosition = Vector2.zero;
        
        Image panelBg = bookMenuPanel.AddComponent<Image>();
        panelBg.color = new Color(0, 0, 0, 0.8f); // Semi-transparent black
        
        // Create Back Button
        GameObject backButtonObj = CreateButton("BackButton", bookMenuPanel.transform, new Vector2(-400, 300), new Vector2(120, 50));
        Button backButton = backButtonObj.GetComponent<Button>();
        TextMeshProUGUI backText = backButtonObj.GetComponentInChildren<TextMeshProUGUI>();
        if (backText != null) backText.text = "← Back";
        
        // Create Title
        GameObject titleObj = CreateText("Title", bookMenuPanel.transform, new Vector2(0, 300), new Vector2(400, 60));
        TextMeshProUGUI titleText = titleObj.GetComponent<TextMeshProUGUI>();
        titleText.text = "📚 BOOK LESSONS";
        titleText.fontSize = 36;
        titleText.alignment = TextAlignmentOptions.Center;
        titleText.fontStyle = FontStyles.Bold;
        
        // Create Book 1 Button
        GameObject book1Obj = CreateBookButton("Book1Button", bookMenuPanel.transform, new Vector2(-200, 50), "Book 1", "Foundation Block\nLearn sequences");
        Button book1Button = book1Obj.GetComponent<Button>();
        
        // Create Book 2 Button
        GameObject book2Obj = CreateBookButton("Book2Button", bookMenuPanel.transform, new Vector2(0, 50), "Book 2", "Decision Crossover\nLearn conditionals");
        Button book2Button = book2Obj.GetComponent<Button>();
        
        // Create Book 3 Button
        GameObject book3Obj = CreateBookButton("Book3Button", bookMenuPanel.transform, new Vector2(200, 50), "Book 3", "Pattern Loop\nLearn loops");
        Button book3Button = book3Obj.GetComponent<Button>();
        
        // Add BookMenuManager
        GameObject managerObj = new GameObject("BookMenuManager");
        managerObj.transform.SetParent(canvas.transform, false);
        BookMenuManager manager = managerObj.AddComponent<BookMenuManager>();
        
        // Assign references via reflection (since fields are private)
        SerializedObject so = new SerializedObject(manager);
        so.FindProperty("bookMenuPanel").objectReferenceValue = bookMenuPanel;
        so.FindProperty("backButton").objectReferenceValue = backButton;
        so.FindProperty("book1Button").objectReferenceValue = book1Button;
        so.FindProperty("book2Button").objectReferenceValue = book2Button;
        so.FindProperty("book3Button").objectReferenceValue = book3Button;
        so.ApplyModifiedProperties();
        
        // Hide panel initially
        bookMenuPanel.SetActive(false);
        
        Selection.activeGameObject = bookMenuPanel;
        EditorUtility.FocusProjectWindow();
        
        Debug.Log("[BookMenuSetupHelper] Book menu created! Don't forget to assign Main Menu Panel reference in BookMenuManager.");
    }
    
    static GameObject CreateButton(string name, Transform parent, Vector2 position, Vector2 size)
    {
        GameObject buttonObj = new GameObject(name);
        buttonObj.transform.SetParent(parent, false);
        
        RectTransform rect = buttonObj.AddComponent<RectTransform>();
        rect.anchoredPosition = position;
        rect.sizeDelta = size;
        
        Image bg = buttonObj.AddComponent<Image>();
        bg.color = new Color(1f, 0.42f, 0.21f); // Orange
        
        Button button = buttonObj.AddComponent<Button>();
        
        // Create text child
        GameObject textObj = new GameObject("Text");
        textObj.transform.SetParent(buttonObj.transform, false);
        
        RectTransform textRect = textObj.AddComponent<RectTransform>();
        textRect.anchorMin = Vector2.zero;
        textRect.anchorMax = Vector2.one;
        textRect.sizeDelta = Vector2.zero;
        textRect.anchoredPosition = Vector2.zero;
        
        TextMeshProUGUI text = textObj.AddComponent<TextMeshProUGUI>();
        text.text = name;
        text.fontSize = 18;
        text.alignment = TextAlignmentOptions.Center;
        text.color = Color.white;
        
        return buttonObj;
    }
    
    static GameObject CreateBookButton(string name, Transform parent, Vector2 position, string title, string description)
    {
        GameObject container = new GameObject(name);
        container.transform.SetParent(parent, false);
        
        RectTransform containerRect = container.AddComponent<RectTransform>();
        containerRect.anchoredPosition = position;
        containerRect.sizeDelta = new Vector2(180, 200);
        
        // Button background
        GameObject buttonObj = new GameObject("Button");
        buttonObj.transform.SetParent(container.transform, false);
        
        RectTransform buttonRect = buttonObj.AddComponent<RectTransform>();
        buttonRect.anchorMin = Vector2.zero;
        buttonRect.anchorMax = Vector2.one;
        buttonRect.sizeDelta = Vector2.zero;
        buttonRect.anchoredPosition = Vector2.zero;
        
        Image bg = buttonObj.AddComponent<Image>();
        bg.color = Color.white;
        
        Button button = buttonObj.AddComponent<Button>();
        
        // Title text
        GameObject titleObj = new GameObject("Title");
        titleObj.transform.SetParent(container.transform, false);
        
        RectTransform titleRect = titleObj.AddComponent<RectTransform>();
        titleRect.anchorMin = new Vector2(0, 0.5f);
        titleRect.anchorMax = new Vector2(1, 1);
        titleRect.sizeDelta = Vector2.zero;
        titleRect.anchoredPosition = Vector2.zero;
        
        TextMeshProUGUI titleText = titleObj.AddComponent<TextMeshProUGUI>();
        titleText.text = title;
        titleText.fontSize = 24;
        titleText.alignment = TextAlignmentOptions.Center;
        titleText.fontStyle = FontStyles.Bold;
        titleText.color = new Color(1f, 0.42f, 0.21f); // Orange
        
        // Description text
        GameObject descObj = new GameObject("Description");
        descObj.transform.SetParent(container.transform, false);
        
        RectTransform descRect = descObj.AddComponent<RectTransform>();
        descRect.anchorMin = new Vector2(0, 0);
        descRect.anchorMax = new Vector2(1, 0.5f);
        descRect.sizeDelta = Vector2.zero;
        descRect.anchoredPosition = Vector2.zero;
        
        TextMeshProUGUI descText = descObj.AddComponent<TextMeshProUGUI>();
        descText.text = description;
        descText.fontSize = 14;
        descText.alignment = TextAlignmentOptions.Center;
        descText.color = Color.black;
        
        return buttonObj;
    }
    
    static GameObject CreateText(string name, Transform parent, Vector2 position, Vector2 size)
    {
        GameObject textObj = new GameObject(name);
        textObj.transform.SetParent(parent, false);
        
        RectTransform rect = textObj.AddComponent<RectTransform>();
        rect.anchoredPosition = position;
        rect.sizeDelta = size;
        
        TextMeshProUGUI text = textObj.AddComponent<TextMeshProUGUI>();
        text.text = name;
        text.fontSize = 24;
        text.alignment = TextAlignmentOptions.Center;
        text.color = Color.white;
        
        return textObj;
    }
}
#endif


