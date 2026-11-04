# Read-only database user

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 08: Tools: letting the agent act** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A database role that can only read. Even if code or a model misbehaves, the database itself refuses writes.

**How does it work?** agent > tool > connection as read-only role > Postgres checks privileges > refuses INSERT/UPDATE/DELETE/DDL

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What privileges does the role need?
- How do you prove it cannot write?
- Why do you still need a code guard?

## What to do
1. CREATE ROLE with LOGIN, GRANT CONNECT and SELECT only on your tables
2. Prove writes fail with that user

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/warehouse/sql/ddl/065_readonly_role.sql` — compare with your role

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `create_role.sql`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
