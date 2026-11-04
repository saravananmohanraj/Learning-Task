# Prompts and instructions

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 06: How agents work, and how EnterpriseGPT is built** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A prompt is the whole list of messages sent to the model: a system message (role and rules), the history, and the user message. In an agent, 'instructions' become the system message.

**How does it work?** system message + history + user message > model > reply

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What belongs in the system message and what in the user message?
- Why do specific prompts with a format and an example usually work better?
- What is prompt injection, and why is it a risk when the data itself contains text?
- How would you know a prompt change made the answer better and not just different?

## What to do
1. Write 3 versions of a prompt that summarises a deal: vague, specific, specific with an example and a required format; compare the outputs
2. Separate the system message (rules, role) from the user message (the request); show how each changes the answer
3. Try a harmless 'prompt injection' (text inside the data that tells the model to ignore its rules); record what happens and why it matters later

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- the 3 prompts and their outputs

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
