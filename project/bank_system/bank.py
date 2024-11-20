from typing import Dict, Optional
from decimal import Decimal
from .models import Account

class Bank:
    def __init__(self, name: str):
        self.name = name
        self._accounts: Dict[str, Account] = {}

    def create_account(self, account_number: str, holder_name: str, 
                      initial_balance: Decimal = Decimal('0.00')) -> Optional[Account]:
        if account_number in self._accounts:
            return None
        
        account = Account(account_number, holder_name, initial_balance)
        self._accounts[account_number] = account
        return account

    def get_account(self, account_number: str) -> Optional[Account]:
        return self._accounts.get(account_number)

    def list_accounts(self) -> Dict[str, Account]:
        return self._accounts.copy()

    def transfer(self, from_account_number: str, to_account_number: str, 
                amount: Decimal) -> bool:
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if not from_account or not to_account:
            return False

        if from_account.withdraw(amount, f"Transfer to {to_account_number}"):
            to_account.deposit(amount, f"Transfer from {from_account_number}")
            return True
        return False