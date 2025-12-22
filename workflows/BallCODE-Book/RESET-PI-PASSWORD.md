# 🔐 Reset Raspberry Pi Password

**Problem:** Need to reset password on Raspberry Pi  
**Methods:** Multiple ways depending on access

---

## 🎯 METHOD 1: Physical Access (Easiest)

**If you have keyboard/monitor connected to Pi:**

### Step 1: Boot Pi and Login

1. Connect keyboard and monitor to Pi
2. Boot up the Pi
3. When login prompt appears, try to login
4. If you can't remember password, proceed to Step 2

### Step 2: Boot into Single User Mode

**For Raspberry Pi OS:**

1. **Reboot the Pi:**
   ```bash
   sudo reboot
   ```

2. **During boot, when you see the boot screen, press and hold:**
   - **Shift key** (for older Pi OS)
   - **Or press any key** during boot (for newer versions)

3. **Select "Advanced Options" → "Single User Mode"**

4. **This boots you into root shell (no password needed)**

### Step 3: Reset Password

**Once in single user mode:**

```bash
# Mount filesystem as read-write
mount -o remount,rw /

# Reset password for 'pi' user
passwd pi
# Enter new password twice

# Or reset password for any user
passwd username

# Reboot
reboot
```

---

## 🎯 METHOD 2: Edit SD Card Directly (If Pi Won't Boot)

**If you can't boot into single user mode:**

### Step 1: Remove SD Card

1. Power off Pi
2. Remove SD card
3. Insert into your Mac (using SD card reader)

### Step 2: Edit Password File on Mac

**On your Mac:**

```bash
# Mount the SD card (it will appear as a disk)
# Find the disk name
diskutil list

# Mount the root partition (usually /dev/diskXs2)
# Replace X with your disk number
sudo mkdir /Volumes/pi-root
sudo mount -t ext4 /dev/diskXs2 /Volumes/pi-root

# Edit the shadow file to remove password
sudo nano /Volumes/pi-root/etc/shadow

# Find the line for 'pi' user:
# pi:$6$...:...:...:...:...:...
# Change to (no password):
# pi::...:...:...:...:...:...
# (Remove everything between the two colons after 'pi:')

# Save (Ctrl+X, Y, Enter)

# Unmount
sudo umount /Volumes/pi-root
```

### Step 3: Boot Pi and Set New Password

1. **Insert SD card back into Pi**
2. **Boot Pi**
3. **Login as 'pi' (no password needed now)**
4. **Set new password:**
   ```bash
   passwd
   # Enter new password twice
   ```

---

## 🎯 METHOD 3: Use Raspberry Pi Imager (Fresh Start)

**If you want to start fresh:**

1. **Download Raspberry Pi Imager:**
   - https://www.raspberrypi.com/software/

2. **Flash new OS to SD card:**
   - Choose Raspberry Pi OS
   - Click gear icon (⚙️) for advanced options
   - **Set username:** `pi` (or your choice)
   - **Set password:** Your new password
   - **Enable SSH:** Yes
   - **Set hostname:** `raspberrypi` (or your choice)

3. **Write to SD card**

4. **Boot Pi with new image**

**This gives you a fresh install with known password!**

---

## 🎯 METHOD 4: If You Can SSH (But Forgot Password)

**If you can still SSH in (maybe with key), reset password:**

```bash
# SSH into Pi
ssh pi@192.168.1.226

# Change password
passwd
# Enter current password (if prompted)
# Enter new password twice
```

---

## 🎯 METHOD 5: Enable SSH and Set Password via SD Card

**If you have SD card access but can't boot:**

### Step 1: Mount SD Card on Mac

```bash
# Find SD card
diskutil list

# Mount boot partition (usually /dev/diskXs1)
# This is the FAT32 partition
# It should auto-mount, or:
sudo mkdir /Volumes/boot
sudo mount -t msdos /dev/diskXs1 /Volumes/boot
```

### Step 2: Enable SSH

```bash
# Create SSH file to enable SSH on boot
touch /Volumes/boot/ssh
```

### Step 3: Set Password via userconf

**For newer Raspberry Pi OS:**

```bash
# Create userconf file
echo 'pi:$6$...' > /Volumes/boot/userconf

# Generate password hash (on your Mac)
# Install mkpasswd if needed: brew install whois
echo 'your_new_password' | mkpasswd -m sha-512 -s

# Copy the hash and create userconf
echo 'pi:YOUR_HASH_HERE' > /Volumes/boot/userconf
```

**Or simpler - just enable SSH and reset password after boot:**

1. Create `/Volumes/boot/ssh` file (enables SSH)
2. Boot Pi
3. SSH in (might need to use default password or no password)
4. Change password: `passwd`

---

## ✅ RECOMMENDED: Easiest Method

**If you have physical access:**

1. **Boot Pi with keyboard/monitor**
2. **Boot into single user mode** (hold Shift during boot)
3. **Run:** `passwd pi`
4. **Set new password**
5. **Reboot**

**If you don't have physical access:**

1. **Use Raspberry Pi Imager** to flash fresh OS
2. **Set password during imaging** (gear icon → advanced options)
3. **Enable SSH** in advanced options
4. **Boot with known password**

---

## 🔒 AFTER RESETTING PASSWORD

**Once you have the new password:**

1. **Test SSH:**
   ```bash
   ssh pi@192.168.1.226
   # Enter new password
   ```

2. **Set up SSH keys (so you don't need password):**
   ```bash
   ssh-keygen
   ssh-copy-id pi@192.168.1.226
   # Enter password one last time
   ```

3. **Then set up .env file:**
   ```bash
   ssh pi@192.168.1.226 "cat > ~/.n8n/.env << 'EOF'
   UNITY_REPO_URL=https://github.com/rashadwest/BallCode.git
   UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
   WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   EOF
   sudo systemctl restart n8n"
   ```

---

## 🐛 TROUBLESHOOTING

### Can't Boot into Single User Mode?

- **Try:** Hold Shift key from power-on
- **Or:** Press any key during boot
- **Or:** Edit `/boot/cmdline.txt` on SD card, add `init=/bin/bash` at end

### SD Card Won't Mount on Mac?

- **Install ext4 support:**
  ```bash
  brew install --cask osxfuse
  brew install ext4fuse
  ```

- **Or use:** Disk Utility to mount

### Still Can't Reset?

- **Use Raspberry Pi Imager** - Fresh install is often easiest
- **Set password during imaging** - No guessing needed

---

**Status:** Need to reset Pi password  
**Recommended:** Physical access → Single user mode → `passwd pi`  
**Alternative:** Raspberry Pi Imager with password set during imaging


