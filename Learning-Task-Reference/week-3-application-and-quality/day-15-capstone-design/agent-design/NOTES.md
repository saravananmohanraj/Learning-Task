# Agent design

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 15: Capstone design: plan before you build** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Agent design decides tools, knowledge, instructions and guardrails, and what the agent must refuse.

**How does it work?** question > guardrails > agent (instructions + knowledge) > read-only SQL tool > typed answer with the SQL used

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Where could a model mistake reach a user, and what stops it?
- What does the agent refuse?

## What to do
1. Tool list (read-only SQL over clean), knowledge (KPI definitions), instructions outline
2. Output schema for answers; guardrails

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/00_quickstart/agent_with_guardrails.py`
- `libs/agno/egpt/guardrails/prompt_injection.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `agent_design.md`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
