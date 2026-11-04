# Day 09: Knowledge and memory

*Week 2: building agents with the framework (basics first)*

**Goal:** Understand retrieval (RAG), knowledge vs memory vs session history, and make an agent use a business glossary.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- What an embedding is: a list of numbers that places a text in 'meaning space'; similar meaning means close vectors
- Similarity: cosine similarity / distance, and what pgvector does with it
- The RAG flow: load documents > chunk > embed > store > embed the question > find nearest chunks > put them in the prompt > answer
- Why retrieval beats pasting everything into the prompt (cost, context limit, focus) and when it fails (bad chunks, missing info)
- Knowledge vs memory vs session history: what each remembers, for how long, for whom
- Where a fact belongs: knowledge, memory, or instructions

## Read
- cookbook/07_knowledge/01_getting_started/ (01_basic_rag.py, 02_agentic_rag.py)
- cookbook/00_quickstart/agent_with_memory.py and agent_with_storage.py
- cookbook/11_memory/01_agent_with_memory.py

## Where to look in the project
- `cookbook/07_knowledge/01_getting_started/README.md` — the RAG learning path
- `cookbook/07_knowledge/01_getting_started/01_basic_rag.py` — basic retrieval
- `cookbook/07_knowledge/01_getting_started/02_agentic_rag.py` — agent decides when to retrieve
- `cookbook/00_quickstart/agent_search_over_knowledge.py` — knowledge + agent in the quickstart
- `cookbook/00_quickstart/agent_with_storage.py` — conversation persistence
- `cookbook/00_quickstart/agent_with_memory.py` — user memory
- `cookbook/11_memory/01_agent_with_memory.py` — memory in depth
- `libs/agno/egpt/vectordb/pgvector/pgvector.py` — the pgvector store used by the examples
- `cookbook/scripts/run_pgvector.sh` — the Postgres these examples need

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `embeddings-by-hand/` | Embeddings and similarity, by hand |
| `rag-basics/` | RAG basics |
| `glossary-knowledge/` | Practice: business glossary |
| `memory-storage/` | Memory and storage |
| `bad-glossary/` | Catching a wrong glossary |

## Hands-on lab
**Time:** about 3 hours · **You will build:** a glossary-aware agent whose conversation survives a restart

1. Embed 6 short sentences (3 about deals, 3 unrelated) and compute cosine similarity to a question yourself.
2. Run `01_basic_rag.py` and `02_agentic_rag.py` against pgvector. List the chunks stored and retrieved for one question.
3. Write an 8 to 10 definition glossary (open, won, deal value ...) and load it as knowledge for your day-8 agent.
4. Ask a question that needs a definition and the data. Show which chunk was retrieved.
5. Add storage; stop and restart the agent; show a second session remembering the first.

**Expected output:** A similarity table; a chunk list; an answer that visibly used the glossary; a restart demo.

**Break it on purpose:** Plant a wrong definition (for example 'Closed Won means stage Quotation'). Watch the agent obey it, then write the eval question or test that would catch it.

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** When does a fact belong in knowledge, in memory, or in the instructions?

### Checklist
- [ ] Compute embeddings and cosine similarity by hand
- [ ] Run both RAG examples and inspect chunks
- [ ] Write the glossary and load it
- [ ] Add storage/memory and test restart
- [ ] Plant a wrong definition and catch it

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] embeddings-by-hand/: your similarity table and what it shows
- [ ] A table: question | retrieved chunks | answer | was the definition used?
- [ ] Restart demo log showing memory persisted
- [ ] bad-glossary/NOTES.md describing the detection method you chose and proof it works

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What does chunk size change in retrieval quality and cost?
- When would you NOT use retrieval?

## Suggested tools
- pgvector (via run_pgvector.sh)
- psql to inspect the vector table
- Markdown for glossary

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-09-<topic>` into `main`

## Demo
Show a question answered from the glossary and the data, with the retrieved chunks.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What is an embedding? What does chunk size change?
- [ ] When should a fact go in knowledge, in memory, or in the instructions?
- [ ] The agent answered from the glossary, but the glossary was wrong. How would you catch that?

## Done when
Your agent uses the glossary correctly and you can explain what was retrieved and why.
