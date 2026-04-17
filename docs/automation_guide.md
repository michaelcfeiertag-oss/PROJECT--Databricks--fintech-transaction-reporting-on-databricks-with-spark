# Automation Guide

## Goal
Introduce a lightweight automation idea for the project.

## Required concept
The project should be runnable in a defined order:
1. ingest raw data
2. prepare silver data
3. build gold reports
4. run data quality checks

## Option A — Use the Databricks Jobs UI
If the Jobs feature is available:
- create a multi-task job
- add notebook tasks in the order listed above
- run manually first
- optionally add a schedule

## Option B — Manual automation plan
If Jobs is not available in your workspace:
- document the notebook sequence
- explain task dependencies
- describe where failures should stop the run
- note which outputs should exist after each stage

## Why this matters
This teaches that a good data project should be repeatable, not just runnable once by hand.

## Included starter file
See `databricks.yml` for an optional example of a more formal job definition.
