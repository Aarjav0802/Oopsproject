from decimal import Decimal
from bank_system.bank import Bank

def main():
    # Create a new bank
    bank = Bank("PyBank")
    
    # Create some accounts
    account1 = bank.create_account("1001", "John Doe", Decimal("1000.00"))
    account2 = bank.create_account("1002", "Jane Smith", Decimal("500.00"))

    # Perform some transactions
    if account1:
        print(f"\nInitial state for {account1.account_holder}:")
        print(account1)
        
        account1.deposit(Decimal("250.50"), "Salary deposit")
        account1.withdraw(Decimal("100.00"), "ATM withdrawal")
        
        print("\nAfter transactions:")
        print(account1)
        
        print("\nTransaction history:")
        for transaction in account1.get_statement():
            print(transaction)

    # Perform a transfer
    if account1 and account2:
        print("\nPerforming transfer...")
        bank.transfer("1001", "1002", Decimal("200.00"))
        
        print(f"\n{account1.account_holder}'s account:")
        print(account1)
        print(f"\n{account2.account_holder}'s account:")
        print(account2)

if __name__ == "__main__":
    main()