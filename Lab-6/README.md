# Lab 6: Movie Ticket Booking

## Objective

Use automated tests to check ticket pricing, group discounts and snack combo pricing, including boundary cases and exceptions.

## Tools

Python, pytest and pytest-cov.

## Functions tested

- `ticket_price()`: seat type, show time, weekday/weekend and age pricing.
- `group_discount()`: ticket count thresholds and student groups.
- `snack_combo()`: combo size and coupon pricing.

## Run tests and coverage

From this folder, run:

```powershell
python -m pytest -v test_code_coverage.py
python -m pytest --cov=movie_tickets --cov-branch --cov-report=term-missing test_code_coverage.py
python -m pytest -v test_branch_coverage.py
python -m pytest --cov=movie_tickets --cov-branch --cov-report=term-missing test_branch_coverage.py
python -m pytest --cov=movie_tickets --cov-branch --cov-report=html
```

Open `htmlcov/index.html` in a browser to view the HTML coverage report.
