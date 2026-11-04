# Practice: messy deals

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 04: JSON in Postgres and 'latest row per key'** · [day README](../README.md)

## Understand it first (before you do anything)
Before the steps, answer these in your `ACTIVITY_LOG.md`, in your own words (read the docs first):
- What is this, in one or two sentences of your own?
- How does it work, step by step? Draw the flow.
- Why do we need it? What would go wrong without it?
- How will you know it is working? What would you check?

## What to do
1. data/deals.ndjson: made-up, messy: same deal repeated with different last_modified; a quote with 3 product-line rows
2. raw_deals(payload jsonb) loaded
3. Queries: row count; distinct deals; latest stage per deal; value per deal at latest version; Closed Won deals
4. The WRONG query (count Closed Won rows) and a written explanation of why numbers differ

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/warehouse/sql/conform/crm_deal.sql` — compare with yours afterwards
- `product/egpt_retail/contracts/_fixtures/landing/raw/crm/dt=2026-09-01/` — real-shaped NDJSON with repeats

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `deals.ndjson`
- load script or \copy command
- `queries.sql`
- answers.md (right vs wrong, with reasons)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
