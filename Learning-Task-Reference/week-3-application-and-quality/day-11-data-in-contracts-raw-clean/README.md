# Day 11: Data in: contracts, raw and clean

*Week 3: the EnterpriseGPT application, quality and capstone design*

**Goal:** Learn how the application brings data in and keeps it safe, by tracing one record end to end.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Where a model runs and where it must never run in the whole data flow (raw files > raw table > clean > semantic layer > KPI values > dashboards/alerts/use cases)
- Landing contract (file layout, fields) and load contract (how files become rows)
- Raw files never change; raw table keeps every version; clean is one row per real thing
- Watermark (pulled up to here) and append-only storage
- Idempotent load and defects/blocked load

## Read
- product/egpt_retail/contracts/LANDING_CONTRACT.md
- product/egpt_retail/warehouse/LOAD_CONTRACT.md

## Where to look in the project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md` — read in full: path convention, file format, re-run behaviour
- `product/egpt_retail/warehouse/LOAD_CONTRACT.md` — read in full: rules, gates, when a load does not finish
- `cookbook/94_retail/C01_landing_contract.py` — runs the landing contract against fixtures
- `cookbook/94_retail/R04_landing_to_silver.py` — loads fixtures raw > silver (no object storage needed, reads files from disk)
- `product/egpt_retail/contracts/_fixtures/landing/` — the made-up input files
- `product/egpt_retail/warehouse/sql/ddl/` — table definitions (030 landing, 05x silver)
- `product/egpt_retail/warehouse/sql/conform/` — the SQL that turns raw rows into clean rows
- `product/egpt_retail/warehouse/sql/defects/uncoercible.sql` — what counts as a defect
- `deploy/compose.yaml` — the 'postgres' service you start for this day

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `data-flow-drawing/` | Data flow drawing |
| `contracts/` | Contracts |
| `run-examples/` | Run the examples |
| `trace-record/` | Trace one record |
| `idempotency/` | Idempotency and watermark |

## Hands-on lab
**Time:** about 3 hours · **You will build:** a traced record across file, landing table and clean table, and proof that a re-load changes nothing

1. Draw the data flow from memory before opening any code; mark where a model may and may not run.
2. Start Postgres: `docker compose -f deploy/compose.yaml up -d postgres`.
3. Run `cookbook/94_retail/C01_landing_contract.py`, then `R04_landing_to_silver.py` with `EGPT_RETAIL_WAREHOUSE_DB_URL` set (see the script header).
4. Pick one record from `product/egpt_retail/contracts/_fixtures/landing/`. Find it in the NDJSON file, in `landing.raw_row`, and in the clean (silver) table. Find the conform SQL that moved it.
5. Run R04 again. Compare row counts before and after.

**Expected output:** One record shown in three places with the query for each, the SQL file name, and equal counts after the second load.

**Break it on purpose:** Copy a fixture file, null one key column in the copy, point `EGPT_LANDING_FIXTURES_ROOT` at the copy and load it. What does the pipeline report?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Where exactly does the code prevent duplicates?

### Checklist
- [ ] Draw the one-page data flow before you open any code
- [ ] Run both examples
- [ ] Trace one record across 3 places + SQL
- [ ] Load the same file twice and show nothing new
- [ ] Find the defect handling in code

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] data-flow-drawing/: diagram + one sentence per layer + model-runs / model-never-runs marked
- [ ] trace-record/TRACE.md: file line, raw_row query + result, silver query + result, SQL file name
- [ ] idempotency/NOTES.md names file and function that prevents duplicates
- [ ] Row counts before/after a second load (equal)

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What would a bad row look like and where would it end up?
- What breaks if the watermark moves first?

## Suggested tools
- psql / pgcli / DBeaver
- `git grep` to find code
- jq for fixtures

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-11-<topic>` into `main`

## Demo
Show the same record in all three places and the SQL that moved it.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What happens if the same file is loaded twice? Show where the code prevents duplicates.
- [ ] What is a 'defect' in this pipeline, and what happens to a bad row?
- [ ] Why must a watermark move only after the write succeeds?

## Done when
You can trace a record without help.
