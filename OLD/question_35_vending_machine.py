class ItemStuckError(Exception):
    pass


class Snack:
    def dispense_item(self, ok):
        try:
            if not ok:
                raise ItemStuckError
            print("Snack dispensed")
        except ItemStuckError:
            print("Error: Item stuck, refund issued")


class Drink:
    def dispense_item(self, ok):
        try:
            if not ok:
                raise ItemStuckError
            print("Drink dispensed")
        except ItemStuckError:
            print("Error: Item stuck, refund issued")


machines = [(Snack(), True), (Drink(), True), (Snack(), False)]

for machine, status in machines:
    machine.dispense_item(status)