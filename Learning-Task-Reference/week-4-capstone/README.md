# Week 4: project-level capstone, 'Ask your data'

**Rule this week:** work alone; pair only to review each other's code. AI may help write code, but you must explain and change every line without it. Everything is made up or public (the GitHub issues API). No real company data, ever.

**Theme:** build one small project that has every layer of EnterpriseGPT, from the design you approved on day 15. Follow your own design; changes go into the design doc first.

**Outcome:** a working pipeline and agent, with tests and an evaluation, that someone else can run from your README, plus a live 30-minute demo.

## The project, in one line
Pull GitHub issues incrementally > NDJSON files > `raw.github_issue` > `clean.issue` > SQL checks > KPIs (issues closed per week, median days to close) > an agent that answers questions using only tool-derived numbers > an evaluation score.

## How the week builds
| Day | Stage | Builds on |
|---|---|---|
| [16](./day-16-capstone-pull-and-land/README.md) | Pull and land files, watermark | Day 5, Day 15 design |
| [17](./day-17-capstone-raw-and-clean/README.md) | Raw table, clean view | Day 4, Day 16 files |
| [18](./day-18-capstone-checks-and-kpis/README.md) | Checks, KPIs in SQL | Day 17 clean |
| [19](./day-19-capstone-agent-and-evaluation/README.md) | Agent and evaluation | Day 8, 9, 13, 18 |
| [20](./day-20-capstone-final-demo/README.md) | Package and demo | All |

## Working pattern
- Test first or alongside; each test has a one-line statement of what it proves.
- Run the stage twice before moving on (re-run safety).
- Make failures happen on purpose, and show them.
- Keep the project in `capstone/` with its own README and TEST_LOG in the cookbook style.

## Suggested tools for the week
| Need | Tool |
|---|---|
| HTTP | httpx or requests, with hand-made fakes in tests |
| Storage | local folder or Azurite |
| Database | Postgres, `psql`, DBeaver, SQLAlchemy/psycopg |
| Agent | the egpt framework: agent, tools, knowledge, evals |
| Tests | pytest, parametrize |
| Docs | Mermaid in README; `asciinema` for a backup demo recording |

## Final checkpoint
30-minute live demo: pull > files > raw > clean > checks > KPIs > agent > evaluation, then questions on any line. The mentor panel signs off in `TRACKER.md`.
