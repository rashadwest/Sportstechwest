// Renders graphics listed in _graphics/manifest.json to the paths they replace.
// Usage: node _graphics/render.js [name-filter]
// Set OUT_DIR to write previews elsewhere instead of overwriting the blog images.
// Needs Playwright (npm i -g playwright) and a Chromium build.
const path = require('path');
const fs = require('fs');
const { chromium } = require(process.env.PLAYWRIGHT_PATH || 'playwright');
const root = path.resolve(__dirname, '..');
const items = JSON.parse(fs.readFileSync(path.join(__dirname, 'manifest.json'), 'utf8'))
  .filter(i => !process.argv[2] || i.src.includes(process.argv[2]));
(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  for (const it of items) {
    const page = await browser.newPage({ viewport: { width: it.w, height: it.h }, deviceScaleFactor: it.scale || 1.5 });
    await page.goto('file://' + path.join(__dirname, it.src));
    await page.evaluate(() => document.fonts.ready);
    const out = process.env.OUT_DIR ? path.join(process.env.OUT_DIR, path.basename(it.out)) : path.join(root, it.out);
    const type = out.endsWith('.png') ? 'png' : 'jpeg';
    await page.screenshot({ path: out, type, ...(type === 'jpeg' ? { quality: 88 } : {}) });
    console.log('rendered', it.out);
    await page.close();
  }
  await browser.close();
})();
