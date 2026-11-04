# Day 18: Capstone 3: checks and KPIs

*Week 4: project-level capstone, 'Ask your data'*

**Goal:** Prove the data is right with SQL checks, then compute KPIs in SQL only.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Data quality dimensions: uniqueness, validity, consistency, completeness
- A check you never saw fail proves nothing
- KPI definition: what counts, which date, which time zone, edge cases

## Read
- Postgres docs: date_trunc, percentile_cont, generate_series

## Where to look in the project
- `product/egpt_retail/warehouse/sql/checks/` — real checks to model yours on
- `cookbook/94_retail/K11_kpi_formula_shape.py` — how real KPI formulas are shaped
- `product/egpt_retail/kpi/` — KPI code

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `checks/` | SQL checks |
| `fail-on-purpose/` | Make checks fail |
| `kpis/` | KPIs in SQL |
| `wrong-vs-right/` | Wrong vs right |

## Hands-on lab
**Time:** about 3 hours · **You will build:** four SQL checks that you have seen fail, and KPIs computed the right way

1. Write the checks: one row per issue in clean; distinct keys in raw equal rows in clean; no issue closed before created; no failed casts.
2. Insert a bad record for each check, show it fail, then remove it.
3. Write issues closed per week and median days to close for the last 8 weeks, including weeks with zero.
4. Compute the same two KPIs wrongly from raw (counting rows) and put right and wrong side by side.

**Expected output:** Pass and fail output for every check, an 8-row KPI result, and a right-vs-wrong table.

**Break it on purpose:** Reopen one issue in your data. How should each KPI treat it, and does your SQL?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Which check would catch the counting-rows mistake?

### Checklist
- [ ] Write checks
- [ ] Break each on purpose
- [ ] Write KPI SQL
- [ ] Compare with raw-based wrong answers

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] checks/PROOF.md: pass output and fail output per check
- [ ] kpis/kpi.sql and an 8-row result
- [ ] wrong-vs-right table with explanation

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- Which check would catch the counting-rows mistake from day 4?
- How should a reopened issue count?

## Suggested tools
- psql
- SQL files run by a small Python/pytest runner
- generate_series for date spines

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-18-<topic>` into `main`

## Demo
Checks green, each failing on bad data, KPI results, wrong vs right.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does each check protect against?
- [ ] Why does the KPI need the clean layer?
- [ ] What would change if an issue were reopened?

## Done when
Checks fail when they should and KPI numbers are correct.
