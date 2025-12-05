# Plan 5: QR Code Integration Guide

**Status:** QR Codes Generated - Ready for Book Integration  
**Completion:** 50% (QR codes generated, integration pending)

---

## Generated QR Codes

Three QR codes have been generated for Episode 1:

1. **Story Mode QR Code** (`story_mode_qr.png`)
   - Links to: `https://ballcode.co/story?episode=1`
   - Use: For accessing Unity story mode

2. **Game Mode QR Code** (`game_mode_qr.png`)
   - Links to: `https://ballcode.co/play?mode=training&episode=1`
   - Use: For accessing Training Mode exercise

3. **Episode 1 Page QR Code** (`episode1_page_qr.png`)
   - Links to: `https://ballcode.co/episode1`
   - Use: For accessing simple web page version

---

## QR Code Placement in Book

### Recommended Placement

#### Option 1: Title Page
- Place Story Mode QR code on Episode 1 title page
- Size: 2" x 2" (or appropriate for book size)
- Position: Bottom right or center

#### Option 2: After Story Acts
- Place Game Mode QR code after Act III
- Size: 2" x 2"
- Position: Center or bottom of page
- Context: "Try the exercise: Scan this code to play Training Mode"

#### Option 3: Skill Pit-Stop Section
- Place Episode 1 Page QR code in Skill Pit-Stop section
- Size: 1.5" x 1.5"
- Position: Sidebar or bottom
- Context: "Access online version: Scan for full Episode 1 experience"

#### Option 4: Back Cover or End Page
- Place all three QR codes on back cover or end page
- Size: 1.5" x 1.5" each
- Layout: Three columns or grid
- Labels: "Story Mode", "Game Mode", "Web Version"

---

## Integration Steps

### Step 1: Prepare QR Code Images

1. **Locate generated QR codes:**
   - `automated_outputs/qrcodes/story_mode_qr.png`
   - `automated_outputs/qrcodes/game_mode_qr.png`
   - `automated_outputs/qrcodes/episode1_page_qr.png`

2. **Verify image quality:**
   - Check that QR codes are clear and scannable
   - Ensure sufficient contrast (black on white)
   - Test scanning with phone camera

3. **Resize if needed:**
   - For print: Ensure 300 DPI minimum
   - For digital: Optimize file size
   - Maintain square aspect ratio

### Step 2: Add to Book Layout

1. **Open book design file** (InDesign, Canva, etc.)

2. **Import QR code images:**
   - Place images in appropriate locations
   - Maintain clear space around QR codes (minimum 0.25" margin)

3. **Add labels/context:**
   - Label each QR code clearly
   - Add brief instructions: "Scan to access..."
   - Ensure text is readable

4. **Test layout:**
   - Verify QR codes are not too small
   - Check that they don't interfere with text
   - Ensure good visual balance

### Step 3: Print Testing

1. **Print test page** with QR codes
2. **Test scanning** with multiple devices:
   - iPhone camera
   - Android camera
   - QR code scanner apps
3. **Verify URLs** work correctly
4. **Check print quality** (no pixelation or blur)

---

## QR Code Specifications

### Technical Requirements

- **Format:** PNG (with transparency if needed)
- **Size:** Minimum 1" x 1" for print (2" x 2" recommended)
- **Resolution:** 300 DPI minimum for print
- **Contrast:** High contrast (black on white)
- **Margin:** Minimum 0.25" clear space around QR code

### Design Guidelines

- **Placement:** Near relevant content, not isolated
- **Context:** Always include label or instruction
- **Size:** Large enough to scan easily (minimum 1" x 1")
- **Style:** Can add subtle styling but maintain scannability

---

## URL Structure

### Story Mode URL
```
https://ballcode.co/story?episode=1
```
- Parameters: `episode=1` (Episode number)
- Future: Can add `&source=book` to track book usage

### Game Mode URL
```
https://ballcode.co/play?mode=training&episode=1
```
- Parameters:
  - `mode=training` (Game mode type)
  - `episode=1` (Episode number)
- Future: Can add `&source=book` to track book usage

### Episode Page URL
```
https://ballcode.co/episode1
```
- Simple path-based URL
- Direct access to Episode 1 web page

---

## Testing Checklist

Before finalizing book layout:

- [ ] All QR codes scan successfully
- [ ] URLs work correctly when scanned
- [ ] QR codes are appropriate size (minimum 1" x 1")
- [ ] Print quality is good (300 DPI, no pixelation)
- [ ] Labels/instructions are clear
- [ ] QR codes don't interfere with text
- [ ] Tested on multiple devices (iPhone, Android)
- [ ] Tested with multiple QR scanner apps

---

## Future Enhancements

### Tracking Parameters
Add `&source=book` to URLs to track book usage:
- `https://ballcode.co/story?episode=1&source=book`
- `https://ballcode.co/play?mode=training&episode=1&source=book`

### Analytics
Track QR code scans to understand:
- Which QR codes are used most
- User engagement from book
- Conversion from book to digital

---

## Files Generated

- `qrcodes/story_mode_qr.png` - Story Mode QR code
- `qrcodes/game_mode_qr.png` - Game Mode QR code
- `qrcodes/episode1_page_qr.png` - Episode Page QR code
- `plan5_qrcode_metadata.json` - QR code metadata

---

**Status:** ✅ QR codes generated and ready  
**Next Step:** Integrate into book layout




