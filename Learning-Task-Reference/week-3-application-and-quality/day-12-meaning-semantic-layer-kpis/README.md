# Day 12: Meaning: the semantic layer and KPIs

*Week 3: the EnterpriseGPT application, quality and capstone design*

**Goal:** Understand how the system knows what data means, and why KPIs are SQL formulas, not model answers.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Ontology and knowledge graph: entities, attributes, relationships
- Semantic layer = what the clean tables do not say (keys, joins, business terms)
- KPI = SQL formula a person accepted; agents suggest, never compute
- Feasibility of a KPI: which entities and fields it needs

## Read
- docs/plan/domain-knowledge-layers.md
- cookbook/94_retail/README.md
- neo4j.com/docs 'Getting started with Cypher'

## Where to look in the project
- `docs/plan/domain-knowledge-layers.md` — the layers of meaning
- `cookbook/94_retail/README.md` — table of every retail script and what it needs
- `cookbook/94_retail/K03_ontology.py` — ontology (needs Neo4j)
- `cookbook/94_retail/K04_metadata_harvest.py` — harvest column metadata from the warehouse
- `cookbook/94_retail/K05_semantic_graph.py` — write that harvest into the graph
- `cookbook/94_retail/K11_kpi_registry_and_feasibility.py` — KPI registry and feasibility
- `cookbook/94_retail/K11_kpi_formula_shape.py` — shapes of real KPI formulas
- `scripts/demo_setup.sh` — creates .venvs/demo that these scripts use
- `product/egpt_retail/ontology/` — ontology code
- `product/egpt_retail/semantic/` — semantic layer code
- `product/egpt_retail/kpi/` — KPI code
- `deploy/compose.yaml` — the 'neo4j' service (browser on 7474, bolt on 7687)

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `cypher-basics/` | Neo4j and Cypher |
| `run-semantic-examples/` | Run the K-examples |
| `graph-queries/` | Your three Cypher queries on K05's graph |
| `kpi-analysis/` | One KPI analysed |

## Hands-on lab
**Time:** about 3 hours · **You will build:** Cypher queries over the real semantic graph and a feasibility change you caused

1. Learn the basics of Cypher on Neo4j's sample graph (10 queries).
2. Set up with `./scripts/demo_setup.sh`, then run K03, K04, K05 and K11 as their headers describe.
3. In the Neo4j browser (port 7474) write three queries: list the entities; show the attributes of one; show how two entities join.
4. For one KPI from K11, write its formula, entities and why it is feasible or not.

**Expected output:** Three saved queries with results, and a KPI note naming its entities and feasibility.

**Break it on purpose:** Follow K11's idea: remove a table the KPI needs and watch one KPI become blocked while another goes partial.

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** Why can an agent suggest a KPI but never compute it?

### Checklist
- [ ] Learn Cypher on a sample graph
- [ ] Run K03, K04, K05, K11
- [ ] Write the three queries
- [ ] Analyse one KPI

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] graph-queries/QUERIES.cypher with each query and a screenshot/result
- [ ] kpi-analysis/NOTES.md: formula, entities, feasibility reasoning
- [ ] A written path: clean table > semantic layer > KPI > dashboard (5 lines, own words)

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What does the graph know that SQL tables alone do not?
- What makes a KPI not feasible, and who decides?

## Suggested tools
- Neo4j Browser
- Docker for Neo4j
- cypher-shell (optional)

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-12-<topic>` into `main`

## Demo
Show your three queries and explain your KPI.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does the semantic layer know that the clean tables do not?
- [ ] What makes a KPI 'not feasible'?
- [ ] Why does an agent suggest KPIs but never compute them?

## Done when
You can explain the path from a clean table to a KPI on a dashboard.
