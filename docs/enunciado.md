# Project Brief

## Context

A small online store needs a simple system to perform the initial triage of orders before shipping. Currently, this verification is done manually, which slows down the process and increases the chance of errors.

Your challenge is to develop a Python program capable of analyzing orders based on business rules and reporting whether each purchase should be approved, sent for review, or blocked.

## Objective

Create an order triage system that allows:

- registering orders via terminal
- validating entered information
- classifying orders according to defined rules
- storing orders during execution
- querying reports and listings using an interactive menu

## Required concepts

The project must require the integrated use of the following fundamental programming concepts:

- relational operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- logical operators: `and`, `or`, `not`
- conditional structures: `if`, `elif`, `else`
- loop structures

## Input data

For each order, the program must receive:

- order code
- order amount
- client age
- item count
- payment approved (`yes` or `no`)
- premium client (`yes` or `no`)
- address confirmed (`yes` or `no`)

Inputs must be validated to avoid:
- negative numbers
- invalid quantities
- responses outside the expected pattern

## Classification rules

### Blocked order

The order must be classified as `BLOCKED` when any of the following occurs:

- payment not approved
- underage client
- address not confirmed

### Order under review

If the order is not blocked, it must be classified as `UNDER REVIEW` when at least one of the following occurs:

- order amount greater than `1000`
- item count greater than or equal to `10`
- non-premium client with order above `500`

### Approved order

The order will be classified as `APPROVED` when:

- it does not meet the blocking rules
- it does not meet the review rules

## Expected outputs

For each registered order, the program must display:

- order code
- final analysis status
- main reason for classification

The system must also allow querying:

- all registered orders
- general summary with count by category
- highest value order
- list of blocked orders

## Functional requirements

The program must:

- use `for` when registering multiple orders
- use `if`, `elif`, and `else` for decisions
- apply logical and relational operators in the rules
- validate user inputs
- organize code into functions
- allow navigation via menu

## Possible expansions

After the initial version, the project can evolve with:

- file persistence
- filters by status
- average order amount calculation
- percentage of approved, reviewed, and blocked orders
- order editing
- graphical interface
- database integration

## Expected result

At the end, the project should represent a small Python system capable of combining programming logic, input validation, modularization, and user interaction in a clear and functional way.
