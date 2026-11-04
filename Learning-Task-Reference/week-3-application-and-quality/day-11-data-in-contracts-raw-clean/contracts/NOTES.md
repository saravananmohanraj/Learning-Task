# Contracts

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 11: Data in: contracts, raw and clean** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A data contract is a written agreement on file layout, fields, types, and what counts as a defect, so loading needs no guessing.

**How does it work?** source writes files to the agreed path > loader checks them against the contract > good rows loaded, bad rows reported as defects

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does the landing contract fix? What does the load contract fix?
- What is a defect, and what is a blocked load?

## What to do
1. Summarise both contracts in your words (what is required, what is a defect, what is a blocked load)

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md`
- `product/egpt_retail/warehouse/LOAD_CONTRACT.md`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
