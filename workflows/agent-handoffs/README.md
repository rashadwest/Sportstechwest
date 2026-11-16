# CCO: Conversation Context Objects

A **CCO** is how we hand work from one agent to another without losing anything.

Every blog post we publish gets one. It holds the facts we verified, the research we cited, the decisions we already made, and what is left to do. Any agent that picks up the work (Claude, Cursor, Garvis, n8n, a new session) reads the CCO first and starts from where we left off. No re-researching. No reopening settled decisions.

This folder sits under `workflows/`, so it never publishes to the site.

---

## When we write one

- **Every post.** Created in the same branch as the post, before the PR.
- **Every handoff.** Whenever work moves to another agent, session, or tool.
- **Every major change.** If the post changes, the CCO changes in the same commit.

## How we name it

`CCO-YYYY-MM-<post-slug>.md`

Example: `CCO-2026-11-beasley-stephenson-post.md`

## How we write one

1. Copy `CCO-TEMPLATE.md`.
2. Fill every section. If a section does not apply, write "None" so the next agent knows it was considered.
3. Facts that sources disagree on go in **Verified facts** with the conflict spelled out.
4. Anything Rashad already decided goes in **Decisions already made**.
5. Commit it with the post.

## How an agent uses one

Start the next session with:

> Read `workflows/agent-handoffs/<CCO file>` first. Treat it as the source of truth for this topic, then continue with the next steps listed in it.

---

## The full post workflow (Thanos)

Every post runs the same play:

| Step | System | What happens |
|---|---|---|
| 1. Research + draft | @AIMCODE | CLEAR framework, peer-reviewed citations, Rashad's voice, one measurable takeaway |
| 2. Checks | @Garvis | `node scripts/validate-post.js`, images + alt text, markdown render, no em dashes, links |
| 3. Launch kit | @Launch | `workflows/blog-launch/<date>-<slug>-launch-kit.md` with social copy and a posting plan |
| 4. CCO | All | `workflows/agent-handoffs/CCO-<date>-<slug>.md` |
| 5. Ship | @Garvis | PR into `main`, CI passes, merge, confirm the live URL |
| 6. Measure | @Launch | One week later, record what worked |

## Index

| CCO | Post | Status |
|---|---|---|
| [CCO-2026-11-beasley-stephenson-post.md](CCO-2026-11-beasley-stephenson-post.md) | Practicing Isn't Pressure | Shipped to `main` |
