class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print("Current balance is:", self.balance)


def main():
    # Account with no previous amount of money.
    no_prev_money_acc = BankAccount()
    # Account with previous amount of money.
    with_prev_money_acc = BankAccount(2000)
    no_prev_money_acc.deposit(1)
    with_prev_money_acc.deposit(1)
    no_prev_money_acc.print_balance()
    with_prev_money_acc.print_balance()
