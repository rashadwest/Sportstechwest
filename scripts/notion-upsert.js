#!/usr/bin/env node
/**
 * Notion Upsert Script
 * Creates or updates a Notion page from draft intent or Claude output
 * Usage: node scripts/notion-upsert.js <draft-file.json> [notion-payload.json]
 */

const fs = require('fs');
const path = require('path');
const { Client } = require('@notionhq/client');

// Load environment variables (optional, use dotenv if available)
try {
  require('dotenv').config({ path: path.join(process.cwd(), '.env') });
} catch (e) {
  // dotenv not installed, use environment variables directly
}

const NOTION_TOKEN = process.env.NOTION_API_TOKEN;
const NOTION_DATABASE_ID = process.env.NOTION_DATABASE_ID;

if (!NOTION_TOKEN) {
  console.error('❌ Error: NOTION_API_TOKEN environment variable not set');
  console.error('   Create a .env file with NOTION_API_TOKEN=your_token');
  process.exit(1);
}

if (!NOTION_DATABASE_ID) {
  console.error('❌ Error: NOTION_DATABASE_ID environment variable not set');
  console.error('   Create a .env file with NOTION_DATABASE_ID=your_database_id');
  process.exit(1);
}

const notion = new Client({ auth: NOTION_TOKEN });

function kebabCase(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

function parseNotionPayload(payload) {
  // Handle both JSON string and object
  if (typeof payload === 'string') {
    try {
      payload = JSON.parse(payload);
    } catch (e) {
      console.error('❌ Error: Invalid JSON payload');
      process.exit(1);
    }
  }

  return {
    title: payload.title || '',
    description: payload.description || '',
    tags: Array.isArray(payload.tags) ? payload.tags : [],
    category: payload.category || 'Insights',
    body_draft: payload.body_draft || '',
    thumbnail_url: payload.thumbnail_url || '',
    date_hint: payload.date_hint || null,
    slug: payload.slug || kebabCase(payload.title || '')
  };
}

async function createOrUpdatePage(payload) {
  const slug = payload.slug || kebabCase(payload.title);

  // Check if page exists (by slug in Title or Slug property)
  try {
    const response = await notion.databases.query({
      database_id: NOTION_DATABASE_ID,
      filter: {
        or: [
          {
            property: 'Title',
            title: {
              equals: payload.title
            }
          },
          {
            property: 'Slug',
            rich_text: {
              equals: slug
            }
          }
        ]
      }
    });

    if (response.results.length > 0) {
      // Update existing page
      const pageId = response.results[0].id;
      console.log(`📝 Updating existing Notion page: ${pageId}`);

      const properties = {
        Title: {
          title: [{ text: { content: payload.title } }]
        },
        Slug: {
          rich_text: [{ text: { content: slug } }]
        },
        Status: {
          select: { name: 'Draft' }
        },
        Description: {
          rich_text: [{ text: { content: payload.description } }]
        },
        Tags: {
          multi_select: payload.tags.map(tag => ({ name: tag }))
        },
        Categories: {
          multi_select: [{ name: payload.category }]
        },
        Author: {
          rich_text: [{ text: { content: 'Rashad West' } }]
        }
      };

      if (payload.thumbnail_url) {
        properties.Thumbnail = { url: payload.thumbnail_url };
      }

      if (payload.date_hint) {
        properties.Date = { date: { start: payload.date_hint } };
      }

      await notion.pages.update({
        page_id: pageId,
        properties
      });

      // Clear existing blocks and add new content
      const blocks = await notion.blocks.children.list({ block_id: pageId });
      for (const block of blocks.results) {
        await notion.blocks.delete({ block_id: block.id });
      }

      // Add body content
      if (payload.body_draft) {
        const bodyBlocks = parseMarkdownToBlocks(payload.body_draft);
        await notion.blocks.children.append({
          block_id: pageId,
          children: bodyBlocks
        });
      }

      const pageUrl = `https://notion.so/${pageId.replace(/-/g, '')}`;
      console.log(`✅ Page updated: ${pageUrl}`);
      return { pageId, pageUrl, updated: true };
    }
  } catch (error) {
    console.warn('⚠️  Could not check for existing page:', error.message);
  }

  // Create new page
  console.log('📝 Creating new Notion page...');

  const properties = {
    Title: {
      title: [{ text: { content: payload.title } }]
    },
    Slug: {
      rich_text: [{ text: { content: slug } }]
    },
    Status: {
      select: { name: 'Draft' }
    },
    Description: {
      rich_text: [{ text: { content: payload.description } }]
    },
    Tags: {
      multi_select: payload.tags.map(tag => ({ name: tag }))
    },
    Categories: {
      multi_select: [{ name: payload.category }]
    },
    Author: {
      rich_text: [{ text: { content: 'Rashad West' } }]
    }
  };

  if (payload.thumbnail_url) {
    properties.Thumbnail = { url: payload.thumbnail_url };
  }

  if (payload.date_hint) {
    properties.Date = { date: { start: payload.date_hint } };
  }

  const page = await notion.pages.create({
    parent: { database_id: NOTION_DATABASE_ID },
    properties
  });

  // Add body content
  if (payload.body_draft) {
    const bodyBlocks = parseMarkdownToBlocks(payload.body_draft);
    await notion.blocks.children.append({
      block_id: page.id,
      children: bodyBlocks
    });
  }

  const pageUrl = `https://notion.so/${page.id.replace(/-/g, '')}`;
  console.log(`✅ Page created: ${pageUrl}`);
  return { pageId: page.id, pageUrl, updated: false };
}

function parseMarkdownToBlocks(markdown) {
  const blocks = [];
  const lines = markdown.split('\n');
  let currentParagraph = [];

  for (const line of lines) {
    const trimmed = line.trim();

    // Flush paragraph if we hit a header
    if (trimmed.startsWith('##')) {
      if (currentParagraph.length > 0) {
        blocks.push({
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [{ type: 'text', text: { content: currentParagraph.join(' ').trim() } }]
          }
        });
        currentParagraph = [];
      }
      // Add heading
      const headingText = trimmed.replace(/^##+\s*/, '');
      blocks.push({
        object: 'block',
        type: 'heading_2',
        heading_2: {
          rich_text: [{ type: 'text', text: { content: headingText } }]
        }
      });
    } else if (trimmed === '---') {
      // Horizontal rule
      if (currentParagraph.length > 0) {
        blocks.push({
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [{ type: 'text', text: { content: currentParagraph.join(' ').trim() } }]
          }
        });
        currentParagraph = [];
      }
      blocks.push({
        object: 'block',
        type: 'divider',
        divider: {}
      });
    } else if (trimmed.length > 0) {
      currentParagraph.push(trimmed);
    } else {
      // Empty line - flush paragraph
      if (currentParagraph.length > 0) {
        blocks.push({
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [{ type: 'text', text: { content: currentParagraph.join(' ').trim() } }]
          }
        });
        currentParagraph = [];
      }
    }
  }

  // Flush remaining paragraph
  if (currentParagraph.length > 0) {
    blocks.push({
      object: 'block',
      type: 'paragraph',
      paragraph: {
        rich_text: [{ type: 'text', text: { content: currentParagraph.join(' ').trim() } }]
      }
    });
  }

  return blocks.slice(0, 100); // Notion limit
}

async function main() {
  const draftFile = process.argv[2];
  const payloadFile = process.argv[3];

  if (!draftFile) {
    console.error('❌ Error: Draft file path required');
    console.error('   Usage: node scripts/notion-upsert.js <draft-file.json> [notion-payload.json]');
    process.exit(1);
  }

  if (!fs.existsSync(draftFile)) {
    console.error(`❌ Error: Draft file not found: ${draftFile}`);
    process.exit(1);
  }

  // Load draft intent
  const draftIntent = JSON.parse(fs.readFileSync(draftFile, 'utf-8'));

  let payload;
  if (payloadFile && fs.existsSync(payloadFile)) {
    // Use Claude-generated payload
    payload = parseNotionPayload(JSON.parse(fs.readFileSync(payloadFile, 'utf-8')));
  } else {
    // Use draft intent as payload
    payload = {
      title: draftIntent.title,
      description: draftIntent.description,
      tags: draftIntent.tags,
      category: draftIntent.category,
      body_draft: draftIntent.notes,
      thumbnail_url: '',
      date_hint: draftIntent.desiredDate,
      slug: draftIntent.slug
    };
  }

  try {
    const result = await createOrUpdatePage(payload);
    console.log(`\n📋 Notion page ${result.updated ? 'updated' : 'created'}:`);
    console.log(`   URL: ${result.pageUrl}`);
    console.log(`   Page ID: ${result.pageId}`);
    console.log(`\n✅ Next steps:`);
    console.log(`   1. Review the page in Notion`);
    console.log(`   2. Set Status to "Ready to Publish" to trigger Glif workflow`);
  } catch (error) {
    console.error('❌ Error creating/updating Notion page:', error.message);
    if (error.body) {
      console.error('   Details:', JSON.stringify(error.body, null, 2));
    }
    process.exit(1);
  }
}

main();

