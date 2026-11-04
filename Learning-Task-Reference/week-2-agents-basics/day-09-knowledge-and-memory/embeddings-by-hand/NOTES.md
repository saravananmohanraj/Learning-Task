# Embeddings and similarity, by hand

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 09: Knowledge and memory** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An embedding turns text into a list of numbers so that texts with similar meaning are close together. Search then means 'find the nearest vectors'.

**How does it work?** text > embedding model > vector > compare with cosine similarity/distance > rank

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does 'close' mean for two vectors?
- Why do two sentences with different words still end up close?
- What does the embedding dimension mean, and why must it match the table?

## What to do
1. Embed 6 short sentences (3 about deals, 3 unrelated) with the embedder your mentor names
2. Compute cosine similarity yourself (numpy) between a question and each sentence; rank them; check the ranking makes sense
3. Change one word in a sentence and see how much the vector and the ranking move
4. Relate your result to the pgvector distance operator: run a similar query in SQL

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/vectordb/pgvector/pgvector.py` — how vectors are stored and compared
- `cookbook/07_knowledge/01_getting_started/01_basic_rag.py` — which embedder the examples use

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `embed.py`
- similarity table

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
