# Practice: run_sql agent

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 08: Tools: letting the agent act** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Grounding: the model only knows your table if the instructions and tool description tell it. Without the 'latest version per deal' rule it counts rows instead of deals.

**How does it work?** question > agent writes SQL (guided by instructions) > run_sql tool > rows > agent explains

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Where do you look first when the number is wrong: the question, the SQL, or the data?
- How do you know the agent used the right table description?
- What instruction change fixed the counting mistake, and why?

## What to do
1. Agent instructions describe the raw_deals table and the 'latest version per deal' rule
2. Ask: how many deals are Closed Won? What is the total value of open deals?
3. Compare with your own day-4 answers; fix instructions/tool description until it stops counting rows

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `agent.py`
- iterations.md (each instruction change and its effect)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
