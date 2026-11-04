# Day 19: Capstone 4: the agent and its evaluation

*Week 4: project-level capstone, 'Ask your data'*

**Goal:** Add an agent that answers questions about your data using only tool-derived numbers, and measure it.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Agent suggests and explains; SQL computes
- Every number must come from the tool
- Knowledge holds KPI definitions; instructions hold behaviour rules

## Read
- Your day 8, 9 and 13 notes

## Where to look in the project
- `libs/agno/egpt/guardrails/sql_guard.py` — compare with the guard you wrote on day 8
- `cookbook/09_evals/accuracy/accuracy_with_tools.py` — eval pattern for tool-using agents
- `cookbook/07_knowledge/01_getting_started/02_agentic_rag.py` — loading definitions as knowledge

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `sql-tool/` | Read-only SQL tool over clean |
| `kpi-knowledge/` | KPI definitions as knowledge |
| `agent/` | The agent |
| `evaluation/` | Evaluation |

## Hands-on lab
**Time:** about 3.5 hours · **You will build:** an agent whose every number comes from its guarded SQL tool, plus its evaluation

1. Reuse your day-8 read-only role and guard, now over `clean.issue`.
2. Write KPI definitions (closed, median days, week boundaries) and load them as knowledge.
3. Build the agent: typed answers that include the SQL used; it refuses questions outside the data.
4. Ask five questions live, including 'how many issues closed last week, and is that above the 8-week median?'.
5. Run your 10-question evaluation, analyse failures, improve once, re-run.

**Expected output:** Every number matches your KPI SQL; one visible refusal; a score before and after.

**Break it on purpose:** Ask a question the data cannot answer. Does the agent refuse or invent a number?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Show one question the agent got wrong and explain why.

### Checklist
- [ ] Wire the tool and knowledge
- [ ] Build and test the agent
- [ ] Run the eval and iterate

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Every number in an answer matches your KPI SQL (checked)
- [ ] evaluation/RESULTS.md: score, failure causes, before/after
- [ ] At least one refusal example (question outside the data)

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- Show one question the agent got wrong and explain why
- How would you detect that the agent made up a number?

## Suggested tools
- egpt framework agent, tools and evals
- Pydantic output schema
- pytest for guard and parsing tests

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-19-<topic>` into `main`

## Demo
Ask five questions live, then show the eval score.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] How do you guarantee a number came from the tool?
- [ ] Show one question the agent got wrong and why.
- [ ] What stops the agent from running a write?

## Done when
Agent numbers come from the tool and the eval score is reported and explained.
