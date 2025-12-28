# 🔐 SSH Password Troubleshooting

**Problem:** SSH password authentication failing  
**Solutions:** Multiple options to fix

---

## 🎯 COMMON ISSUES

### Issue 1: Password Authentication Disabled

**The Pi might only accept SSH keys, not passwords.**

**Check if password auth is enabled:**
```bash
# Try to see what auth methods are allowed
ssh -v pi@192.168.1.226 2>&1 | grep -i "auth"
```

**If you see "publickey" only, password auth is disabled.**

---

## ✅ SOLUTION 1: Set Up SSH Keys (Recommended)

**This is the most secure and convenient method.**

### Step 1: Generate SSH Key (if you don't have one)

```bash
# Check if you already have an SSH key
ls -la ~/.ssh/id_rsa.pub

# If not, generate one
ssh-keygen -t rsa -b 4096
# Press Enter for all prompts (or set a passphrase if you want)
```

### Step 2: Copy Key to Raspberry Pi

**Option A: Using ssh-copy-id (easiest)**
```bash
ssh-copy-id pi@192.168.1.226
# Enter password one last time - after this, you won't need it!
```

**Option B: Manual copy**
```bash
# Copy your public key
cat ~/.ssh/id_rsa.pub

# SSH into Pi (you'll need password this one time)
ssh pi@192.168.1.226

# On the Pi, run:
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
# Paste your public key, save (Ctrl+X, Y, Enter)
chmod 600 ~/.ssh/authorized_keys
exit
```

### Step 3: Test

```bash
# Should work without password now!
ssh pi@192.168.1.226
```

---

## ✅ SOLUTION 2: Enable Password Authentication on Pi

**If you need password auth, enable it on the Pi.**

**SSH into Pi (if you can via another method), then:**

```bash
# Edit SSH config
sudo nano /etc/ssh/sshd_config

# Find and change:
# PasswordAuthentication no
# To:
PasswordAuthentication yes

# Save and restart SSH
sudo systemctl restart ssh
```

**Or if you have physical access to Pi:**
- Connect keyboard/monitor
- Enable password auth
- Or set up SSH keys from the Pi itself

---

## ✅ SOLUTION 3: Use Different User/Password

**Maybe the username or password is different?**

**Try:**
```bash
# Different common usernames
ssh raspberry@192.168.1.226
ssh admin@192.168.1.226
ssh user@192.168.1.226

# Or check if you need to specify password differently
ssh -o PreferredAuthentications=password pi@192.168.1.226
```

---

## ✅ SOLUTION 4: Manual Steps (If SSH Works Interactively)

**If you can SSH manually but not in script:**

### Step 1: SSH Manually

```bash
ssh pi@192.168.1.226
# Enter password when prompted
```

### Step 2: Once on Pi, Create .env File

```bash
# Create .env file
cat > ~/.n8n/.env << 'EOF'
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF

# Verify it was created
cat ~/.n8n/.env

# Restart n8n
sudo systemctl restart n8n

# Exit
exit
```

---

## ✅ SOLUTION 5: Use SSH with Password in Script

**If password auth works but you need to automate it:**

**Install sshpass (if available):**
```bash
# On Mac
brew install hudochenkov/sshpass/sshpass

# Then use:
sshpass -p 'your_password' ssh pi@192.168.1.226 "command"
```

**Or use expect script:**
```bash
#!/usr/bin/expect
spawn ssh pi@192.168.1.226
expect "password:"
send "your_password\r"
interact
```

---

## 🔍 DEBUGGING: Check What's Wrong

### Test 1: Can You Ping the Pi?

```bash
ping -c 3 192.168.1.226
```

### Test 2: Is SSH Port Open?

```bash
nc -zv 192.168.1.226 22
```

### Test 3: Verbose SSH (See What's Happening)

```bash
ssh -v pi@192.168.1.226
```

**Look for:**
- `Authentications that can continue: publickey,password` - Password should work
- `Authentications that can continue: publickey` - Password auth disabled

---

## 💡 QUICK FIX: Try Interactive SSH First

**Before automating, make sure you can SSH manually:**

```bash
# Try this first
ssh pi@192.168.1.226

# If this works, then the password is correct
# The issue might be with how the script is passing it
```

---

## 🎯 RECOMMENDED APPROACH

**Best solution: Set up SSH keys**

1. **Generate key** (if needed): `ssh-keygen`
2. **Copy to Pi**: `ssh-copy-id pi@192.168.1.226`
3. **Enter password one last time**
4. **After that, no password needed!**

**Then you can run:**
```bash
ssh pi@192.168.1.226 "cat > ~/.n8n/.env << 'EOF'
UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF
sudo systemctl restart n8n"
```

---

**Status:** SSH authentication issue  
**Action:** Set up SSH keys (easiest) or enable password auth on Pi  
**Time:** 5 minutes



