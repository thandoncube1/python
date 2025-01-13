# Example file for Advanced Python by Joe Marini
# Defining and using custom exceptions in Python

# Define a custom exception class


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Create a bank account with an initial balance of $100
account = BankAccount(100)

try:
    account.deposit(10)
    # should work
    account.withdraw(50)
    # Attempt to withdraw $100, which exceeds the balance
    account.withdraw(100)
finally:
    print(f"Current balance: ${account.get_balance():.2f}")
