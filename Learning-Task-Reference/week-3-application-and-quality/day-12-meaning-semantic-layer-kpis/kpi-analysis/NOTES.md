# One KPI analysed

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 12: Meaning: the semantic layer and KPIs** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A KPI is a SQL formula a person accepted; the system computes it without a model. Agents may suggest KPIs; they never compute them.

**How does it work?** suggestion > person accepts > formula registered > feasibility checked against entities > computed by SQL per date

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What makes a KPI feasible or not?
- Why can a model never be the source of the number?

## What to do
1. Formula, entities used, why feasible or not

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/94_retail/K11_kpi_formula_shape.py`
- `cookbook/94_retail/K11_kpi_registry_and_feasibility.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
