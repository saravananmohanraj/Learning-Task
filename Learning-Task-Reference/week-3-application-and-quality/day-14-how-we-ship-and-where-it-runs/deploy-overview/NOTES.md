# Deploy overview

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 14: How we ship, and where it runs** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An image (built from a Dockerfile) is run as containers; compose starts several together; in Azure secrets live in Key Vault.

**How does it work?** Dockerfile > image > container(s) via compose > Azure: same image, config and secrets injected

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does each Dockerfile instruction do?
- Where does a model key live in production and why?

## What to do
1. Read Dockerfile line by line; explain each instruction
2. Draw where the app, Postgres and secrets live (local vs Azure)

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `deploy/Dockerfile`
- `deploy/compose.yaml`
- `deploy/AZURE_CUTOVER.md`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
