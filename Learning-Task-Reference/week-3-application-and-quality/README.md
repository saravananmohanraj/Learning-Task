# Week 3: the EnterpriseGPT application, quality and capstone design

**Rule this week:** AI may help write code, but you must explain every line. Pair only to review each other's code.

**Theme:** from single agents to a real application. You learn how data gets in and gets meaning, how agents are measured, how the team ships, and then you design your own project on paper before building it.

**Outcome:** you can trace a record from file to clean table, explain the semantic layer and why KPIs are SQL, evaluate an agent with a real score, open and review a PR, and hold an approved design for the week-4 capstone.

## How the week builds
| Day | Topic | Builds on |
|---|---|---|
| [11](./day-11-data-in-contracts-raw-clean/README.md) | Data in: contracts, raw, clean | Day 4 (latest per key) |
| [12](./day-12-meaning-semantic-layer-kpis/README.md) | Semantic layer and KPIs | Day 11 |
| [13](./day-13-evaluating-agents/README.md) | Evaluating agents | Day 8-9 agent |
| [14](./day-14-how-we-ship-and-where-it-runs/README.md) | Shipping, review, deploy | Whole repo |
| [15](./day-15-capstone-design/README.md) | Capstone design | Everything so far |

## Working pattern
Understand the concept, then **trace** or **measure** something real, then explain it. Days 11-12 are about reading and tracing existing code; day 13-14 are about proof and process; day 15 is about planning.

## Suggested tools for the week
| Need | Tool |
|---|---|
| Graph | Neo4j Browser, Docker |
| Database | `psql`, DBeaver |
| Evaluation | framework evals (cookbook/09_evals), pytest |
| Quality gates | repo scripts `format.sh` / `validate.sh`, ruff, pre-commit (optional) |
| PRs | `gh` CLI, the PR template |
| Design | Mermaid, draw.io, Excalidraw, ADR notes |

## End-of-week check
20-minute explain-back on days 11 to 14 plus a short quiz on the semantic layer, evals and shipping. Day 15's design must be approved by a mentor before week 4 starts.
