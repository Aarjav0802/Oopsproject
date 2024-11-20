from datetime import datetime
from typing import List, Optional
from decimal import Decimal

class Transaction:
    def __init__(self, amount: Decimal, transaction_type: str, description: str):
        self.amount = amount
        self.type = transaction_type
        self.description = description
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return f"{self.timestamp}: {self.type} - {self.amount} ({self.description})"

class Account:
    def __init__(self, account_number: str, account_holder: str, initial_balance: Decimal = Decimal('0.00')):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transactions: List[Transaction] = []
        if initial_balance > 0:
            self.transactions.append(
                Transaction(initial_balance, "DEPOSIT", "Initial deposit")
            )

    @property
    def balance(self) -> Decimal:
        return self._balance

    def deposit(self, amount: Decimal, description: str = "Deposit") -> bool:
        if amount <= 0:
            return False
        
        self._balance += amount
        self.transactions.append(
            Transaction(amount, "DEPOSIT", description)
        )
        return True

    def withdraw(self, amount: Decimal, description: str = "Withdrawal") -> bool:
        if amount <= 0 or amount > self._balance:
            return False
        
        self._balance -= amount
        self.transactions.append(
            Transaction(amount, "WITHDRAWAL", description)
        )
        return True

    def get_statement(self) -> List[Transaction]:
        return self.transactions.copy()

    def __str__(self) -> str:
        return f"Account {self.account_number} - Balance: ${self.balance}"