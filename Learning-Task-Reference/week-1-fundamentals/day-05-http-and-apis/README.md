# Day 05: HTTP and APIs

*Week 1: fundamentals (no AI-written code; AI only as a tutor)*

**Goal:** Understand HTTP and write a robust paginated API client with retries.

> **Project paths.** Where a path is given it is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch. Your own work stays in this folder.

## Read
- GitHub REST docs: 'Using pagination in the REST API' and 'Rate limits' (docs.github.com/rest)

## Where to look in the project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md` — 'Storage path convention' and 'Re-run behaviour' preview where the pull is going

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `http-basics/` | HTTP basics |
| `auth-tokens/` | Authentication and secrets |
| `pagination-rate-limits/` | Pagination and rate limits |
| `fetch-issues/` | Practice: fetch_issues client |

## Hands-on
- [ ] curl experiments recorded in http-basics/COMMANDS.md
- [ ] Write fetch_issues.py + tests
- [ ] Run for one week of issues: record pages fetched and rate-limit headers

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] http-basics/, auth-tokens/, pagination-rate-limits/ notes
- [ ] fetch-issues/fetch_issues.py, test_fetch_issues.py, RUN_OUTPUT.md
- [ ] LOG.md and EXPLAIN_BACK.md

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-05-<topic>` into `main`

## Demo
Run your function for one week of issues; show pages fetched and rate-limit headers.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does a 429 mean and what should a client do? What about 401?
- [ ] How does your code know there is another page?
- [ ] Why is since useful when you pull the same source every day?

## Done when
Your function and tests are your own and you can explain the retry logic.

## Notes for this day
- The plan's example date (2026-09-01) may now return an empty week: choose a window where the repo has activity.
- The GitHub issues endpoint also returns pull requests; decide whether to filter them (they have a pull_request key) and note it.
- Unauthenticated limit is low (60/hr); a read-only token via env var is fine, never committed.
- Week 1 end check: short SQL test on day 4 data + 15-minute explain-back of two days chosen by the reviewer.
