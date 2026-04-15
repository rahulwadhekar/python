class OverdraftLimitExceededError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 500:
            print("Minimum balance required")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < -1000:
            raise OverdraftLimitExceededError
        self.balance -= amount
        print("Withdrawn:", amount)


try:
    acc = CurrentAccount(500)
    acc.withdraw(2000)

except OverdraftLimitExceededError:
    print("Overdraft limit exceeded")