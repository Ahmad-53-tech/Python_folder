# A bank wants to provide a simple system where customers can deposit and withdraw money from their account while ensuring that
#transactions follow basic banking rules. Each customer has an account holder name and the current balance. The system should allow
#customers to:
# * Deposit money but only if the deposit amount is positive otherwise, it should display deposit amount must be greater than
#zero


# * Withdraw money but only if they have sufficient funds otherwise, it should display insufficient funds. If the withdrawal amount is
# less than zero, print withdrawal amount must be greater than zero.

# * View the account details including their account balance.
# The account holder name should be Alice, and the balance should be $500, first deposit $200, first withdrawal 100$, second withdrawal
# $700, second deposit $50 and third withdrawal $20


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amt):

        if amt > 0:
            print(f"Deposit Successful! you deposited ${amt}.")
            self.balance += amt
            print(f"Current Balance: {self.balance}")
        else:
            print(f"You tried to deposit {amt}. Amount must be greater than 0")

    def withdraw(self, amt1):
        if amt1 <= 0:
            print(f"You tried to withdraw {amt1}. Amount must be greater than 0")
        elif amt1 < self.balance:
            print(f"Withdrawal Successful! you withdrew ${amt1}.")
            self.balance -= amt1
            print(f"Current Balance: {self.balance}")

        else:
            print("Insufficient Funds")

    def view_details(self):
        print(f"Account Placeholder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")



# Creating
alice_bank_account = BankAccount("Alice", 500)
print(f"Account Placeholder: {alice_bank_account.account_holder}")
print(f"Balance: {alice_bank_account.balance}")
print()
alice_bank_account.deposit(200)
print()
alice_bank_account.withdraw(100)
print()
alice_bank_account.withdraw(700)
print()
alice_bank_account.deposit(-50)
print()
alice_bank_account.withdraw(-20)
print()
alice_bank_account.view_details()



