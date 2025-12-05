// Usage:
//   node download-image.js "https://example.com/image.png" \
//        /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-server-hero.png

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function main() {
  const [,, url, outPath] = process.argv;
  if (!url || !outPath) {
    console.error('Usage: node download-image.js <url> <outputPath>');
    process.exit(1);
  }

  const dir = path.dirname(outPath);
  fs.mkdirSync(dir, { recursive: true });

  const res = await fetch(url);
  if (!res.ok) {
    console.error(`Failed to download: ${res.status} ${res.statusText}`);
    process.exit(1);
  }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  console.log(`Saved: ${outPath}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});


