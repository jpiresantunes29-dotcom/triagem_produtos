# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```bash
cd src
python main.py
```

The program is interactive and runs entirely in the terminal — no arguments needed.

## Architecture

The project is a terminal-based order triage system split across four modules in `src/`:

- **`main.py`** — entry point; runs the interactive menu loop and handles order registration (`register_orders`). Orders are stored in-memory as a list of dicts for the duration of the session.
- **`rules.py`** — single function `classify_order(...)` that applies the business rules and returns `(status, reason)`. Status values: `"APPROVED"`, `"UNDER REVIEW"`, `"BLOCKED"`.
- **`validations.py`** — input helpers (`read_positive_integer`, `read_non_negative_integer`, `read_non_negative_float`, `read_yes_or_no`) that loop until valid input is received.
- **`reports.py`** — display functions that operate on the orders list: list all, summary counts by status, highest-value order, blocked orders only.

## Classification rules (priority order)

1. **BLOCKED** if: payment not approved, OR client under 18, OR address not confirmed
2. **UNDER REVIEW** if (not blocked): amount > 1000, OR item count ≥ 10, OR (non-premium client AND amount > 500)
3. **APPROVED** otherwise

## Order data structure

Each order dict contains: `code`, `amount`, `age`, `item_count`, `payment_approved`, `premium_client`, `address_confirmed`, `status`, `reason`.

`yes`/`no` fields are stored as strings (not booleans).
