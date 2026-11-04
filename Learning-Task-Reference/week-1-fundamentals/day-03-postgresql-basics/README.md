# Day 03: PostgreSQL basics

*Week 1: fundamentals (no AI-written code; AI only as a tutor)*

**Goal:** Write and explain core SQL: filtering, joins, aggregation, NULL handling, keys, indexes, transactions.

> **Project paths.** Where a path is given it is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch. Your own work stays in this folder.

## Read
- postgresql.org/docs: Tutorial chapters 2 and 3

## Where to look in the project
- `product/egpt_retail/warehouse/sql/ddl/052_silver_crm_deal.sql` — a real 'deal' table: compare its types, keys and indexes with the table you designed (after you finish yours)
- `product/egpt_retail/warehouse/sql/checks/` — small real SQL checks: read how they are written

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `select-filter/` | SELECT, WHERE, ORDER BY, LIMIT |
| `joins/` | Joins |
| `aggregation/` | GROUP BY, COUNT/SUM/AVG, HAVING |
| `nulls-types/` | Types and NULL |
| `keys-indexes-transactions/` | Keys, indexes, transactions |
| `practice/` | Practice: deals and dealers |

## Hands-on
- [ ] Create the two tables and seed 15-20 rows by hand
- [ ] Write the 6 required queries, each with a comment on what it returns and why
- [ ] Prove ROLLBACK leaves data unchanged

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] practice/schema.sql, seed.sql, queries.sql
- [ ] One NOTES.md + COMMANDS.md per topic folder
- [ ] LOG.md and EXPLAIN_BACK.md

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-03-<topic>` into `main`

## Demo
Run each query and explain its result.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Why does the left join return the deal without a dealer and the inner join does not?
- [ ] How does AVG treat NULL? How would you count NULLs as zero?
- [ ] What would an index on created_at help with?

## Done when
Every query is written by you and explained.
