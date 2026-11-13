"""Expense Splitter: who owes whom, with the fewest payments.

Team: Crocosoftware
License: MIT
"""

# An expense is (payer, amount in EUR, people who share it).
Expense = tuple[str, float, list[str]]
# A transfer is (debtor, creditor, amount in EUR).
Transfer = tuple[str, str, float]
