# Language model basics

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 06: How agents work, and how EnterpriseGPT is built** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A language model predicts the next token from all the tokens it is given (the context). It has no memory between calls and cannot reach your systems. Everything it should know about your task must be inside the messages you send.

**How does it work?** text > tokens > model scores possible next tokens > temperature controls how random the pick is > repeat until a stop > text out

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What is a token? How many tokens is a short sentence?
- What is the context window and what happens when you exceed it?
- What does temperature change? Why can the same prompt give different answers?
- Why does a long conversation cost more, call after call?
- What is a hallucination, and why does it happen?
- List three things a model cannot do on its own.

## What to do
1. Count tokens for 3 texts of different length (use the provider's token counter) and work out the cost of each
2. Send the same prompt 3 times at temperature 0 and at a high temperature; record what changes
3. Ask the model something it cannot know (for example the stage of 'deal D-1001'); watch it guess; write what this tells you
4. Fill the context window on purpose with a long text and see what happens

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/90_models` — see which providers the framework supports

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- token and temperature results table

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
