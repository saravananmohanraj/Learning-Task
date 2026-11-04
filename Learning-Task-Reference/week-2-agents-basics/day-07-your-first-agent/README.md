# Day 07: Your first agent

*Week 2: building agents with the framework (basics first)*

**Goal:** Use the framework to build an agent with a typed (structured) output, and connect what you built by hand on day 6 to what the framework does.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Which parts of the day-6 loop the framework now does for you (building messages, calling the model, parsing the reply)
- Structured output: why free text is hard to use in software, and how a schema turns a reply into a validated object
- Pydantic models: fields, types, validation errors
- What the framework sends to the model when you set output_schema, and what happens if the reply does not match
- Why tests never call the model (cost, speed, non-determinism)

## Read
- cookbook/00_quickstart/README.md and cookbook/02_agents/README.md
- docs.pydantic.dev 'Models'

## Where to look in the project
- `cookbook/00_quickstart/README.md` — setup steps (uv venv .venvs/quickstart --python 3.12; uv pip install -r cookbook/00_quickstart/requirements.txt)
- `cookbook/00_quickstart/agent_with_structured_output.py` — typed output example
- `cookbook/00_quickstart/agent_with_typed_input_output.py` — typed input and output example
- `cookbook/02_agents/02_input_output` — more input/output patterns
- `cookbook/90_models` — how to switch to another model provider
- `libs/agno/egpt/agent/agent.py` — the Agent class: read its constructor arguments

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `pydantic/` | Pydantic models |
| `structured-output/` | Structured output |
| `quickstart-runs/` | Quickstart agents |
| `debug-trace/` | Reading a run trace and tracing the code |
| `deal-summary-agent/` | Practice: deal summary agent |

## Hands-on lab
**Time:** about 2.5 hours · **You will build:** a typed deal-summary agent, after comparing three ways of getting structured output

1. Define a Pydantic `DealSummary` (deal id, latest stage, value, one-line note) and print its JSON schema.
2. With the provider SDK ask about one made-up deal three ways: free text; 'reply with JSON only'; with the schema. Parse each in code and note which breaks first.
3. Run `cookbook/00_quickstart/agent_with_structured_output.py` with debug output on. Annotate one full trace by hand.
4. Build your own agent with `output_schema=DealSummary`, fed one of your day-4 deals as JSON. Run it on three deals.
5. Test parsing and validation with a fixed canned reply. No model call in the test.

**Expected output:** Three valid `DealSummary` objects, an annotated trace, and passing tests with the key unset.

**Break it on purpose:** Add a required field that is not in your data (for example `customer_region`). What does the framework report?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Which parts of your day-6 loop did the framework do for you here?

### Checklist
- [ ] Build and break a Pydantic model
- [ ] Compare free text vs JSON vs schema output
- [ ] Run both quickstart examples
- [ ] Annotate one debug trace and map it to the code
- [ ] Build the deal summary agent on 3 deals with tests

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] pydantic/: the model, 3 captured ValidationErrors, and the JSON schema
- [ ] structured-output/ACTIVITY_LOG.md: free vs JSON vs schema comparison and the failure you caused
- [ ] debug-trace/: an annotated trace and the code path (file + function + one line each)
- [ ] deal-summary-agent/: valid typed output for 3 deals, tests passing with the key unset
- [ ] ACTIVITY_LOG.md in each topic names the commands and env variables used (never the key itself)

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What would you change in the instructions if the model kept inventing a stage name that is not in your data?
- How would you test the invalid-reply path without calling the model?
- Which part of the trace costs the most tokens, and why?

## Suggested tools
- python-dotenv (load .env)
- pydantic
- pytest
- jq to pretty-print JSON
- `git secrets`/gitleaks or `git diff --cached` check before every commit

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-07-<topic>` into `main`

## Demo
Run your agent on three deals and walk through one debug trace.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does output_schema change in what the model is asked to do? What happens if the model returns something invalid?
- [ ] Where does your key come from at run time? Why not in the code?
- [ ] Why should tests not call the model?

## Done when
Your agent and tests are your own and you can explain the trace.

## Notes for this day
- Check `.env` is in `.gitignore` before the first commit of the day.
