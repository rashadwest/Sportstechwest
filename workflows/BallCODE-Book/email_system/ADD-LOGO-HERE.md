# 📸 Add Your BallCODE Logo Here

## Quick Instructions

1. **Get your BallCODE logo file** (PNG or SVG)

2. **Save it here:**
   ```
   email_system/assets/images/ballcode-logo.png
   ```

3. **That's it!** The signature files will automatically reference it.

---

## Logo File Details

**Recommended:**
- **Format:** PNG (for email signatures)
- **Size:** 120x60px (small) or 240x120px (larger)
- **Name:** `ballcode-logo.png`
- **Location:** `email_system/assets/images/`

**Alternative:**
- **Format:** SVG (scalable, best quality)
- **Name:** `ballcode-logo.svg`
- **Location:** `email_system/assets/images/`

---

## After Adding Logo

### **Option 1: Use Hosted Logo (Recommended)**
1. Upload logo to ballcode.co website
2. Use `signature_with_logo.html` 
3. Logo URL: `https://ballcode.co/assets/images/ballcode-logo.png`

### **Option 2: Use Embedded Logo (Base64)**
1. Run: `./convert_logo_to_base64.sh`
2. Open `signature_base64.html`
3. Replace `BASE64_LOGO_HERE` with base64 string from `assets/images/logo_base64.txt`
4. Copy signature to email client

### **Option 3: Simple Signature (No Logo)**
- Use `signature_simple.html` - Works without logo file

---

## Logo Description (For Reference)

**BallCODE Logo:**
- Left: Stylized basketball (semi-circle) with dark blue, light blue, and orange segments
- Right: "BALL" above "CODE" text with code symbols (`=> >> - •` and `> = > - •`)
- Colors: Dark blue (#1a3d5c), Light blue (#4a90e2), Orange (#ff6b35)

**See:** `../documents/BALLCODE-LOGO-REFERENCE.md` for full details

---

**Once you add the logo file, your signature will be complete!** 🎨


