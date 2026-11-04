# SQL guard

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 08: Tools: letting the agent act** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A guard checks SQL text before it runs: exactly one statement, SELECT only, with limits. It is a second line of defence next to the read-only role.

**How does it work?** query string > parse > reject if not a single SELECT > add/enforce row cap and timeout > run

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What tricks could get a write past a naive check (multiple statements, comments, CTEs)?
- Why cap rows and time?
- Why is string matching weaker than parsing?

## What to do
1. Allow a single SELECT only; refuse DELETE/UPDATE/DROP, multiple statements, comments tricks
2. Cap returned rows; time out slow queries
3. Hand-written tests: DELETE, two statements in one string, allowed SELECT

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/guardrails/sql_guard.py` — compare AFTER you wrote yours
- `cookbook/94_retail/R06_sql_guard_parsing.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `sql_guard.py`
- `test_sql_guard.py`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
