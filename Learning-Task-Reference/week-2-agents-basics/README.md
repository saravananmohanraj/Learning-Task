# Week 2: building agents with the framework (basics first)

**Rule this week:** AI may help write code, but you must be able to explain and change every line without it. Model keys go in a local `.env` that git ignores, never in code, commits, prompts or chat.

**Theme:** learn how agents work from the outside in, one building block per day. Every block follows the same pattern: understand it first, then build something small, then break it on purpose.

**Outcome:** you can build an agent with model, instructions, typed output, tools, knowledge, memory, and a workflow with human approval, and you can explain a run trace line by line.

## How the week builds
| Day | Building block | Builds on |
|---|---|---|
| [06](./day-06-how-enterprisegpt-is-built/README.md) | Models, prompts, the agent loop, repo map | Week 1 setup |
| [07](./day-07-your-first-agent/README.md) | Agent + structured output | Day 4 deals data |
| [08](./day-08-tools-letting-the-agent-act/README.md) | Tools (safe SQL) | Day 3-4 SQL, Day 7 agent |
| [09](./day-09-knowledge-and-memory/README.md) | Knowledge (RAG) and memory | Day 8 agent |
| [10](./day-10-teams-workflows-human-in-loop/README.md) | Workflow, team, approval | Day 8-9 agent |

## Concept first, then build
Every topic folder's `NOTES.md` starts with **Understand it first**: what the thing is, how it works as a flow, and questions you answer in your own words *before* you touch code. Agents are built on a few simple ideas; if you know them, the framework stops being magic.

| Day | Ideas you must own before building |
|---|---|
| 06 | Language model, tokens, context, temperature, prompt, **the agent loop**, chatbot vs workflow vs agent. You build a tiny agent with no framework. |
| 07 | Structured output, schemas, validation. You trace what the framework does for you from your day-6 loop. |
| 08 | Tool calling (the model only asks; your code runs), grounding, defence in depth. |
| 09 | Embeddings and similarity (computed by hand), the RAG flow, knowledge vs memory vs history. |
| 10 | Agent vs team vs workflow as flows, human approval. |

The ladder for every block: **understand > see it run > build the smallest version > extend > break it on purpose > explain**.

## Working pattern (use it every day)
1. **Understand:** read, then explain the concept in your own words in the topic's `ACTIVITY_LOG.md`.
2. **Predict:** before you run something, write what you expect to happen.
3. **Run and observe:** record the real output in `ACTIVITY_LOG.md`.
4. **Break it:** change one thing on purpose; note what fails and why.
5. **Explain:** to your buddy first, then in the explain-back.

## Suggested tools for the week
| Need | Tool |
|---|---|
| Edit, search | VS Code, `git grep`, `rg` |
| Database | `psql`, `pgcli`, DBeaver |
| Secrets | `.env` + python-dotenv; check `git diff --cached` before every commit |
| JSON | `jq` |
| Diagrams | Mermaid, draw.io, Excalidraw |
| Testing | pytest (never call the model in tests) |

## End-of-week check
20-minute explain-back of your day 8 to 10 code chosen by the reviewer, plus a short quiz on tools, retrieval and memory.
