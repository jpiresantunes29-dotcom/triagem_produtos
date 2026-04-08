# Order Triage

A Python system to register, classify, and query orders from an online store, applying approval, review, and blocking rules with input validation and simple reports.

## About the project

This project was developed with a focus on practicing programming logic and code organization in Python. The goal is to simulate a simple order triage system, like those used in online stores to analyze purchases before final approval.

During execution, the user can register orders, view saved records, and query reports directly from the terminal.

## Features

- order registration via terminal
- validation of numeric inputs and yes/no responses
- automatic order classification
- listing of all registered orders
- general summary with totals by category
- identification of the highest value order
- display of blocked orders only
- interactive menu to navigate through system options

## Classification rules

Each order receives one of the following statuses:

### `BLOCKED`
The order will be blocked when at least one of the following occurs:

- payment not approved
- underage client
- address not confirmed

### `UNDER REVIEW`
The order will be sent for review when it is not blocked but presents a risk condition, such as:

- order amount greater than `1000`
- item count greater than or equal to `10`
- non-premium client with order above `500`

### `APPROVED`
The order will be approved when it does not fit the blocking or review rules.

## Concepts practiced

This project covers several important programming fundamentals:

- relational operators
- logical operators
- conditional structures with `if`, `elif`, and `else`
- loops
- input validation
- code modularization
- organization across multiple files

## Project structure

```
triagem_produtos/
├── docs/
│   └── enunciado.md
├── src/
│   ├── main.py
│   ├── validations.py
│   ├── rules.py
│   └── reports.py
└── README.md
```
