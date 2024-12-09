# Custom Exception
class InsufficientFunds(Exception):
    pass

# Bank Account Class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFunds("Withdrawal amount exceeds account balance.")
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        except InsufficientFunds as e:
            print(f"Exception: {e}")

# Example Usage
account_balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
account = BankAccount(account_balance)
account.withdraw(withdraw_amount)
