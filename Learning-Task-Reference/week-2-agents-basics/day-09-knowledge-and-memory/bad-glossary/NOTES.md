# Catching a wrong glossary

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 09: Knowledge and memory** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Retrieved text is trusted by the agent. A wrong definition produces confidently wrong answers, so it needs its own checks.

**How does it work?** wrong chunk > retrieved > agent obeys it > wrong answer

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- How would a test or eval question reveal a wrong definition?
- Who reviews the glossary and when?

## What to do
1. Plant one wrong definition on purpose; observe the agent follow it
2. Design a way to catch this (test, eval question, review rule)

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- notes on how you detect a wrong definition + proof

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
