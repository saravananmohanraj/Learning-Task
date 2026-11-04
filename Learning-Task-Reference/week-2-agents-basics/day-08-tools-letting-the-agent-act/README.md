# Day 08: Tools: letting the agent act

*Week 2: building agents with the framework (basics first)*

**Goal:** Give an agent a safe tool, and learn to debug a wrong answer through its tool calls.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Why a model cannot run code: it only returns text, and a tool call is a structured request in that text
- The tool-calling loop in the framework: tools are turned into schemas the model sees; the model asks for a tool; the framework validates and runs it; the result is appended as a message; the model is called again
- What the model sees about a tool: its name, description (docstring) and typed arguments, nothing else
- The @tool decorator and Toolkit in libs/agno/egpt/tools/
- Safety: a tool can do anything your code can; defence in depth (read-only DB user AND a code guard AND row caps)
- Grounding: why the agent needs the table description and the 'latest version per deal' rule to count correctly

## Read
- cookbook/00_quickstart/agent_with_tools.py
- cookbook/02_agents/04_tools/

## Where to look in the project
- `cookbook/00_quickstart/agent_with_tools.py` — a tool-using agent
- `cookbook/02_agents/04_tools` — more tool patterns
- `libs/agno/egpt/tools/decorator.py` — the @tool decorator
- `libs/agno/egpt/tools/toolkit.py` — Toolkit: grouping tools
- `libs/agno/egpt/guardrails/sql_guard.py` — the framework's own SQL guard: read it only AFTER you wrote yours, then compare
- `cookbook/94_retail/R06_sql_guard_parsing.py` — how the team tests SQL guard parsing
- `product/egpt_retail/warehouse/sql/ddl/065_readonly_role.sql` — how the project creates a read-only database role

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `tool-calling/` | Tool calling |
| `readonly-db-user/` | Read-only database user |
| `sql-guard/` | SQL guard |
| `run-sql-agent/` | Practice: run_sql agent |

## Hands-on lab
**Time:** about 3 hours · **You will build:** an agent that answers from your deals table through a guarded read-only SQL tool

1. Create a Postgres role that can only SELECT on your tables. Try an INSERT as that role and capture the refusal.
2. Write `run_sql(query)`: exactly one SELECT, row cap, timeout. Write tests for a DELETE, two statements in one string, a comment trick, and an allowed SELECT.
3. Build an agent whose instructions describe `raw_deals`. Give it the tool.
4. Ask: how many deals are Closed Won? What is the total value of open deals?
5. Compare the SQL it wrote with your day-4 answers. Change the instructions until it stops counting rows.

**Expected output:** Both numbers equal your day-4 results; the guard refuses all three attacks; the trace shows the SQL the agent ran.

**Break it on purpose:** Delete the 'latest version per deal' rule from the instructions. How does the answer change, and why?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** The agent gave a wrong number: which three places do you check, in order?

### Checklist
- [ ] Trace the quickstart tool run
- [ ] Create the read-only role
- [ ] Write run_sql with the guard and its tests
- [ ] Build the agent, ask the two questions, iterate on instructions

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] Both questions answered with numbers equal to your day-4 SQL
- [ ] Guard tests pass; a write attempt is refused (screenshot or log)
- [ ] run-sql-agent/ITERATIONS.md: each instruction change and whether the answer improved
- [ ] A trace in which you can point to the SQL the agent generated
- [ ] tool-calling/ACTIVITY_LOG.md: the generated tool schema, the good vs bad docstring result, and the code path you found

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- The agent gave a wrong number: what are the three places you look first, in what order?
- What could still go wrong even with a guard and a read-only user?

## Suggested tools
- psql / pgcli / DBeaver to compare queries
- sqlparse (optional) for parsing the statement in the guard
- pytest parametrize for guard cases

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-08-<topic>` into `main`

## Demo
Show the tool calls in the trace, the right answer, and the guard refusing a write.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] Walk through one tool call: who decides to call it, who runs it, and what the model sees.
- [ ] Why a read-only database user as well as your guard?
- [ ] The agent gave a wrong number. How do you find out why?

## Done when
The agent answers both questions correctly from the tool, and the guard tests pass.

## Notes for this day
- Never point this agent at real data. Use only your made-up deals.
