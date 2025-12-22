using UnityEngine;
using UnityEditor;
using System.IO;

public class BuildScript
{
    public static void BuildWebGL()
    {
        // Get all scenes from Build Settings
        string[] scenes = EditorBuildSettings.scenes.Length > 0 
            ? System.Array.ConvertAll(EditorBuildSettings.scenes, scene => scene.path)
            : new string[] { "Assets/Scenes/Main Menu.unity" }; // Fallback scene
        
        string buildPath = Path.Combine(Application.dataPath, "../Builds/WebGL");
        Directory.CreateDirectory(buildPath);
        
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions
        {
            scenes = scenes,
            locationPathName = buildPath,
            target = BuildTarget.WebGL,
            options = BuildOptions.None
        };
        
        Debug.Log($"Building WebGL to: {buildPath}");
        Debug.Log($"Scenes to build: {string.Join(", ", scenes)}");
        
        var report = BuildPipeline.BuildPlayer(buildPlayerOptions);
        
        if (report.summary.result == UnityEditor.Build.Reporting.BuildResult.Succeeded)
        {
            Debug.Log($"✅ WebGL build succeeded! Output: {buildPath}");
        }
        else
        {
            Debug.LogError($"❌ WebGL build failed! Errors: {report.summary.totalErrors}");
            EditorApplication.Exit(1);
        }
    }
}
