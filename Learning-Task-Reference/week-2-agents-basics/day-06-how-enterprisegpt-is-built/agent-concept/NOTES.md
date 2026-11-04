# What an agent is, and how the loop works

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 06: How agents work, and how EnterpriseGPT is built** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An agent is a model in a loop with tools. It decides the next step itself: answer, or call a tool, read the result, and decide again. A chatbot only replies; a workflow follows steps you fixed in advance.

**How does it work?** user goal > build messages (instructions + history + knowledge + user) > model decides: final answer OR tool call > your code runs the tool > result added as a message > model called again > ... > final answer (optionally parsed into a schema) > session/memory saved

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What stops the loop?
- Which parts of the agent are 'the model', and which are your code?
- When would you choose a workflow instead of an agent?
- What can go wrong in the loop, and how would you notice?
- Which Agent field controls each part: model, instructions, tools, knowledge, db, output_schema?

## What to do
1. Draw the agent loop on one page: user goal, messages built, model decision, tool call, tool result, next model call, final answer
2. Label every box with the matching field of the Agent class in libs/agno/egpt/agent/agent.py (model, instructions, tools, knowledge, db, add_history_to_context, enable_agentic_memory, output_schema, ...)
3. Write one example each of what a chatbot, a workflow and an agent would do for the same request
4. List 5 ways an agent can fail (wrong tool, bad arguments, endless loop, cost blow-up, confident wrong answer) and one defence for each

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/agent/agent.py` — the Agent dataclass: read the field list (model, instructions, tools, knowledge, db, output_schema ...)

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- loop diagram labelled with Agent field names
- failure-modes table

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
