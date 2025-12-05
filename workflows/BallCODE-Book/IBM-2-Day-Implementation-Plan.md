# 2-Day Implementation Plan: Story in Game + Paywall

**Architecture:** Story in Unity game, exercise buttons on front page → paywall

---

## What Can Be Built in 2 Days ✅

### Day 1: Front Page + Paywall (4-5 hours)

**1. Front Page (2-3 hours)**
- Create homepage HTML
- Add "Story Mode" button (links to Unity)
- Add exercise buttons (Episode 1, 2, 3, etc.)
- Style and make responsive
- Add JavaScript for button clicks

**2. Paywall Page (2 hours)**
- Create paywall HTML page
- Display pricing options
- Add placeholder payment (for demo)
- Add redirect after "purchase"

**Result:** Functional front page + paywall for demo

---

### Day 2: Integration + Testing (2-3 hours)

**3. Story Mode Integration (1 hour)**
- Update StoryModeManager.cs to check purchase status
- Add paywall redirect if not purchased
- Test flow

**4. Testing & Polish (1-2 hours)**
- Test all flows
- Fix any issues
- Prepare for demo

**Result:** Complete integrated demo ready

---

## Quick Implementation Guide

### Step 1: Create Front Page (2-3 hours)

**File:** `ballcode.co/index.html` (or homepage)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BallCODE - Learn Coding Through Basketball</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        .hero {
            text-align: center;
            margin-bottom: 60px;
        }
        .hero h1 {
            font-size: 3em;
            color: #667eea;
            margin-bottom: 10px;
        }
        .button-group {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        .btn {
            padding: 20px 30px;
            font-size: 1.2em;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .btn-story {
            background: #667eea;
            color: white;
        }
        .btn-exercise {
            background: #764ba2;
            color: white;
        }
    </style>
</head>
<body>
    <div class="hero">
        <h1>BallCODE</h1>
        <p>Learn how robots think—through the game you love.</p>
    </div>
    
    <div class="button-group">
        <!-- Story Mode Button (FREE) -->
        <button class="btn btn-story" onclick="loadStoryMode(1)">
            📖 Read Episode 1 Story (FREE)
        </button>
        
        <!-- Exercise Buttons (Lead to Paywall) -->
        <button class="btn btn-exercise" onclick="showPaywall(1)">
            🎮 Episode 1 Exercise
        </button>
        <button class="btn btn-exercise" onclick="showPaywall(2)">
            🎮 Episode 2 Exercise
        </button>
        <button class="btn btn-exercise" onclick="showPaywall(3)">
            🎮 Episode 3 Exercise
        </button>
    </div>
    
    <script>
        function loadStoryMode(episode) {
            // Load Unity Story Mode
            window.location.href = `/story?episode=${episode}`;
        }
        
        function showPaywall(episode) {
            // Check if already purchased (for demo, always show paywall)
            // In production: check localStorage or server
            window.location.href = `/paywall?episode=${episode}`;
        }
    </script>
</body>
</html>
```

---

### Step 2: Create Paywall Page (2 hours)

**File:** `ballcode.co/paywall.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlock Episode - BallCODE</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background: #f5f5f5;
        }
        .paywall-container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .pricing-options {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .pricing-card {
            border: 2px solid #e0e0e0;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .pricing-card.selected {
            border-color: #667eea;
            background: #f0f4ff;
        }
        .price {
            font-size: 2em;
            color: #667eea;
            font-weight: bold;
            margin: 10px 0;
        }
        .btn-purchase {
            background: #667eea;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }
        .btn-purchase:hover {
            background: #764ba2;
        }
        .demo-note {
            background: #fff3cd;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #ffc107;
        }
    </style>
</head>
<body>
    <div class="paywall-container">
        <h1>Unlock Episode <span id="episode-number">1</span> Exercise</h1>
        <p>Purchase access to the interactive exercise for this episode.</p>
        
        <div class="demo-note">
            <strong>Demo Mode:</strong> This is a demonstration. In production, this would process real payments.
        </div>
        
        <div class="pricing-options">
            <div class="pricing-card" onclick="selectOption('single')">
                <h3>Single Episode</h3>
                <div class="price">$9.99</div>
                <p>Unlock Episode <span id="episode-single">1</span> exercise</p>
            </div>
            
            <div class="pricing-card" onclick="selectOption('full')">
                <h3>Full Series</h3>
                <div class="price">$79.99</div>
                <p>Unlock all 12 episodes</p>
            </div>
        </div>
        
        <button class="btn-purchase" onclick="processPurchase()">
            Purchase Now
        </button>
        
        <p style="text-align: center; margin-top: 20px;">
            <a href="/">← Back to Home</a>
        </p>
    </div>
    
    <script>
        // Get episode from URL
        const urlParams = new URLSearchParams(window.location.search);
        const episode = urlParams.get('episode') || '1';
        document.getElementById('episode-number').textContent = episode;
        document.getElementById('episode-single').textContent = episode;
        
        let selectedOption = 'single';
        
        function selectOption(option) {
            selectedOption = option;
            document.querySelectorAll('.pricing-card').forEach(card => {
                card.classList.remove('selected');
            });
            event.currentTarget.classList.add('selected');
        }
        
        function processPurchase() {
            // For demo: Just redirect to exercise
            // In production: Process payment via Stripe/PayPal
            
            // Save purchase status (for demo)
            localStorage.setItem(`episode${episode}Purchased`, 'true');
            
            // Redirect to exercise
            window.location.href = `/play?mode=mathlete&episode=${episode}&level=state-tracker`;
        }
    </script>
</body>
</html>
```

---

### Step 3: Update Story Mode (1 hour)

**File:** `Unity-Scripts/StoryModeManager.cs`

Add paywall check to existing `OnPlayExerciseClicked()` method:

```csharp
public void OnPlayExerciseClicked()
{
    // Check if episode is purchased
    if (IsEpisodePurchased(currentEpisode))
    {
        // Load exercise directly
        LoadExercise(currentEpisode);
    }
    else
    {
        // Redirect to paywall
        string paywallURL = $"ballcode.co/paywall?episode={currentEpisode + 1}&source=story";
        #if UNITY_WEBGL && !UNITY_EDITOR
        Application.ExternalEval($"window.location.href = '{paywallURL}'");
        #else
        Application.OpenURL(paywallURL);
        #endif
    }
}

bool IsEpisodePurchased(int episode)
{
    #if UNITY_WEBGL && !UNITY_EDITOR
    // Check browser localStorage
    string purchased = Application.ExternalEval($"localStorage.getItem('episode{episode + 1}Purchased')");
    return purchased == "true";
    #else
    // For editor testing
    return PlayerPrefs.GetInt($"Episode{episode + 1}Purchased", 0) == 1;
    #endif
}
```

---

## Testing Checklist

**Before Demo:**
- [ ] Front page loads correctly
- [ ] Story Mode button links to Unity
- [ ] Exercise buttons show paywall
- [ ] Paywall displays correctly
- [ ] "Purchase" redirects to exercise (for demo)
- [ ] Story Mode paywall check works
- [ ] All flows tested

---

## Demo Flow for IBM

### What to Show:

**1. Front Page (Live)**
- Show homepage
- Click "Story Mode" → Show Unity loads
- Click "Episode 1 Exercise" → Show paywall

**2. Story Mode (Unity)**
- Show story reading
- Click "Play Exercise" → Show paywall (if not purchased)

**3. Paywall (Demo)**
- Show pricing options
- Click "Purchase" → Show redirect to exercise
- Explain: "In production, this processes real payments"

**Key Message:**
"Story is free in the game. Exercises are monetized. Everything is integrated."

---

## Time Breakdown

**Day 1 (4-5 hours):**
- Front page: 2-3 hours
- Paywall page: 2 hours

**Day 2 (2-3 hours):**
- Story Mode integration: 1 hour
- Testing: 1-2 hours

**Total: 6-8 hours** - Very doable!

---

## What This Achieves

✅ **Integrated Platform**
- Story in game (not separate)
- Exercises gated behind paywall
- Professional appearance

✅ **Clear Monetization**
- Free story (engagement)
- Paid exercises (revenue)
- Freemium model

✅ **Ready for Demo**
- Functional front page
- Working paywall (demo mode)
- Story Mode integration

---

**Status:** ✅ **FEASIBLE** - Can build in 2 days for IBM demo

**Next Step:** Start with front page, then paywall, then integration.



