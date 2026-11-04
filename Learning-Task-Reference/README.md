# 4-week learning plan (Adithya) · EnterpriseGPT · AICoE onboarding

Four weeks of learning, done together as a cohort, before you take project tasks. We train you to build **agentic applications**, so the plan goes from fundamentals, to agent basics, to the real application, to a project you design and build yourself. Every exercise is shaped like the real work.

**The goal is to understand, not to finish.** At the end of each day a mentor may ask you to explain what you built, line by line. If you cannot explain a line, it does not count as done, even if it works.

## The four weeks
| Week | Theme | How you learn |
|---|---|---|
| [1: Fundamentals](./week-1-fundamentals/README.md) | Terminal, git, Python, Docker, SQL, JSON, HTTP | Official docs, you type everything, no AI-written code |
| [2: Agent basics](./week-2-agents-basics/README.md) | Model, agent, structured output, tools, knowledge, memory, workflows | One building block a day: understand, build small, break on purpose |
| [3: The application](./week-3-application-and-quality/README.md) | Contracts, raw/clean, semantic layer, KPIs, evals, shipping, capstone design | Trace and measure real code, then design on paper |
| [4: Capstone](./week-4-capstone/README.md) | 'Ask your data': pipeline + agent + evaluation | Build your own project, demo it live |

## How this folder works
```text
<repo root>/
├── README.md            <- you are here (rules + index)
├── TRACKER.md           <- reviewer's high-level progress view
├── week-N-<theme>/
│   ├── README.md            week overview, how it builds, suggested tools
│   └── day-NN-<topic>/
│       ├── README.md        understand first > deep-dive topics > hands-on > expected output > think it through > tools
│       ├── LOG.md           daily log (learned / 3 surprises / 1 question)
│       └── <topic>/         one folder per topic to deep-dive
│           ├── NOTES.md         guide: what to do, where to look in the project, what to produce
│           ├── ACTIVITY_LOG.md  YOU create it: what you did, commands/queries run, output seen, lessons
│           └── (your code, SQL, data, worksheets)
```

**Depth rule:** a topic is not "done" because you read about it. It is done when the topic folder holds your own work and an `ACTIVITY_LOG.md` of things you ran yourself and can explain.

**How to read a day's README:** *Understand first* tells you what you must be able to explain before coding. *What the output should look like* tells you what must exist at the end. The README never gives you the solution; *Think it through yourself* lists the questions you decide on your own and write down.

## Rules
- You own every line you submit. "The AI wrote it" is not an answer.
- **Week 1: no AI-written code.** AI may be used as a tutor ("explain a window function", "what does this error mean"). You type the code. Read the official docs first.
- **Weeks 2 to 4:** AI may help write code, but you must be able to explain and change every line without it.
- Write tests by hand, before or alongside the code. Say in one sentence what each test proves. Tests never call a model.
- Commit after every working step with a message saying what changed. Do not commit `__pycache__/`, `.venv/`, `.env`, keys or real data.
- **Keys stay out of code.** Model keys and passwords go in a local `.env` that git ignores, never in code, commits, prompts or chat.
- Stuck more than 45 minutes? Write down what you tried and ask.
- **Never** commit or paste real company data into exercises, prompts or chat. All data is made up by you, or public (the GitHub issues API). Never send a secret or personal data to a model.

## How your day runs
Follow the same rhythm every day. It keeps you and your buddy in step and makes your progress easy to see.

### 1. Start of day (about 20 minutes)
1. Update your repo: `git switch main && git pull`.
2. Create the day's branch: `git switch -c day-NN-<topic>` (the exact folder name is in the Plan index below).
3. Open the day's `README.md`. Read the **Goal**, **Step 1: Understand first**, **Hands-on lab** and **What the output should look like**. Decide what "finished" means for today before you start.
4. Check your buddy's plan: tell each other in two sentences what you will build today and what you expect to be hard.
5. Join the **cohort stand-up (15 minutes)**: what you did yesterday, what you learned, where you are stuck. Keep it short.

### 2. During the day
- **Understand before you build.** For each topic open its `NOTES.md` and answer *Understand it first* in your `ACTIVITY_LOG.md` before the steps.
- **Work in the day's folder.** Code, SQL, worksheets and your `ACTIVITY_LOG.md` go inside the matching topic folder. Nothing lives anywhere else.
- **Keep the log as you go**, not at the end: what you did, exact commands, what you saw, what failed, what you fixed.
- **Small commits.** Commit after every working step with a message saying what changed.
- **Stuck for more than 45 minutes?** Write down what you tried and ask your buddy, then use the **office hour** (one fixed hour a day when a mentor takes questions from anyone).
- **Keys and data:** model keys only in your local `.env`; never commit it; never paste real company data anywhere.

### 3. End of day (about 30 minutes)
1. Run the lab's *Break it on purpose* step and answer the reflection question in your `ACTIVITY_LOG.md`.
2. Fill `LOG.md`: what you learned, three things that surprised you, one question you still have.
3. **Buddy review:** swap code. Explain your work to your buddy; they ask you about any line. You may explain, but never write your buddy's code.
4. Push your branch and open a Pull Request into `main`. Your buddy reviews first; then the mentor reviews, merges and records the result in `TRACKER.md`.
5. **Explain-back:** a mentor picks two or three people and asks the day's questions out loud. Everyone prepares answers in their own words (nothing to write down).

### A day is finished when
- [ ] The day's **Done when** statement is true
- [ ] Every output listed under **What the output should look like** exists in your folders
- [ ] You can explain every line you wrote without the AI or the docs open
- [ ] `ACTIVITY_LOG.md` and `LOG.md` are filled, and the PR is open

If you cannot tick all four, say so at the next stand-up. An unfinished day is normal; a hidden one is not.

### Week rhythm
- **Monday:** read the week's `README.md` (theme, outcome, days). Agree with your buddy how you will pair on reviews.
- **Mid-week:** if you are more than half a day behind, tell a mentor so the plan can be adjusted early.
- **Friday:** do the week's checkpoint (shown in the week README and in `TRACKER.md`), and read your buddy's logs to see what they learned.

## Git workflow (quick reference)
1. `git switch main && git pull` (main always holds the approved work)
2. `git switch -c day-NN-<topic>` (example: `day-07-your-first-agent`)
3. Do the day's work inside that day's folder; commit small and often
4. Push and open a Pull Request into `main`; your buddy reviews first, then the mentor merges and records the result in `TRACKER.md`
5. Next day starts from the updated `main`

**Follow this structure exactly.** All your work (notes, commands, code, logs) goes inside the matching day and topic folder. Capstone code (weeks 3-4) goes in `capstone/`.

## The project repository (what you learn from)
This learning repo (the one you are in) is where your work lives. The product code you study is a separate repo, **`saturam-agent-framework`**:

```bash
git clone https://github.com/Saturam-Inc/saturam-agent-framework.git ~/saturam-agent-framework
cd ~/saturam-agent-framework      # stay on the `main` branch
```

Every path in the day and topic guides (for example `cookbook/00_quickstart/README.md`) is relative to the root of that clone, on `main`. Never put your learning work inside that clone, and never commit to it. If a path is missing, check you are on `main` and ask.

Top-level map of `saturam-agent-framework`: `libs/agno/egpt/` (framework), `product/egpt_retail/` (application), `frontend/` (React app), `cookbook/` (runnable examples), `deploy/` (Docker, compose, Azure), `scripts/` (setup, format, validate), `docs/` (plans), plus `CLAUDE.md`, `CONTRIBUTING.md`, `ARCHITECTURE.md`.

## EnterpriseGPT in one page
EnterpriseGPT connects to a company's systems, brings their data in, understands what it means, and turns it into KPIs, dashboards, alerts and use cases that act on them. One repository holds all of it:

| Part | Where | What it is |
|---|---|---|
| Framework (egpt) | `libs/agno/egpt/` | Agent framework: agents, teams, workflows, tools, models, knowledge (RAG), memory, storage. Knows nothing about any one industry. |
| Application | `product/egpt_retail/` | Contracts, warehouse, semantic layer, KPIs, skills, dashboards, alerts, use cases, API. |
| Web app | `frontend/` | The React interface. |
| Examples | `cookbook/` | Runnable examples for every pattern. Your main learning material in week 2. |

| Layer | Holds | Example |
|---|---|---|
| Raw files | Exactly what the source sent, one file per pull, never changed | `raw/crm/deal/dt=2026-09-01/deal-20260901T020000Z.ndjson` |
| Raw table | Each line of each file as one row in Postgres (JSON), every version kept | one row per deal version |
| Clean | One tidy row per real thing: de-duplicated, typed | one row per deal, latest version |
| Semantic layer | What the data means: entities, keys, joins, business terms, as a knowledge graph | "a deal belongs to one customer; won means stage Closed Won" |
| KPI values | Numbers per date, from SQL formulas a person accepted; **no AI model computes them** | win rate for September |
| Dashboards, alerts, use cases | What people see and act on | an alert when win rate drops |

Use cases come in three kinds: **analytics automation** (watch the data, explain a change, alert someone), **process automation** (carry out routine steps across systems, with a person approving) and **decision intelligence** (weigh options, recommend a decision, measure whether it worked).

**The core problem:** a source sends the same thing many times (a deal changed 3 times arrives 3 times; a quote with 5 products arrives as 5 rows). Counting rows gives the wrong answer. Turning "many rows" into "one row per real thing, latest version" is the core skill. Days 4, 11 and 18 are built around it.

## Plan index
Start each week with its overview: [Week 1](./week-1-fundamentals/README.md) · [Week 2](./week-2-agents-basics/README.md) · [Week 3](./week-3-application-and-quality/README.md) · [Week 4](./week-4-capstone/README.md) · [Tracker](./TRACKER.md)

- Day 01: [Setup, terminal, git and Python](./week-1-fundamentals/day-01-setup-terminal-git-python/README.md)
- Day 02: [Servers, processes, ports and Docker](./week-1-fundamentals/day-02-servers-processes-ports-docker/README.md)
- Day 03: [PostgreSQL basics](./week-1-fundamentals/day-03-postgresql-basics/README.md)
- Day 04: [JSON in Postgres and 'latest row per key'](./week-1-fundamentals/day-04-json-and-latest-row-per-key/README.md)
- Day 05: [HTTP and APIs](./week-1-fundamentals/day-05-http-and-apis/README.md)
- Day 06: [How agents work, and how EnterpriseGPT is built](./week-2-agents-basics/day-06-how-enterprisegpt-is-built/README.md)
- Day 07: [Your first agent](./week-2-agents-basics/day-07-your-first-agent/README.md)
- Day 08: [Tools: letting the agent act](./week-2-agents-basics/day-08-tools-letting-the-agent-act/README.md)
- Day 09: [Knowledge and memory](./week-2-agents-basics/day-09-knowledge-and-memory/README.md)
- Day 10: [Teams, workflows and a person in the loop](./week-2-agents-basics/day-10-teams-workflows-human-in-loop/README.md)
- Day 11: [Data in: contracts, raw and clean](./week-3-application-and-quality/day-11-data-in-contracts-raw-clean/README.md)
- Day 12: [Meaning: the semantic layer and KPIs](./week-3-application-and-quality/day-12-meaning-semantic-layer-kpis/README.md)
- Day 13: [Evaluating agents](./week-3-application-and-quality/day-13-evaluating-agents/README.md)
- Day 14: [How we ship, and where it runs](./week-3-application-and-quality/day-14-how-we-ship-and-where-it-runs/README.md)
- Day 15: [Capstone design: plan before you build](./week-3-application-and-quality/day-15-capstone-design/README.md)
- Day 16: [Capstone 1: pull and land files](./week-4-capstone/day-16-capstone-pull-and-land/README.md)
- Day 17: [Capstone 2: raw table and clean view](./week-4-capstone/day-17-capstone-raw-and-clean/README.md)
- Day 18: [Capstone 3: checks and KPIs](./week-4-capstone/day-18-capstone-checks-and-kpis/README.md)
- Day 19: [Capstone 4: the agent and its evaluation](./week-4-capstone/day-19-capstone-agent-and-evaluation/README.md)
- Day 20: [Capstone 5: package and final demo](./week-4-capstone/day-20-capstone-final-demo/README.md)

## Reference reading
| Topic | Where |
|---|---|
| git | Pro Git book, git-scm.com/book (ch. 2, 3) |
| Python envs, pytest | docs.python.org tutorial (virtual environments); docs.pytest.org "Get started" |
| Docker, compose | docs.docker.com "Get started" |
| PostgreSQL | postgresql.org/docs: Tutorial (ch. 2, 3), JSON functions, window functions |
| HTTP APIs | docs.github.com/rest: pagination, rate limits |
| Language models | The prompt engineering guide of the model provider you are given |
| Pydantic | docs.pydantic.dev "Models" |
| Agents in our framework | cookbook/00_quickstart, 02_agents, 04_workflows, 07_knowledge, 09_evals, 11_memory |
| Neo4j | neo4j.com/docs "Getting started with Cypher" |
| Azure | Microsoft Learn: Azure Fundamentals; deploy/AZURE_CUTOVER.md |
| Our system | CLAUDE.md; CONTRIBUTING.md; ARCHITECTURE.md; LANDING_CONTRACT.md; LOAD_CONTRACT.md; docs/plan/domain-knowledge-layers.md; cookbook/94_retail/README.md |

## What "ready" means at the end of week 4
- Set up the project, run its services and tests, and find your way around the code without help
- Write and explain SQL for filtering, joining, grouping and "latest row per key", including on JSON
- Explain how EnterpriseGPT works: what the framework does, what the application adds, how data moves from a source to a KPI, and where a model runs and where it never does
- Build an agent with our framework (model, instructions, tools, structured output, knowledge) and measure how well it answers
- Built a small working pipeline and agent end to end, with tests and an evaluation, and can explain every part

---

## Questions or doubts?
If anything in this plan is unclear, or you are stuck, **connect with your Team Lead**. Do not wait more than 45 minutes on a blocker; ask your buddy first, then your Team Lead or the daily office hour.

*This learning plan was created by **Vinoth**.*
