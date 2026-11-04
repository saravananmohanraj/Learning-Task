# Human approval

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 10: Teams, workflows and a person in the loop** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Human-in-the-loop pauses a run before a sensitive step until a person approves; a rejection must leave the system unchanged.

**How does it work?** step produces draft > run pauses > person approves/rejects > approve: continue and save; reject: stop and log reason

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Where exactly does the pause sit?
- What state is saved while waiting?
- What happens when nobody answers?

## What to do
1. Approve once, reject once; define what rejection does (nothing saved, reason logged)
2. Tests for the approval logic without model calls

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/00_quickstart/human_in_the_loop.py`
- `libs/agno/egpt/approval/decorator.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- approval logic + tests
- run_output.md (approve once, reject once)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
