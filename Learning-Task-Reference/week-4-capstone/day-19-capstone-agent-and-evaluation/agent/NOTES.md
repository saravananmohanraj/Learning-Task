# The agent

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 19: Capstone 4: the agent and its evaluation** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** The capstone agent explains and answers using only numbers returned by its SQL tool; KPI definitions come from knowledge.

**How does it work?** question > agent > knowledge lookup (definitions) > read-only SQL tool > numbers > typed answer

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- How do you guarantee a number came from the tool?
- What should it do with a question outside the data?

## What to do
1. Answers e.g. 'how many issues closed last week, and is that above the 8-week median?'
2. Typed output with the SQL used; refuses questions it cannot answer from data

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `agent.py`
- sample runs

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
