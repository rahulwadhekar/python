class DailyLimitExceededError(Exception):
    pass


class Wallet:
    def transfer(self, amount):
        pass


class BasicWallet(Wallet):
    def transfer(self, amount):
        if amount > 10000:
            raise DailyLimitExceededError
        print("Transferred with 2% fee:", amount * 1.02)


class PremiumWallet(Wallet):
    def transfer(self, amount):
        print("Transferred without fee:", amount)


try:
    w = BasicWallet()
    w.transfer(15000)

except DailyLimitExceededError:
    print("Daily limit exceeded!")