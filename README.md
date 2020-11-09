# QA Engineer Technical Task 1

## Task

Plan and implement a testing plan for a simple administrative console application.

## Getting started

You will need to spin up the dev stack by following the instructions in [./INSTALL.md](./INSTALL.md). Working knowledge of docker, python and javascript are required/assumed.

## Requirements

- Pretend that you are writing a full test suite for the entire application. Write a 1-2 page test plan describing (at a minimum):
	- overall objectives and approach
	- components to be tested
	- specific tests to be used
	- pass/fail criteria

- Write actual tests for the following features of the application:
	- unit tests of CRUD functionality for Organization model (minitest)
	- functional test [login page](http://localhost:8080/admin) (nightwatch)
	- functional test of [user model edit page](http://localhost:8080/admin/core_admin/user/2/change/) (nightwatch)

Submit your work by as a git repo at a public host of your choice (e.g. gitlab, github).

## Notes:

- Scope the tasks out in a reasonable fashion -- you don't need to write 100 tests for each feature but you probably need more than 1.

- If you wish, you may use different frameworks to conduct the tests (e.g. WebdriverIO instead of nightwatch). However, you will need to provide sufficient documentation/code to replicate your tests.

- You may reuse your own code from prior work.

- You may use code snippets from other authors but they must be annotated in comments, and they must not constitute wholesale copying (to be arbitrated by Geosite engineers)

## Evaluation criteria:

- Is your test plan comprehensive and sufficient to ensure product quality? 
- Are all the task requirements met?
- Are your tests well written and sufficient for testing the features they  intend to test? Do they fulfill meaningful pass/fail criteria? 
