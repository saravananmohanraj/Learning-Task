# Structured output

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 07: Your first agent** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Structured output means the model's reply must fit a schema, so software can use it. The framework sends the schema to the provider as a response format, then parses the reply back into your Pydantic object.

**How does it work?** output_schema > converted to a response format > sent with the messages > model replies in that shape > framework parses into the object > validation error if it does not fit

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Why is free text hard to use in code?
- What does output_schema change in what the model is asked to do?
- What happens when the reply is invalid, and what would you do about it?

## What to do
1. Ask the same question twice with a provider SDK directly: once for free text, once asking for JSON only; parse both in code and note which breaks first
2. Read how the framework builds the response format and converts the reply back (libs/agno/egpt/agent/_response.py: get_response_format, convert_response_to_structured_format)
3. Break it on purpose: give a schema the model finds hard to fill; observe the failure and how the framework reports it

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/agent/_response.py` — get_response_format, convert_response_to_structured_format
- `cookbook/00_quickstart/agent_with_structured_output.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- comparison of free text vs JSON vs schema

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
