#if UNITY_EDITOR
using UnityEngine;
using UnityEditor;
using UnityEngine.UI;

/// <summary>
/// Helper to add Book button to existing main menu
/// Select your main menu GameObject, then use this menu item
/// </summary>
public class BookButtonSetupHelper
{
    [MenuItem("GameObject/UI/Add Book Button to Selected Menu", true)]
    static bool ValidateAddBookButton()
    {
        return Selection.activeGameObject != null;
    }
    
    [MenuItem("GameObject/UI/Add Book Button to Selected Menu", false, 11)]
    static void AddBookButton()
    {
        GameObject selected = Selection.activeGameObject;
        
        if (selected == null)
        {
            EditorUtility.DisplayDialog("Error", "Please select a GameObject first (your main menu container)", "OK");
            return;
        }
        
        // Find existing game mode buttons to match style
        GameModeButton[] existingButtons = selected.GetComponentsInChildren<GameModeButton>();
        
        if (existingButtons.Length == 0)
        {
            EditorUtility.DisplayDialog("Error", "No GameModeButton components found. Make sure you selected the correct menu container.", "OK");
            return;
        }
        
        // Use first button as template
        GameModeButton template = existingButtons[0];
        GameObject templateObj = template.gameObject;
        
        // Create Book button by duplicating template
        GameObject bookButtonObj = Object.Instantiate(templateObj, templateObj.transform.parent);
        bookButtonObj.name = "BookButton";
        
        // Update GameModeButton component
        GameModeButton bookButton = bookButtonObj.GetComponent<GameModeButton>();
        if (bookButton != null)
        {
            // Set to Book mode using reflection
            SerializedObject so = new SerializedObject(bookButton);
            so.FindProperty("gameMode").enumValueIndex = 4; // Book is index 4
            so.ApplyModifiedProperties();
        }
        
        // Update button text
        TextMeshProUGUI text = bookButtonObj.GetComponentInChildren<TextMeshProUGUI>();
        if (text != null)
        {
            text.text = "Book";
        }
        else
        {
            Text textLegacy = bookButtonObj.GetComponentInChildren<Text>();
            if (textLegacy != null)
            {
                textLegacy.text = "Book";
            }
        }
        
        // Position next to other buttons (adjust as needed)
        RectTransform rect = bookButtonObj.GetComponent<RectTransform>();
        if (rect != null && existingButtons.Length > 0)
        {
            RectTransform lastButton = existingButtons[existingButtons.Length - 1].GetComponent<RectTransform>();
            if (lastButton != null)
            {
                rect.anchoredPosition = new Vector2(
                    lastButton.anchoredPosition.x + lastButton.sizeDelta.x + 20,
                    lastButton.anchoredPosition.y
                );
            }
        }
        
        Selection.activeGameObject = bookButtonObj;
        EditorUtility.FocusProjectWindow();
        
        Debug.Log("[BookButtonSetupHelper] Book button created! Make sure BookMenuManager is set up in your scene.");
    }
}
#endif


