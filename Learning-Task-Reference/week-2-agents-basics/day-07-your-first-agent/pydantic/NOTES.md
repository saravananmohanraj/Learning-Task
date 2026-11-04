# Pydantic models

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 07: Your first agent** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Pydantic defines data shapes as Python classes and validates real data against them. A bad value fails loudly with a clear error instead of flowing on silently.

**How does it work?** raw data (dict/JSON) > Model(**data) > types checked and coerced > ValidationError listing every problem, or a typed object

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does Pydantic do with a string '12' for an int field?
- How do you make a field optional or constrained?
- What is a JSON schema and how is it produced from a model?

## What to do
1. Define a model with 4+ fields including an optional field and a constrained field
2. Trigger and read 3 different ValidationErrors on purpose
3. Turn the model into a JSON schema (model_json_schema) and read it: this is what a provider gets

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `models.py`
- `test_models.py`
- captured ValidationErrors

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
