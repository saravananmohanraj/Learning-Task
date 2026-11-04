# Day 15: Capstone design: plan before you build

*Week 3: the EnterpriseGPT application, quality and capstone design*

**Goal:** Design the 'Ask your data' project on paper, review it with your buddy, and only then start building in week 4.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- The three use-case kinds (analytics automation, process automation, decision intelligence): which one is your capstone closest to and why?
- Where each part of your project sits in the layers (raw files, raw table, clean, KPI, agent)
- Agent safety: prompt injection, secrets to a model, cost limits, never trusting a model's number

## Read
- Section 2 of this plan (EnterpriseGPT in one page)
- Your notes from days 4, 5, 8, 9, 11-13

## Where to look in the project
- `docs/plan/analytics-automation-design.md` — the analytics-automation use-case kind
- `docs/plan/delivery-plan.md` — how a plan is written here
- `cookbook/00_quickstart/agent_with_guardrails.py` — input guardrails
- `libs/agno/egpt/guardrails/prompt_injection.py` — prompt-injection guard
- `libs/agno/egpt/guardrails/pii.py` — PII guard
- `cookbook/STYLE_GUIDE.md` — README + TEST_LOG expectations for your project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md` — model for your own file layout and re-run rules

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `architecture/` | Architecture one-pager |
| `data-design/` | Data design |
| `agent-design/` | Agent design |
| `test-and-eval-plan/` | Test and eval plan |

## Hands-on lab
**Time:** about 3 hours · **You will build:** an approved design and an empty but runnable project skeleton

1. Draw the architecture: GitHub API to files to raw to clean to checks to KPIs to agent to evaluation, with the re-run rule on each arrow.
2. Sketch the DDL for `raw.github_issue` and the watermark table, including the unique key that makes loads idempotent.
3. Write the agent design: tools, knowledge, instructions, guardrails, what it must refuse.
4. List the tests you will write first and draft the 10 evaluation questions.
5. Walk your buddy through it and update the design from their feedback.
6. Create the `capstone/` skeleton: README, folders, and empty test files that pytest can collect.

**Expected output:** Four design documents, a skeleton where `pytest -q` runs (tests may be skipped), and mentor approval before Day 16.

**Break it on purpose:** Ask your buddy to find the single weakest arrow in your diagram. Fix it on paper before writing code.

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** What is the smallest version that still shows every layer?

### Checklist
- [ ] Write the four design documents
- [ ] Buddy design review; update after feedback
- [ ] Create the empty project skeleton (README, folders, empty test files)

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Four filled topic folders that someone else can build from
- [ ] Review comments from your buddy and mentor in REVIEW.md, and your changes
- [ ] Project skeleton committed

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What is the smallest version of this project that still shows every layer?
- What will you cut if you run out of time?

## Suggested tools
- Mermaid / draw.io / Excalidraw
- Markdown ADR (architecture decision record) format
- pytest skeleton

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-15-<topic>` into `main`

## Demo
10-minute design walk-through to a mentor; they approve before you build.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Which use-case kind is this and why?
- [ ] Where could a model's mistake reach a user in your design, and what stops it?
- [ ] What makes your load safe to re-run?

## Done when
Your design is approved and the skeleton is committed.

## Notes for this day
- New day: it bridges the learning weeks and the project weeks. Do not skip it.
