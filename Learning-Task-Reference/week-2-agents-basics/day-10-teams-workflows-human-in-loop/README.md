# Day 10: Teams, workflows and a person in the loop

*Week 2: building agents with the framework (basics first)*

**Goal:** Choose between a single agent, a team and a workflow, and add human approval.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Single agent vs team vs workflow, each as a flow: one loop; a leader agent delegating to members; fixed steps run in order
- Start with a single agent; scale up only when needed (cost, steps, control)
- Workflow = predictable and testable; team = flexible and costly
- Human-in-the-loop: where approval sits in the flow and what a rejection does
- Why creating an agent inside a loop is a problem (cost, state, performance)

## Read
- cookbook/00_quickstart/multi_agent_team.py, sequential_workflow.py, human_in_the_loop.py
- cookbook/04_workflows/01_basic_workflows/

## Where to look in the project
- `cookbook/00_quickstart/multi_agent_team.py` — a team
- `cookbook/00_quickstart/sequential_workflow.py` — a sequential workflow
- `cookbook/00_quickstart/human_in_the_loop.py` — confirmation before a tool runs
- `cookbook/04_workflows/01_basic_workflows/README.md` — workflow learning path
- `cookbook/02_agents/11_approvals` — approvals pattern
- `libs/agno/egpt/approval/decorator.py` — how approval is attached to a tool
- `libs/agno/egpt/workflow/` — workflow engine

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `patterns/` | Agent, team, workflow |
| `weekly-note-workflow/` | Practice: two-step workflow |
| `approval/` | Human approval |
| `team-comparison/` | Same question through a team |

## Hands-on lab
**Time:** about 3 hours · **You will build:** a two-step workflow with a human approval gate, compared with a team

1. Run `multi_agent_team.py`, `sequential_workflow.py` and `human_in_the_loop.py`; sketch each as a flow.
2. Build a workflow: step 1 your agent answers a question, step 2 a writer agent turns it into a short weekly note.
3. Add an approval gate: the note is saved to a file only after a person approves.
4. Run it twice: approve once, reject once.
5. Run the same question through a team. Measure tokens, steps and time for both.

**Expected output:** Approve: file saved. Reject: no file and a logged reason. A measured comparison table.

**Break it on purpose:** Create the writer agent inside a loop over 5 questions, then create it once outside and reuse it. Compare cost and behaviour.

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Why is the workflow easier to test than the team?

### Checklist
- [ ] Run three quickstart examples
- [ ] Build the workflow with approval
- [ ] Run the same question via a team
- [ ] Fill the comparison table

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Approve run: file saved. Reject run: no file, reason logged (both in RUN_OUTPUT.md)
- [ ] team-comparison/NOTES.md with a measured table (tokens, steps, time)
- [ ] Tests for the approval branch pass without a key

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- Which part of your workflow would you make deterministic code instead of an agent?
- What if the approver is unavailable?

## Suggested tools
- Debug output / token counters
- `time` or Python `perf_counter` for timing
- Mermaid for step diagrams

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-10-<topic>` into `main`

## Demo
Run the workflow, approve once and reject once.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Why is a workflow easier to test than a team?
- [ ] Where did you put the approval, and what happens when it is rejected?
- [ ] Why is creating an agent inside a loop a problem?

## Done when
The workflow runs, approval works both ways, and you can explain the trade-off with a team.

## Notes for this day
- End of week 2 check: 20-minute explain-back of your day 8-10 code chosen by the reviewer, plus a short quiz on tools, retrieval and memory.
