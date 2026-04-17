# Why the Repo Is Structured This Way

## Goal
This repo is designed to model a good beginner-to-intermediate Databricks project structure.

## Main principles
### 1. Notebooks are staged
Each notebook has a focused purpose.

### 2. SQL is separated
The `sql/` folder makes it easier to see staged SQL logic clearly.

### 3. Sample data is versioned
Small sample files are included in GitHub so the project is portable.

### 4. Live workspace objects are not versioned
Unity Catalog objects and notebook runtime state are not GitHub artifacts.

### 5. Automation is introduced lightly
A job sequence is suggested without making the project depend on advanced production tooling.
