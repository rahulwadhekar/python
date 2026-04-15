class InsufficientFundsError(Exception):
    pass


class PaymentProcessor:
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        total = amount * 1.02
        balance = 1000
        if total > balance:
            raise InsufficientFundsError
        print("Paid via Credit Card:", total)


class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        total = amount + 50
        balance = 1000
        if total > balance:
            raise InsufficientFundsError
        print("Paid via Crypto:", total)


payments = [CreditCardPayment(), CryptoPayment()]

for p in payments:
    try:
        p.process_payment(900)
    except InsufficientFundsError:
        print("Insufficient balance")