# Repository map

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 06: How agents work, and how EnterpriseGPT is built** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** EnterpriseGPT keeps the generic agent framework (libs/agno/egpt) separate from the retail application (product/egpt_retail) so the framework knows nothing about any one industry.

**How does it work?** framework (agents, tools, models, knowledge) > used by application (contracts, warehouse, semantic layer, KPIs, use cases, API) > shown by frontend > shown by cookbook examples

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Why keep framework and application apart?
- Where would a new generic tool go? A new retail KPI?
- Which folder do you read first to learn a pattern, and why?

## What to do
1. One sentence per folder: libs/agno/egpt, product/egpt_retail, frontend, cookbook, deploy, scripts, docs
2. Coding rules in CLAUDE.md: sync and async variants of public methods; never create agents inside a loop; PostgreSQL in production
3. Find where your scratch loop's pieces live in the framework (look in libs/agno/egpt/agent/ and libs/agno/egpt/models/); you will trace this properly on day 7

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `CLAUDE.md` — 'Repository Structure'
- `ARCHITECTURE.md` — 'Code Layout'

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
