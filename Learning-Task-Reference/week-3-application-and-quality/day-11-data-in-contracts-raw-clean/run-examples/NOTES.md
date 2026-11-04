# Run the examples

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 11: Data in: contracts, raw and clean** · [day README](../README.md)

## Understand it first (before you do anything)
Before the steps, answer these in your `ACTIVITY_LOG.md`, in your own words (read the docs first):
- What is this, in one or two sentences of your own?
- How does it work, step by step? Draw the flow.
- Why do we need it? What would go wrong without it?
- How will you know it is working? What would you check?

## What to do
1. docker compose -f deploy/compose.yaml up -d postgres
2. Run cookbook/94_retail/C01_landing_contract.py
3. Run R04_landing_to_silver.py with EGPT_RETAIL_WAREHOUSE_DB_URL set

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/94_retail/C01_landing_contract.py`
- `cookbook/94_retail/R04_landing_to_silver.py`
- `deploy/compose.yaml`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
