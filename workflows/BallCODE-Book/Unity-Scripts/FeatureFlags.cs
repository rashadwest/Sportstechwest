using UnityEngine;

/// <summary>
/// Feature Flag System for Reversible MVP Push
/// Allows instant enable/disable of features without code changes
/// </summary>
public static class FeatureFlags
{
    // Feature flag keys
    private const string BOOK1_MVP_KEY = "FeatureFlag_Book1MVP";
    private const int DISABLED = 0;
    private const int ENABLED = 1;
    
    /// <summary>
    /// Book 1 MVP Feature Flag
    /// Controls whether Book 1 exercise is available
    /// Can be disabled instantly via PlayerPrefs without code change
    /// </summary>
    public static bool Book1MVPEnabled
    {
        get
        {
            // Default: ENABLED (1) for MVP push
            // Can be disabled by setting PlayerPrefs to 0
            int flagValue = PlayerPrefs.GetInt(BOOK1_MVP_KEY, ENABLED);
            return flagValue == ENABLED;
        }
        set
        {
            // Set feature flag value
            PlayerPrefs.SetInt(BOOK1_MVP_KEY, value ? ENABLED : DISABLED);
            PlayerPrefs.Save();
            
            Debug.Log($"[FeatureFlags] Book1MVP set to: {(value ? "ENABLED" : "DISABLED")}");
        }
    }
    
    /// <summary>
    /// Disable Book 1 MVP instantly (for rollback)
    /// </summary>
    public static void DisableBook1MVP()
    {
        Book1MVPEnabled = false;
        Debug.LogWarning("[FeatureFlags] Book1MVP DISABLED - Feature rolled back");
    }
    
    /// <summary>
    /// Enable Book 1 MVP
    /// </summary>
    public static void EnableBook1MVP()
    {
        Book1MVPEnabled = true;
        Debug.Log("[FeatureFlags] Book1MVP ENABLED - Feature active");
    }
    
    /// <summary>
    /// Check if feature flag system is working
    /// </summary>
    public static bool IsFeatureFlagSystemWorking()
    {
        // Test: Save, read, verify
        bool originalValue = Book1MVPEnabled;
        
        // Toggle
        Book1MVPEnabled = !originalValue;
        bool toggledValue = Book1MVPEnabled;
        
        // Restore
        Book1MVPEnabled = originalValue;
        bool restoredValue = Book1MVPEnabled;
        
        bool working = (toggledValue == !originalValue) && (restoredValue == originalValue);
        
        if (!working)
        {
            Debug.LogError("[FeatureFlags] Feature flag system NOT working correctly!");
        }
        
        return working;
    }
    
    /// <summary>
    /// Get current status of all feature flags (for debugging)
    /// </summary>
    public static string GetFeatureFlagsStatus()
    {
        return $"Book1MVP: {(Book1MVPEnabled ? "ENABLED" : "DISABLED")}";
    }
}

