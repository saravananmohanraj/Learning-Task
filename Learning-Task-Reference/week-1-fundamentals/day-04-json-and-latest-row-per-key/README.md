# Day 04: JSON in Postgres and 'latest row per key'

*Week 1: fundamentals (no AI-written code; AI only as a tutor)*

**Goal:** Master the core skill of the job: turning many repeated rows into one row per real thing, latest version.

> **Project paths.** Where a path is given it is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch. Your own work stays in this folder.

## Read
- postgresql.org/docs: JSON types and functions
- postgresql.org/docs: Tutorial 3.5 Window Functions

## Where to look in the project
- `product/egpt_retail/contracts/_fixtures/landing/raw/crm/dt=2026-09-01/crm-20260901T020000Z.ndjson` — real shape of an NDJSON drop (made-up data)
- `product/egpt_retail/contracts/_fixtures/landing/raw/crm/dt=2026-09-01/crm-20260901T060000Z.ndjson` — a later pull of the same source: find a record that appears twice
- `product/egpt_retail/warehouse/sql/ddl/030_landing.sql` — how raw rows are stored (landing.raw_row)
- `product/egpt_retail/warehouse/sql/conform/crm_deal.sql` — the team's own 'latest row per key' SQL: read it only AFTER you wrote yours, then compare

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `ndjson-jsonb/` | NDJSON and jsonb |
| `window-functions/` | Window functions and DISTINCT ON |
| `latest-per-key/` | Practice: messy deals |

## Hands-on
- [ ] Hand-write deals.ndjson (never real data); include repeated versions AND multi-line quotes
- [ ] Load into raw_deals
- [ ] Write right and wrong answers side by side in ANSWERS.md

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] latest-per-key/data/deals.ndjson
- [ ] latest-per-key/load script or \copy command
- [ ] latest-per-key/queries.sql
- [ ] latest-per-key/ANSWERS.md (right vs wrong, with reasons)
- [ ] LOG.md and EXPLAIN_BACK.md

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-04-<topic>` into `main`

## Demo
Show the file, raw table, and right and wrong answers side by side.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Walk through your window-function query clause by clause.
- [ ] Why is 'count the rows' wrong? Give two different reasons rows repeat.
- [ ] If two versions have exactly the same last_modified, which does your query pick? Is that safe?

## Done when
You can write the latest-per-key query from memory and explain why it is needed.

## Notes for this day
- Plan clarification: a deal's latest version can span several rows (one per product line). ROW_NUMBER()=1 returns ONE line only, so 'value at latest version' would be wrong. Keep ALL rows whose last_modified equals the deal's max last_modified (e.g. RANK()=1 or join to MAX per deal), then sum price*qty.
- In the example data the older version has 2 lines and the newer has 1. Decide and write down what that means (line removed? newer file only carries changed lines?). State your assumption in ANSWERS.md.
- Add a tie case on purpose (same last_modified, different content) and a deterministic tie-breaker (e.g. extra ORDER BY column).
