# Judge reliability

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 13: Evaluating agents** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An agent can act as judge of another agent's answer, but a judge is a model too and can be wrong.

**How does it work?** answer + expected > judge agent > score with reason > spot-check judge against human decisions

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Name three ways a judge can be wrong.
- How do you check the judge?

## What to do
1. Think of 3 ways an agent judge could be wrong; add a check for one

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/09_evals/agent_as_judge`
- `libs/agno/egpt/eval/agent_as_judge.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
