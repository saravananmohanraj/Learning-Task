# Day 17: Capstone 2: raw table and clean view

*Week 4: project-level capstone, 'Ask your data'*

**Goal:** Load files into raw.github_issue idempotently and build clean.issue as a view.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Raw keeps every version; clean is latest per issue
- Why clean is a view over raw, not a copy
- Deterministic ordering for ties

## Read
- Your day 4 notes (latest per key)
- Postgres docs: INSERT ... ON CONFLICT

## Where to look in the project
- `product/egpt_retail/warehouse/sql/ddl/030_landing.sql` — real raw-row table
- `product/egpt_retail/warehouse/sql/conform/crm_deal.sql` — real clean SQL for a deal
- `product/egpt_retail/warehouse/LOAD_CONTRACT.md` — load rules to mirror at small scale

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `raw-load/` | raw.github_issue |
| `clean-view/` | clean.issue |
| `proof/` | Proof of correctness |

## Hands-on lab
**Time:** about 2.5 hours · **You will build:** a re-runnable raw loader and a clean view

1. Create `raw.github_issue` (file path, line number, pulled at, record key, payload jsonb) with a unique key on file path + line number.
2. Write the loader; load every landed file.
3. Run it again and compare row counts.
4. Create the view `clean.issue`: one row per issue, latest version, typed columns, deterministic tie-break.
5. Hand-check 3 issues from the API to clean.

**Expected output:** Second load inserts 0 rows; clean has one row per issue number; three hand-checks written down.

**Break it on purpose:** Edit a copy of one issue so two versions share the same updated_at. Does your view pick the same row every time?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Why is clean a view over raw rather than a copy?

### Checklist
- [ ] Write DDL and loader
- [ ] Write the view
- [ ] Run loader twice and compare counts
- [ ] Hand-check 3 issues

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Second load inserts 0 rows (counts shown)
- [ ] clean.issue has exactly one row per issue number
- [ ] proof/NOTES.md with the 3 hand-checks

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What happens to an issue that was reopened?
- Which columns could fail a cast?

## Suggested tools
- psql / DBeaver
- SQLAlchemy or psycopg
- EXPLAIN to check the view's cost

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-17-<topic>` into `main`

## Demo
Load, re-load, show no duplicates; show clean vs raw for one issue.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] How does your load stay safe to re-run?
- [ ] Why is clean a view over raw rather than a copy?
- [ ] Which tie-breaker did you choose and why?

## Done when
Re-running changes nothing and clean is correct.
