# Tool calling

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 08: Tools: letting the agent act** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** The model cannot run code. It can only reply with a structured request ('call run_sql with this argument'). The framework validates it, runs your function, and sends the result back as a message.

**How does it work?** tools > schemas (name, description, typed args) sent to model > model asks for a tool > framework runs it > result appended > model called again > final answer

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does the model see about a tool? What does it not see?
- Who validates the arguments, and what if they are wrong?
- What if the tool raises an error? What should the model see?
- Why does the docstring matter so much?

## What to do
1. Run agent_with_tools.py with debug output; list each tool call, its arguments and its result
2. Write a tiny harmless tool (add two numbers) with a clear docstring; print the schema the framework generates from it and compare with what you would write by hand
3. Rewrite the docstring badly (vague); observe how the model's use of the tool changes
4. Find in the code where tools are parsed and where calls are run (libs/agno/egpt/agent/_tools.py: parse_tools, run_tool; libs/agno/egpt/models/base.py: get_function_calls_to_run, run_function_calls)

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/00_quickstart/agent_with_tools.py`
- `libs/agno/egpt/tools/decorator.py`
- `libs/agno/egpt/agent/_tools.py` — parse_tools, run_tool
- `libs/agno/egpt/models/base.py` — get_function_calls_to_run, run_function_calls

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
