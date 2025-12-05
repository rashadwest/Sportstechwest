#!/usr/bin/env node
/**
 * Post Validation Script
 * Validates Jekyll blog post front matter, date rules, and image paths
 * Usage: node scripts/validate-post.js <post-file.md>
 */

const fs = require('fs');
const path = require('path');

const POSTS_DIR = path.join(process.cwd(), '_posts');
const IMAGES_DIR = path.join(process.cwd(), 'assets', 'images', 'blog-img');

// Required front matter fields
const REQUIRED_FIELDS = [
  'layout',
  'title',
  'description',
  'thumbnail',
  'badge_color',
  'trending',
  'simple_nav',
  'date',
  'tags',
  'categories',
  'author'
];

function parseFrontMatter(content) {
  const frontMatterMatch = content.match(/^---\n([\s\S]*?)\n---\n/);
  if (!frontMatterMatch) {
    return null;
  }

  const frontMatter = {};
  const lines = frontMatterMatch[1].split('\n');

  for (const line of lines) {
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) continue;

    const key = line.slice(0, colonIndex).trim();
    let value = line.slice(colonIndex + 1).trim();

    // Remove quotes
    if ((value.startsWith('"') && value.endsWith('"')) || 
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    // Parse arrays
    if (value.startsWith('[') && value.endsWith(']')) {
      value = value.slice(1, -1).split(',').map(v => v.trim().replace(/['"]/g, ''));
    }

    frontMatter[key] = value;
  }

  return frontMatter;
}

function getLatestPostDate() {
  const postsDir = path.join(process.cwd(), '_posts');
  if (!fs.existsSync(postsDir)) {
    return null;
  }

  const files = fs.readdirSync(postsDir);
  const posts = files.filter(f => f.startsWith('2025-') && f.endsWith('.md'));
  let latestDate = null;

  for (const postFile of posts) {
    const postPath = path.join(postsDir, postFile);
    const content = fs.readFileSync(postPath, 'utf-8');
    const fm = parseFrontMatter(content);
    if (fm && fm.date) {
      const date = new Date(fm.date);
      if (!latestDate || date > latestDate) {
        latestDate = date;
      }
    }
  }

  return latestDate;
}

function validateDate(dateStr) {
  const date = new Date(dateStr);
  const year = date.getFullYear();
  const latestDate = getLatestPostDate();

  const errors = [];

  if (year !== 2025) {
    errors.push(`Date year must be 2025, got ${year}`);
  }

  if (latestDate && date <= latestDate) {
    errors.push(`Date must be after latest post date: ${latestDate.toISOString().split('T')[0]}`);
  }

  return errors;
}

function validateTags(tags) {
  const errors = [];
  if (!Array.isArray(tags)) {
    errors.push('Tags must be an array');
    return errors;
  }

  for (const tag of tags) {
    if (typeof tag !== 'string') {
      errors.push(`Tag must be a string: ${tag}`);
    }
  }

  return errors;
}

function validateCategories(categories) {
  const errors = [];
  if (!Array.isArray(categories)) {
    errors.push('Categories must be an array');
    return errors;
  }

  const validCategories = ['Insights', 'Tutorial', 'News'];
  for (const cat of categories) {
    if (!validCategories.includes(cat)) {
      errors.push(`Invalid category: ${cat}. Must be one of: ${validCategories.join(', ')}`);
    }
  }

  return errors;
}

function validateThumbnail(thumbnailPath) {
  const errors = [];
  if (!thumbnailPath || !thumbnailPath.startsWith('/assets/images/blog-img/')) {
    errors.push('Thumbnail must start with /assets/images/blog-img/');
    return errors;
  }

  const filename = thumbnailPath.replace('/assets/images/blog-img/', '');
  const imagePath = path.join(IMAGES_DIR, filename);

  if (!fs.existsSync(imagePath)) {
    errors.push(`Thumbnail image not found: ${imagePath}`);
  }

  return errors;
}

function validateImagePaths(content) {
  const errors = [];
  const imageRegex = /src=["']([^"']+)["']/g;
  let match;

  while ((match = imageRegex.exec(content)) !== null) {
    const imagePath = match[1];
    if (imagePath.startsWith('/assets/images/blog-img/')) {
      const filename = imagePath.replace('/assets/images/blog-img/', '');
      const fullPath = path.join(IMAGES_DIR, filename);

      if (!fs.existsSync(fullPath)) {
        errors.push(`Image not found: ${imagePath} (${fullPath})`);
      }
    }
  }

  return errors;
}

function validateMarkdownFormat(content) {
  const errors = [];
  const warnings = [];

  // Check for <br> tags (should use blank lines instead)
  if (content.includes('<br>') || content.includes('<br />')) {
    warnings.push('Found <br> tags. Use blank lines between paragraphs instead.');
  }

  // Check header levels (should use ## not ###)
  const h3Regex = /^###\s+/gm;
  if (h3Regex.test(content)) {
    warnings.push('Found ### headers. Use ## for section headers instead.');
  }

  return { errors, warnings };
}

async function validatePost(postFile) {
  const errors = [];
  const warnings = [];

  if (!fs.existsSync(postFile)) {
    console.error(`❌ Error: Post file not found: ${postFile}`);
    process.exit(1);
  }

  const content = fs.readFileSync(postFile, 'utf-8');
  const frontMatter = parseFrontMatter(content);

  if (!frontMatter) {
    errors.push('Missing or invalid front matter (must start with ---)');
    return { errors, warnings };
  }

  // Validate required fields
  for (const field of REQUIRED_FIELDS) {
    if (!(field in frontMatter)) {
      errors.push(`Missing required field: ${field}`);
    }
  }

  // Validate date
  if (frontMatter.date) {
    const dateErrors = validateDate(frontMatter.date);
    errors.push(...dateErrors);
  }

  // Validate tags
  if (frontMatter.tags) {
    const tagErrors = validateTags(frontMatter.tags);
    errors.push(...tagErrors);
  }

  // Validate categories
  if (frontMatter.categories) {
    const catErrors = validateCategories(frontMatter.categories);
    errors.push(...catErrors);
  }

  // Validate thumbnail
  if (frontMatter.thumbnail) {
    const thumbErrors = validateThumbnail(frontMatter.thumbnail);
    errors.push(...thumbErrors);
  }

  // Validate image paths in content
  const imageErrors = validateImagePaths(content);
  errors.push(...imageErrors);

  // Validate markdown format
  const formatCheck = validateMarkdownFormat(content);
  errors.push(...formatCheck.errors);
  warnings.push(...formatCheck.warnings);

  return { errors, warnings };
}

async function main() {
  const postFile = process.argv[2];

  if (!postFile) {
    console.error('❌ Error: Post file path required');
    console.error('   Usage: node scripts/validate-post.js <post-file.md>');
    process.exit(1);
  }

  const result = await validatePost(postFile);

  if (result.warnings.length > 0) {
    console.log('\n⚠️  Warnings:');
    for (const warning of result.warnings) {
      console.log(`   - ${warning}`);
    }
  }

  if (result.errors.length > 0) {
    console.log('\n❌ Validation Errors:');
    for (const error of result.errors) {
      console.log(`   - ${error}`);
    }
    process.exit(1);
  }

  console.log('✅ Post validation passed!');
  process.exit(0);
}

main();

