# Data flow drawing

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 11: Data in: contracts, raw and clean** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** EnterpriseGPT moves data raw files > raw table > clean > semantic layer > KPI values > dashboards/alerts/use cases. A model may help interpret or suggest, but numbers come from SQL.

**How does it work?** source > raw files (never changed) > raw table (every version) > clean (one row per thing) > semantic layer (meaning) > KPI values (SQL) > dashboards/alerts

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Why are raw files never changed?
- Where does a model run? Where must it never run?
- What goes wrong if KPIs are computed from the raw table?

## What to do
1. Draw the layers from the repo README in your own words, from a source system to a dashboard
2. For each layer write one sentence: what it holds and who writes it
3. Mark where an AI model runs and where it must not, and say why

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `ARCHITECTURE.md` — Data Flow
- `docs/plan/domain-knowledge-layers.md`
- `README.md`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- flow diagram (png / mermaid / drawio)
- layers.md (one sentence per layer)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
