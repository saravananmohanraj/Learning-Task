# Your evaluation set

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 13: Evaluating agents** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An evaluation set is questions with expected answers you computed yourself, so you can score an agent repeatably.

**How does it work?** question + expected answer (from your SQL) > run agent > compare > score > failure analysis

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Why must expected answers come from SQL, not from the agent?
- Which questions are traps (counting rows, NULLs)?

## What to do
1. 10 questions with expected answers over your deals data (include at least 2 tricky ones: counting rows trap, NULLs)
2. Expected answers computed by YOUR SQL, not by the agent

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- questions file (json/csv)
- the SQL that produced each expected answer

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
