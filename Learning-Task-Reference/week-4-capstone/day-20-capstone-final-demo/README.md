# Day 20: Capstone 5: package and final demo

*Week 4: project-level capstone, 'Ask your data'*

**Goal:** Package the project like the team's cookbooks and present it live.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- A project someone else can run from README alone
- Dry-run from a clean state
- Presenting: problem, flow, live demo, what broke, what you learned

## Read
- cookbook/08_learning/ (README and TEST_LOG style)

## Where to look in the project
- `cookbook/STYLE_GUIDE.md` — README + TEST_LOG expectations
- `cookbook/08_learning/README.md` — model README
- `cookbook/08_learning/TEST_LOG.md` — model TEST_LOG

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `package/` | README and TEST_LOG |
| `dry-run/` | Clean-state dry run |
| `final-demo/` | Final demo |

## Hands-on lab
**Time:** about 3 hours · **You will build:** proof that someone else can run your project, and a rehearsed demo

1. Write the project README and TEST_LOG in cookbook style.
2. In an empty folder: fresh clone, fresh virtual environment, fresh database. Follow your own README exactly; fix every gap you find.
3. Ask your buddy to run it from the README alone.
4. Write RUNBOOK.md (exact commands) and REFLECTION.md (what you know now that you did not before).
5. Rehearse the 30-minute demo once against a timer.

**Expected output:** A buddy gets the same results from your README; a rehearsed demo that fits the time.

**Break it on purpose:** Delete your database and local files and run the demo flow end to end. What fails first?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Which three lines of your code are you least sure about? Learn them now.

### Checklist
- [ ] Write README and TEST_LOG
- [ ] Dry run on a clean machine/folder
- [ ] Rehearse the 30-minute demo

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] A buddy runs your README without help and gets the same results
- [ ] RUNBOOK.md and REFLECTION.md
- [ ] Demo completed live

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What will you say when something fails live?
- Which three lines of code are you least sure about? Learn them now.

## Suggested tools
- Fresh clone + venv
- asciinema / screen recording as a backup (optional)
- Mermaid in README

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-20-<topic>` into `main`

## Demo
30 minutes: pull > files > raw > clean > checks > KPIs > agent > evaluation, run live, then questions on any line.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] How does your load stay safe to re-run?
- [ ] Why does the KPI need the clean layer?
- [ ] Show one question the agent got wrong and explain why.

## Done when
A second run pulls only new or changed issues; the load re-runs without duplicates; the checks fail on bad data; the agent's numbers come from the tool; the eval score is reported and explained.

## Notes for this day
- Final checkpoint: mentor panel.
