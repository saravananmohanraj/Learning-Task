# RAG basics

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 09: Knowledge and memory** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Retrieval-augmented generation fetches only the relevant pieces of your documents and puts them in the prompt, instead of pasting everything.

**How does it work?** documents > chunk > embed > store in pgvector; at question time: embed question > nearest chunks > added to prompt > model answers

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does chunk size change (quality, cost, context)?
- What is the difference between basic RAG and agentic RAG?
- When does retrieval fail?
- How do you see which chunks were used?

## What to do
1. Run 01_basic_rag.py and 02_agentic_rag.py against the project's Postgres (pgvector) with the embedder your mentor names
2. Record chunks stored and which chunks were retrieved for one question
3. Change chunk size; compare retrieval

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/07_knowledge/01_getting_started/01_basic_rag.py`
- `cookbook/07_knowledge/01_getting_started/02_agentic_rag.py`
- `cookbook/scripts/run_pgvector.sh`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
