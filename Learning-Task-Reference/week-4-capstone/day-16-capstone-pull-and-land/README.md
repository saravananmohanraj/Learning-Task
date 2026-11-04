# Day 16: Capstone 1: pull and land files

*Week 4: project-level capstone, 'Ask your data'*

**Goal:** Build the incremental pull: GitHub issues to append-only NDJSON files with a safe watermark.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Watermark and append-only recap
- Why the file name has a UTC timestamp and is never overwritten
- Failure safety: what happens if the process dies between steps

## Read
- Your day 5 notes and function
- Your capstone design (day 15)

## Where to look in the project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md` — path convention and re-run behaviour: your files follow the same ideas
- `product/egpt_retail/contracts/_fixtures/landing/raw/crm/dt=2026-09-01/crm-20260901T020000Z.ndjson` — what a landed file looks like

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `pull/` | Pull issues since watermark |
| `land-files/` | Write NDJSON files |
| `watermark/` | Watermark in Postgres |
| `tests/` | Tests by hand |

## Hands-on lab
**Time:** about 3 hours · **You will build:** an incremental pull that lands append-only files and moves its watermark safely

1. Reuse your day-5 client to pull issues changed since the watermark.
2. Write each pull as an NDJSON file with a UTC-timestamped name; refuse to overwrite.
3. Store the watermark in Postgres; advance it only after the file is written.
4. Run twice. The second run should write only new or changed issues.
5. Write the tests: paging, path format, watermark only on success, overwrite refused.

**Expected output:** Run 1 creates a file; run 2 fetches only changes; tests pass.

**Break it on purpose:** Make the file write raise an error. Show the watermark did not move, then fix and re-run.

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** An issue changes after you pulled it: what happens on the next run?

### Checklist
- [ ] Implement pull + land + watermark
- [ ] Write tests first or alongside
- [ ] Run twice; then force a write failure

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Run 1 creates a file; run 2 creates only new/changed issues (RUN_OUTPUT.md)
- [ ] After a forced failure the watermark is unchanged (proof in output)
- [ ] All tests pass; each test has a one-line 'what it proves'

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- An issue changes after you pulled it: what happens on the next run?
- What if two runs start at the same time?

## Suggested tools
- httpx / requests
- pytest + `responses`/`respx` or hand-made fakes
- Local folder or Azurite for files
- psql

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-16-<topic>` into `main`

## Demo
Run twice, show the files and watermark, then show the failure case.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Why must the watermark advance only after the write succeeds?
- [ ] An issue changes after you pulled it: what happens?
- [ ] Walk through one test and say what bug it would catch.

## Done when
Two runs behave correctly and the failure case is safe.
