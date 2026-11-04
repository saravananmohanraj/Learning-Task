# Day 06: How agents work, and how EnterpriseGPT is built

*Week 2: building agents with the framework (basics first)*

**Goal:** Understand what a language model is, what an agent is, and how the agent loop works, by building a tiny agent yourself with no framework. Then learn the repository.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- What a language model does: predicts the next token from all tokens so far; no memory between calls; no access to your systems
- Tokens, context window, system and user messages, temperature, cost per token, why the same prompt gives different answers, hallucination
- What a prompt really is: the whole message list you send, not just the last question
- What an agent is, and how it differs from a chatbot and from a workflow
- The agent loop: build messages > model decides (answer or tool call) > code runs the tool > result goes back > repeat > final answer
- The parts of an agent: model, instructions, tools, knowledge, memory/storage, output schema, guardrails
- Framework (egpt) vs application (product/egpt_retail), and where a model runs or must never run

## Read
- The prompt engineering and tool-use guides of the model provider you are given
- CLAUDE.md, CONTRIBUTING.md, ARCHITECTURE.md (repository root)

## Where to look in the project
- `README.md` — what the repo is
- `CLAUDE.md` — sections 'Repository Structure', 'Code Locations', 'Coding Patterns', 'Don't'
- `CONTRIBUTING.md` — contribution rules
- `ARCHITECTURE.md` — sections 'Layer Diagram', 'Layer Responsibilities', 'Data Flow', 'Code Layout', 'Dependency Rules'
- `docs/plan/domain-knowledge-layers.md` — how meaning is added on top of data
- `docs/plan/build-plan.md` — how the work is planned
- `libs/agno/egpt/` — the framework: browse agent/, models/, tools/, knowledge/, memory/, workflow/, team/, eval/
- `product/egpt_retail/` — the application: browse contracts/, warehouse/, semantic/, kpi/, usecases/, api/
- `frontend/` — the React web app
- `cookbook/` — runnable examples
- `deploy/` — how it runs
- `scripts/` — helper scripts (setup, format, validate, run)

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `llm-basics/` | Language model basics |
| `prompting/` | Prompts and instructions |
| `agent-concept/` | What an agent is, and how the loop works |
| `agent-from-scratch/` | Practice: an agent with no framework |
| `repo-map/` | Repository map |

## Hands-on lab
**Time:** about 2.5 hours · **You will build:** a working agent loop of under 60 lines with no framework

1. Send one prompt to the model with the provider SDK; print the reply and the token usage.
2. Define a fake tool `get_deal_stage(deal_id)` that reads from a small dict of made-up deals.
3. Describe the tool to the model using the provider's tool-calling feature.
4. Write the loop: call the model; if it asks for the tool, run it, append the result as a message and call the model again; stop on a final answer or after 5 iterations.
5. Print every message so you can see the whole conversation.
6. Write a test with a fake model (a function returning a canned tool request, then a canned answer). It must run with no network and no key.

**Expected output:** A transcript like: user question > assistant asks for get_deal_stage(D-1001) > tool result > assistant final answer. `pytest` passes with the key unset.

**Break it on purpose:** Ask about a deal that is not in the dict, then set max iterations to 1. What does the model do each time, and why?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** What did the model see on its second call that it did not see on its first?

### Checklist
- [ ] Run the token, temperature and unknown-fact experiments
- [ ] Write and compare the 3 prompt versions
- [ ] Draw and label the agent loop
- [ ] Build the framework-free agent with a fake tool, an iteration guard and a fake-model test
- [ ] Write the repo map

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] llm-basics/ACTIVITY_LOG.md: a table of token counts, costs, and temperature results, plus your conclusion
- [ ] prompting/ACTIVITY_LOG.md: 3 prompts, 3 outputs, and what made the difference
- [ ] agent-concept/ diagram labelled with real Agent field names, and the 5 failure modes with defences
- [ ] agent-from-scratch/: loop code, a printed transcript showing user > tool call > tool result > final answer, and a passing test that never calls the model
- [ ] repo-map/ACTIVITY_LOG.md: one sentence per folder, in your own words

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What exactly does the model 'see' on the second call of the loop that it did not see on the first?
- Why can the model never run a tool itself?
- If a tool returns an error message, what should the loop do?

## Suggested tools
- Provider SDK (Python) and its token counter
- python-dotenv for the key in .env
- Mermaid, draw.io or Excalidraw for the loop diagram
- pytest
- git grep to explore the repo

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-06-<topic>` into `main`

## Demo
10 minutes: show your loop diagram, the transcript of your framework-free agent, and your repo map.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What is a token, and why does a long conversation cost more?
- [ ] What is the difference between a chatbot, a workflow and an agent?
- [ ] Walk through the agent loop: who decides to call a tool, who runs it, and what does the model see afterwards?
- [ ] Why must a KPI number never come from a model's answer?

## Done when
You can explain the agent loop without notes, your framework-free agent works and is tested, and you can find your way around the repository.

## Notes for this day
- From this week AI may help write code, but you must explain every line.
- This week you need a model key from your mentor. Put it in a local `.env` that git ignores. Never in code, commits, prompts or chat.
