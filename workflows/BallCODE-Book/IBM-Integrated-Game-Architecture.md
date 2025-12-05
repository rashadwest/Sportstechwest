# Integrated Game Architecture - Story in Game + Paywall

**Proposed Architecture:** Story deployed within Unity game, exercise buttons on front page leading to paywall

---

## Proposed Architecture

### User Flow

```
1. User visits ballcode.co (Front Page)
   ↓
2. Front Page shows:
   - Story Mode button (FREE - Episode 1)
   - Exercise buttons (Episode 1, Episode 2, etc.)
   ↓
3. User clicks "Episode 1 Exercise" button
   ↓
4. Paywall appears
   - "Unlock Episode 1 Exercise - $X.XX"
   - Payment processing
   ↓
5. After payment → Exercise unlocks
   ↓
6. User plays exercise in Mathlete Mode
   ↓
7. Return to Story Mode (if started from story)
```

---

## Architecture Components

### 1. Front Page (ballcode.co)

**Layout:**
```
┌─────────────────────────────────────┐
│         BALLCODE HOME PAGE          │
├─────────────────────────────────────┤
│                                     │
│  [Story Mode] (FREE - Episode 1)   │
│  └─ Read Episode 1 story            │
│                                     │
│  [Episode 1 Exercise] → Paywall    │
│  [Episode 2 Exercise] → Paywall    │
│  [Episode 3 Exercise] → Paywall    │
│  ...                                 │
│                                     │
│  [My Progress] (if logged in)      │
│  [Account]                          │
└─────────────────────────────────────┘
```

**Features:**
- Story Mode button (links to Unity Story Mode - FREE for Episode 1)
- Exercise buttons for each episode (lead to paywall)
- User account/login (optional for free story)
- Progress tracking (if logged in)

---

### 2. Story Mode (Inside Unity Game)

**Access:**
- Click "Story Mode" button on front page
- Loads Unity WebGL build with Story Mode
- URL: `ballcode.co/story?episode=1`

**Features:**
- Page-turner interface
- Audio narration
- Visual diagrams
- "Play Exercise" button appears at relevant points
- **Exercise button → Leads to paywall** (if not purchased)

**Story Mode Flow:**
```
Story Mode (Unity)
├── Read Episode 1 Story
├── Skill Pit-Stop
├── "Play Exercise" button appears
│   └─ Click → Check if purchased
│      ├─ If YES → Load Exercise
│      └─ If NO → Redirect to Paywall
└── Continue story after exercise
```

---

### 3. Paywall System

**Trigger Points:**
1. Click exercise button on front page
2. Click "Play Exercise" button in Story Mode (if not purchased)

**Paywall Features:**
- Episode-specific pricing
- Payment processing (Stripe, PayPal, etc.)
- Instant unlock after payment
- Save purchase status (browser/localStorage or account)

**Paywall Options:**
- Single episode purchase
- Full series bundle
- Subscription model
- Institutional licensing (separate flow)

---

### 4. Exercise Access (After Payment)

**Flow:**
```
Paywall → Payment → Unlock → Load Exercise
```

**Exercise Loading:**
- URL: `ballcode.co/play?mode=mathlete&episode=1&level=state-tracker`
- Pre-configured Mathlete Mode
- Episode-specific level
- No additional paywall (already purchased)

---

## Implementation Details

### Front Page Structure

**HTML/React/Next.js Page:**
```html
<div class="homepage">
  <h1>BallCODE</h1>
  
  <!-- Story Mode Button (FREE) -->
  <button onclick="loadStoryMode(1)">
    Read Episode 1 Story (FREE)
  </button>
  
  <!-- Exercise Buttons (Lead to Paywall) -->
  <div class="exercises">
    <button onclick="showPaywall(1)">
      Episode 1 Exercise
    </button>
    <button onclick="showPaywall(2)">
      Episode 2 Exercise
    </button>
    <button onclick="showPaywall(3)">
      Episode 3 Exercise
    </button>
    <!-- ... more episodes ... -->
  </div>
</div>
```

**JavaScript Functions:**
```javascript
function loadStoryMode(episode) {
  // Load Unity Story Mode
  window.location.href = `/story?episode=${episode}`;
}

function showPaywall(episode) {
  // Check if already purchased
  if (isPurchased(episode)) {
    loadExercise(episode);
  } else {
    // Show paywall modal
    showPaywallModal(episode);
  }
}

function loadExercise(episode) {
  // Load exercise after purchase
  window.location.href = `/play?mode=mathlete&episode=${episode}`;
}
```

---

### Story Mode Integration (Unity)

**StoryModeManager.cs Updates:**
```csharp
public class StoryModeManager : MonoBehaviour 
{
    [Header("Exercise Integration")]
    public Button playExerciseButton;
    public string paywallURL = "ballcode.co/paywall";
    
    void OnPlayExerciseClicked()
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
            Application.OpenURL($"{paywallURL}?episode={currentEpisode}&source=story");
        }
    }
    
    bool IsEpisodePurchased(int episode)
    {
        // Check localStorage or server
        // Return true if purchased
        return PlayerPrefs.GetInt($"Episode{episode}Purchased", 0) == 1;
    }
}
```

---

### Paywall Implementation

**Paywall Page (`ballcode.co/paywall`):**
```html
<div class="paywall">
  <h2>Unlock Episode {episode} Exercise</h2>
  
  <div class="pricing">
    <div class="option">
      <h3>Single Episode</h3>
      <p class="price">$9.99</p>
      <button onclick="purchaseEpisode({episode})">
        Purchase Episode {episode}
      </button>
    </div>
    
    <div class="option">
      <h3>Full Series (12 Episodes)</h3>
      <p class="price">$79.99</p>
      <button onclick="purchaseFullSeries()">
        Purchase Full Series
      </button>
    </div>
  </div>
  
  <div class="payment-form">
    <!-- Stripe/PayPal integration -->
  </div>
</div>
```

**Payment Processing:**
```javascript
async function purchaseEpisode(episode) {
  // Process payment via Stripe/PayPal
  const result = await processPayment(episode);
  
  if (result.success) {
    // Save purchase status
    savePurchaseStatus(episode);
    
    // Redirect to exercise
    window.location.href = `/play?mode=mathlete&episode=${episode}`;
  }
}
```

---

## Feasibility for 2 Days

### ✅ What CAN Be Done (2 Days)

**1. Front Page with Exercise Buttons (2-3 hours)**
- Create homepage with buttons
- Style and make responsive
- Add JavaScript for paywall triggers
- **Result:** Functional front page

**2. Paywall Page (2-3 hours)**
- Create paywall HTML page
- Add pricing display
- Integrate payment processing (Stripe/PayPal)
- **Result:** Functional paywall

**3. Story Mode in Unity (Already Exists)**
- StoryModeManager.cs already has structure
- Need to add paywall check
- **Result:** Story Mode with paywall integration

**Total Time:** 4-6 hours - **FEASIBLE**

---

### ❌ What CANNOT Be Done (2 Days)

**1. Full Payment Processing Integration**
- Stripe/PayPal setup (requires accounts, API keys)
- Payment webhook handling
- Purchase status database
- **Time:** 1-2 days (with payment provider setup)

**2. Exercise Development**
- Building Episode 1 exercise in Mathlete Mode
- Testing and debugging
- **Time:** 1-2 weeks

**3. Full User Account System**
- Registration/login
- Purchase history
- Progress tracking
- **Time:** 3-5 days

---

## Minimal Viable Implementation (2 Days)

### What to Build:

**1. Front Page (2 hours)**
- [ ] Create homepage HTML
- [ ] Add "Story Mode" button (links to Unity)
- [ ] Add exercise buttons (Episode 1, 2, 3, etc.)
- [ ] Style and make responsive
- [ ] Add JavaScript for button clicks

**2. Paywall Page (2 hours)**
- [ ] Create paywall HTML page
- [ ] Display pricing options
- [ ] Add "Coming Soon" or placeholder payment
- [ ] Add redirect after "purchase" (for demo)

**3. Story Mode Integration (1 hour)**
- [ ] Update StoryModeManager.cs to check purchase status
- [ ] Add paywall redirect if not purchased
- [ ] Test flow

**Total:** 5 hours - **FEASIBLE**

---

## Demo Strategy for IBM

### What to Show:

**1. Front Page (Live Demo)**
- Show homepage with buttons
- Click "Story Mode" → Show Unity Story Mode loads
- Click "Episode 1 Exercise" → Show paywall appears
- **Message:** "This is the integrated experience. Story is in the game, exercises are gated behind paywall."

**2. Story Mode (Unity Demo)**
- Show story reading experience
- Show "Play Exercise" button
- Click button → Show paywall (if not purchased)
- **Message:** "Story is integrated into the game. Exercises are monetized."

**3. Paywall (Demo)**
- Show pricing options
- Explain payment flow
- **Message:** "Monetization model: Free story, paid exercises."

---

## What to Say to IBM

**If Asked About Architecture:**

"We're building an integrated platform where:
- **Story Mode is free** - Students can read Episode 1 story in the Unity game
- **Exercises are monetized** - Exercise buttons on the front page lead to a paywall
- **Seamless experience** - Story and exercises are integrated, but exercises require purchase

This creates a freemium model where:
- Content (story) is accessible to build engagement
- Practice (exercises) is monetized for revenue
- Everything is integrated in one platform"

**Key Points:**
- ✅ Story in game (not separate website)
- ✅ Exercise buttons on front page
- ✅ Paywall for exercises
- ✅ Integrated experience

---

## Implementation Priority

### For IBM Demo (2 Days):

**Priority 1: Front Page (2 hours)**
- Homepage with buttons
- Story Mode button (links to Unity)
- Exercise buttons (lead to paywall)

**Priority 2: Paywall Page (2 hours)**
- Paywall HTML page
- Pricing display
- Placeholder payment (for demo)

**Priority 3: Story Mode Integration (1 hour)**
- Update Unity script
- Add paywall check
- Test flow

**Skip for Now:**
- Full payment processing (use placeholder)
- User accounts (optional for demo)
- Exercise development (explain vision)

---

## Architecture Benefits

### ✅ Advantages:

1. **Integrated Experience**
   - Everything in one platform
   - Seamless story → exercise flow
   - Professional appearance

2. **Clear Monetization**
   - Free story builds engagement
   - Paid exercises generate revenue
   - Freemium model

3. **Scalable**
   - Easy to add more episodes
   - Consistent user experience
   - Centralized payment

4. **Better for Partnerships**
   - Shows complete platform
   - Demonstrates business model
   - Professional integration

---

## Next Steps

### Immediate (2 Days):
1. Create front page with buttons
2. Create paywall page
3. Update Story Mode integration
4. Test flow

### After IBM (1-2 Weeks):
1. Integrate real payment processing
2. Build user account system
3. Develop Episode 1 exercise
4. Test full flow

---

**Status:** ✅ **FEASIBLE** - Can build front page + paywall in 2 days for demo

**Recommendation:** This architecture is better than separate website. Shows integrated platform and monetization model clearly.



