# Day 13: Evaluating agents

*Week 3: the EnterpriseGPT application, quality and capstone design*

**Goal:** Measure how well an agent answers, and learn to read failures.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Three kinds of eval: accuracy against expected answers, agent-as-judge, reliability (right tool called)
- Why a score alone is not enough: failure analysis
- Why a judge agent needs its own checks

## Read
- cookbook/09_evals/README.md
- accuracy/accuracy_with_given_answer.py and accuracy/accuracy_with_tools.py

## Where to look in the project
- `cookbook/09_evals/README.md` — map of the eval types
- `cookbook/09_evals/accuracy/accuracy_with_given_answer.py` — accuracy eval with expected answers
- `cookbook/09_evals/accuracy/accuracy_with_tools.py` — accuracy eval for an agent that uses tools
- `cookbook/09_evals/agent_as_judge` — an agent scoring another agent
- `cookbook/09_evals/reliability` — did it call the right tool
- `libs/agno/egpt/eval/accuracy.py` — how accuracy scoring is implemented
- `libs/agno/egpt/eval/agent_as_judge.py` — how judging is implemented

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `eval-examples/` | Run the example evals |
| `eval-set/` | Your evaluation set |
| `run-and-record/` | Run and record |
| `judge-checks/` | Judge reliability |

## Hands-on lab
**Time:** about 3 hours · **You will build:** a scored evaluation of your own agent with a failure analysis

1. Run the two accuracy examples in `cookbook/09_evals/accuracy/`; read how the score is computed.
2. Write 10 questions over your deals data. Compute every expected answer with your own SQL, and include at least two trap questions (counting rows, NULLs).
3. Run the evaluation against your day-8/9 agent and record the score.
4. Write a failure table: question, agent answer, expected, cause.
5. Fix one cause and re-run.

**Expected output:** A score before and after, and a cause for every failure.

**Break it on purpose:** Make one expected answer wrong on purpose. Does your evaluation notice?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Your eval scored 7 out of 10: what do you look at first?

### Checklist
- [ ] Run example evals
- [ ] Write 10 Q&A with SQL-derived answers
- [ ] Run, analyse failures, fix, re-run

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] eval-set/questions.json (or similar) + the SQL that produced each expected answer
- [ ] run-and-record/RESULTS.md: score table, per-failure cause, before/after
- [ ] judge-checks/NOTES.md

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- Your eval scored 7/10: what do you look at first?
- Is a 10/10 score proof the agent is good?

## Suggested tools
- Framework evals (cookbook/09_evals)
- pytest to run evals in CI later
- CSV/JSON for the question set

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-13-<topic>` into `main`

## Demo
Show the eval results and walk through two failures.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Your eval scored 7 out of 10. What do you look at first?
- [ ] Why does an agent acting as judge need its own checks?
- [ ] How do you know your expected answers are right?

## Done when
Your eval runs and you can explain each failure.

## Notes for this day
- Plan change: the original day 13 combined evals and shipping; they are now days 13 and 14.
