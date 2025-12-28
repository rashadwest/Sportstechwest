#!/usr/bin/env python3
"""
Create Soccer Commands from Basketball - Number System Reuse
Maps basketball dribble system (1-7) to soccer skills (1-7)
"""

import json
from pathlib import Path

# Basketball to Soccer Skill Mapping (Same Numbers!)
SKILL_MAPPING = {
    1: {
        "basketball": "Pound Dribble",
        "soccer": "Basic Dribble",
        "description": "Forward movement with ball control",
        "movement": "forward",
        "clock": 0.5
    },
    2: {
        "basketball": "Crossover Dribble",
        "soccer": "Cut Dribble",
        "description": "Quick change of direction (left or right)",
        "movement": "left_right",
        "clock": 0.8
    },
    3: {
        "basketball": "In & Out Dribble",
        "soccer": "In & Out",
        "description": "Feint move - fake one direction, go the other",
        "movement": "multi_directional",
        "clock": 1.0
    },
    4: {
        "basketball": "Between the Legs Dribble",
        "soccer": "Step Over",
        "description": "Step over the ball to fake direction",
        "movement": "complex_directional",
        "clock": 1.2
    },
    5: {
        "basketball": "Behind the Back Dribble",
        "soccer": "Cruyff Turn",
        "description": "Turn with ball behind standing leg",
        "movement": "rapid_change",
        "clock": 1.5
    },
    6: {
        "basketball": "Half Spin Dribble",
        "soccer": "Half Turn",
        "description": "180-degree turn with the ball",
        "movement": "rotational_180",
        "clock": 1.6
    },
    7: {
        "basketball": "Spin Dribble",
        "soccer": "Full Turn",
        "description": "360-degree turn with the ball",
        "movement": "rotational_360",
        "clock": 1.8
    }
}

def generate_soccer_commands_cs():
    """Generate SoccerCommands.cs from basketball pattern"""
    
    template = """using UnityEngine;

/// <summary>
/// Soccer-specific commands - Uses same number system (1-7) as basketball
/// </summary>
public class SoccerCommands : ISportCommand
{
    private SoccerGameManager gameManager;
    
    public SoccerCommands(SoccerGameManager manager)
    {
        gameManager = manager;
    }
    
    /// <summary>
    /// Execute skill by number (1-7) - Same number system as basketball!
    /// </summary>
    public void ExecuteSkill(int skillNumber, float clock = 0.5f)
    {
        switch (skillNumber)
        {
{SKILL_CASES}
            default:
                Debug.LogWarning($"Unknown skill number: {skillNumber}");
                break;
        }
    }
    
    public void Execute(string action, params object[] args)
    {
        // Handle number-based skills
        if (action.StartsWith("skill_"))
        {
            int skillNum = int.Parse(action.Split('_')[1]);
            float clock = args.Length > 0 ? float.Parse(args[0].ToString()) : 0.5f;
            ExecuteSkill(skillNum, clock);
            return;
        }
        
        // Handle named actions
        switch (action.ToLower())
        {
{NAMED_ACTIONS}
            default:
                Debug.LogWarning($"Unknown soccer action: {action}");
                break;
        }
    }
    
{SKILL_IMPLEMENTATIONS}
    
    // General soccer commands
    private void ExecuteDribble(object[] args)
    {
        // Forward dribble
        if (gameManager != null && gameManager.player != null)
        {
            gameManager.player.Dribble(Vector3.forward);
        }
    }
    
    private void ExecutePass(object[] args)
    {
        // Pass to direction
        string direction = args[0].ToString();
        if (gameManager != null && gameManager.ball != null)
        {
            Vector3 dir = GetDirection(direction);
            gameManager.ball.Kick(dir, 10f);
        }
    }
    
    private void ExecuteShoot(object[] args)
    {
        // Shoot at goal
        if (gameManager != null && gameManager.ball != null)
        {
            Vector3 goalDirection = GetGoalDirection();
            gameManager.ball.Kick(goalDirection, 15f);
        }
    }
    
    private Vector3 GetDirection(string direction)
    {
        switch (direction.ToLower())
        {
            case "left": return Vector3.left;
            case "right": return Vector3.right;
            case "forward": return Vector3.forward;
            case "back": return Vector3.back;
            default: return Vector3.forward;
        }
    }
    
    private Vector3 GetGoalDirection()
    {
        // Calculate direction to goal
        return Vector3.forward; // TODO: Calculate actual goal direction
    }
}
"""
    
    # Generate skill cases
    skill_cases = []
    for num, skill in SKILL_MAPPING.items():
        method_name = f"ExecuteSkill{num}_{skill['soccer'].replace(' ', '')}"
        skill_cases.append(f"            case {num}: {method_name}(clock); break;")
    
    # Generate named actions
    named_actions = []
    for num, skill in SKILL_MAPPING.items():
        skill_lower = skill['soccer'].lower().replace(' ', '_')
        named_actions.append(f"            case \"{skill_lower}\":")
        named_actions.append(f"            case \"skill_{num}\":")
        method_name = f"ExecuteSkill{num}_{skill['soccer'].replace(' ', '')}"
        named_actions.append(f"                {method_name}(0.5f);")
        named_actions.append(f"                break;")
    
    # Generate skill implementations
    skill_implementations = []
    for num, skill in SKILL_MAPPING.items():
        method_name = f"ExecuteSkill{num}_{skill['soccer'].replace(' ', '')}"
        skill_implementations.append(f"""    /// <summary>
    /// Skill {num}: {skill['soccer']} - {skill['description']}
    /// Basketball equivalent: {skill['basketball']}
    /// </summary>
    private void {method_name}(float clock)
    {{
        Debug.Log($"[SoccerCommands] Executing Skill {num}: {skill['soccer']}, clock: {{clock}}");
        
        if (gameManager != null && gameManager.player != null)
        {{
            // TODO: Implement {skill['soccer']} movement
            // Movement type: {skill['movement']}
            // Clock: {{clock}}s
        }}
    }}
""")
    
    # Replace placeholders
    code = template.replace("{SKILL_CASES}", "\n".join(skill_cases))
    code = code.replace("{NAMED_ACTIONS}", "\n".join(named_actions))
    code = code.replace("{SKILL_IMPLEMENTATIONS}", "\n".join(skill_implementations))
    
    return code

def generate_soccer_level_data():
    """Generate soccer level data using number system"""
    
    levels = []
    
    # Book 1: Skill 1 (Basic Dribble)
    levels.append({
        "levelId": "soccer_book1_skill_1",
        "sport": "soccer",
        "levelName": "Basic Dribble",
        "bookNumber": 1,
        "gameMode": "blockcoding",
        "skills": [
            {
                "number": 1,
                "name": "Basic Dribble",
                "basketballEquivalent": "Pound Dribble",
                "clock": 0.5,
                "movement": "forward"
            }
        ],
        "successCriteria": {
            "requiredSkills": [1],
            "maxTime": 5.0
        }
    })
    
    # Book 2: Skills 1-2 (Basic + Cut)
    levels.append({
        "levelId": "soccer_book2_skills_1_2",
        "sport": "soccer",
        "levelName": "Basic Dribble + Cut",
        "bookNumber": 2,
        "gameMode": "blockcoding",
        "skills": [
            {
                "number": 1,
                "name": "Basic Dribble",
                "clock": 0.5
            },
            {
                "number": 2,
                "name": "Cut Dribble",
                "clock": 0.8
            }
        ],
        "successCriteria": {
            "requiredSkills": [1, 2],
            "sequence": [1, 2, 1],
            "maxTime": 8.0
        }
    })
    
    return levels

def main():
    """Main execution"""
    print("⚽ Creating Soccer Commands from Basketball Number System")
    print("=" * 60)
    print()
    
    # Generate C# code
    print("📝 Generating SoccerCommands.cs...")
    soccer_commands = generate_soccer_commands_cs()
    
    output_dir = Path(__file__).parent.parent / "Unity-Scripts" / "Soccer"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    commands_file = output_dir / "SoccerCommands.cs"
    commands_file.write_text(soccer_commands)
    print(f"✅ Created: {commands_file}")
    print()
    
    # Generate level data
    print("📝 Generating soccer level data...")
    levels = generate_soccer_level_data()
    
    levels_dir = Path(__file__).parent.parent / "Unity-Scripts" / "Levels" / "Soccer"
    levels_dir.mkdir(parents=True, exist_ok=True)
    
    for level in levels:
        level_file = levels_dir / f"{level['levelId']}.json"
        level_file.write_text(json.dumps(level, indent=2))
        print(f"✅ Created: {level_file}")
    print()
    
    # Generate mapping document
    print("📝 Generating skill mapping document...")
    mapping = {
        "basketball_to_soccer": SKILL_MAPPING,
        "note": "Same number system (1-7) - different skill names",
        "reusability": "~90% code reuse possible"
    }
    
    mapping_file = Path(__file__).parent.parent / "SOCCER-BASKETBALL-SKILL-MAPPING.json"
    mapping_file.write_text(json.dumps(mapping, indent=2))
    print(f"✅ Created: {mapping_file}")
    print()
    
    print("=" * 60)
    print("✅ Soccer commands created using basketball number system!")
    print()
    print("Key Benefits:")
    print("  ✅ Same number system (1-7)")
    print("  ✅ Same block coding structure")
    print("  ✅ ~90% code reuse")
    print("  ✅ Easy to implement")
    print()
    print("Next steps:")
    print("  1. Review SoccerCommands.cs")
    print("  2. Implement skill movements in Unity")
    print("  3. Test skill execution")
    print("  4. Create soccer levels")

if __name__ == "__main__":
    main()


