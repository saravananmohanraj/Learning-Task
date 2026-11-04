# Architecture one-pager

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 15: Capstone design: plan before you build** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A design on paper shows every part, what flows between them, and how each can be re-run safely, before any code.

**How does it work?** source > files > raw > clean > checks > KPIs > agent > eval, with re-run rules at each arrow

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What is the smallest version that still shows every layer?
- What will you cut if time runs out?

## What to do
1. Diagram: GitHub API > NDJSON files > raw.github_issue > clean.issue > checks > KPIs > agent > eval
2. For each box: input, output, who writes it, how to re-run safely

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `ARCHITECTURE.md` — 'Layer Diagram', 'Data Flow'
- `docs/plan/analytics-automation-design.md`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- architecture diagram (png / mermaid / drawio)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
