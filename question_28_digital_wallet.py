class InsufficientBalanceError(Exception):
    pass


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError
            self.balance -= amount
            print("Payment successful. Remaining:", self.balance)
        except InsufficientBalanceError:
            print("Payment failed: Insufficient balance")


wallet = Wallet(1000)

wallet.pay(300)
wallet.pay(800)