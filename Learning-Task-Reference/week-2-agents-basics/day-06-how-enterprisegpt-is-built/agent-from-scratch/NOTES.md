# Practice: an agent with no framework

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 06: How agents work, and how EnterpriseGPT is built** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Writing the loop yourself with the provider SDK shows there is no magic: an agent is a while-loop around model calls plus a dictionary of functions.

**How does it work?** messages > call model > if reply contains tool_call: run function, append result, call model again; else: done

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- How does the provider tell you the model wants a tool? What does the reply look like?
- What must you send back after running the tool so the model can continue?
- What happens if the model asks for a tool that does not exist, or with bad arguments?
- What is the maximum-iterations guard protecting you from?

## What to do
1. Using only the provider's SDK, write the loop yourself in under about 60 lines: send messages, if the reply asks for a tool, run it, append the result, call the model again, stop when it answers
2. Give it one fake tool (for example get_deal_stage(deal_id) reading from a dict)
3. Add a maximum-iterations guard so it can never loop forever
4. Print every message so you can see the whole conversation
5. Test the loop with a fake model (a function that returns canned replies); the test must not call the real model

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/models/base.py` — afterwards: where the framework does your loop (response, get_function_calls_to_run, run_function_calls)

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `agent_loop.py`
- test_agent_loop.py (fake model, no network)
- `transcript.txt`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
