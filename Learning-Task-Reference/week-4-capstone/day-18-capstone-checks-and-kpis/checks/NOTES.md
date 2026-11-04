# SQL checks

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 18: Capstone 3: checks and KPIs** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A check is SQL that proves something about the data. A check you have never seen fail proves nothing.

**How does it work?** check query > returns violations > zero rows = pass; any rows = fail

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Which check would catch counting rows instead of issues?
- What data quality dimension does each check cover?

## What to do
1. One row per issue in clean
2. Distinct keys in raw equal rows in clean
3. No issue closed before created
4. No failed casts

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/warehouse/sql/checks/`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `checks.sql`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
