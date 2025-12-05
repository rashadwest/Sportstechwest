#!/usr/bin/env node
/**
 * Cursor Draft Init Script
 * Creates a draft intent JSON file for starting a new blog post
 * Usage: node scripts/cursor-init-draft.js [title]
 */

const fs = require('fs');
const path = require('path');

// Create .cursor/drafts directory if it doesn't exist
const draftsDir = path.join(process.cwd(), '.cursor', 'drafts');
if (!fs.existsSync(draftsDir)) {
  fs.mkdirSync(draftsDir, { recursive: true });
}

// Get title from args or prompt
const title = process.argv[2] || 'Untitled Blog Post';
const slug = title
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-+|-+$/g, '');

const timestamp = new Date().toISOString().replace(/[:.]/g, '-').split('T')[0];
const filename = `${timestamp}-${slug}.json`;
const filepath = path.join(draftsDir, filename);

// Draft intent template
const draftIntent = {
  title: title,
  description: '',
  tags: [],
  category: 'Insights',
  notes: '',
  desiredDate: null, // Will be set to next available date after latest post
  createdAt: new Date().toISOString(),
  slug: slug
};

// Write draft intent
fs.writeFileSync(filepath, JSON.stringify(draftIntent, null, 2));

console.log(`✅ Draft intent created: ${filepath}`);
console.log(`\n📝 Next steps:`);
console.log(`   1. Edit the draft intent JSON with your content`);
console.log(`   2. Send to Claude (first pass) to generate Notion payload + Markdown outline`);
console.log(`   3. Run: node scripts/notion-upsert.js ${filepath}`);

process.exit(0);






