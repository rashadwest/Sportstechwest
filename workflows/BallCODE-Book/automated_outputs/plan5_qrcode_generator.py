#!/usr/bin/env python3
"""
Plan 5: QR Code Generator for Episode 1
Generates QR codes for story mode, game mode, and episode page.
"""

import qrcode
from qrcode.image.pil import PilImage
from pathlib import Path
import json

def generate_qr_code(url: str, output_path: Path, size: int = 10):
    """Generate QR code image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    
    return output_path

def main():
    """Main execution"""
    print("📱 Plan 5: QR Code Generator")
    print("=" * 60)
    
    # Define QR code URLs
    qr_links = {
        "story_mode": "https://ballcode.co/story?episode=1",
        "game_mode": "https://ballcode.co/play?mode=training&episode=1",
        "episode1_page": "https://ballcode.co/episode1"
    }
    
    # Create output directory
    output_dir = Path(__file__).parent / "qrcodes"
    output_dir.mkdir(exist_ok=True)
    
    generated_qrs = {}
    
    print("\nGenerating QR codes...")
    for name, url in qr_links.items():
        print(f"\n  Generating: {name}")
        print(f"  URL: {url}")
        
        output_path = output_dir / f"{name}_qr.png"
        
        try:
            generate_qr_code(url, output_path, size=10)
            generated_qrs[name] = {
                "url": url,
                "file": str(output_path),
                "status": "generated"
            }
            print(f"  ✅ Saved: {output_path}")
        except Exception as e:
            print(f"  ❌ Error: {e}")
            generated_qrs[name] = {
                "url": url,
                "file": None,
                "status": "error",
                "error": str(e)
            }
    
    # Save metadata
    metadata = {
        "episode": 1,
        "generation_date": "2025-01-27",
        "qrcodes": generated_qrs,
        "count": len(generated_qrs)
    }
    
    metadata_file = Path(__file__).parent / "plan5_qrcode_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print("\n" + "=" * 60)
    print(f"✅ Generated {len(generated_qrs)} QR codes")
    print(f"📁 Output directory: {output_dir}")
    print(f"📄 Metadata: {metadata_file}")
    print("\nQR codes ready for book integration!")

if __name__ == "__main__":
    main()




