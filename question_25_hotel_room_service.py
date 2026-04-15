class DoNotDisturbError(Exception):
    pass


class CleaningService:
    def deliver(self, request, dnd):
        try:
            if dnd:
                raise DoNotDisturbError
            print("Cleaning Done" if request else "No cleaning requested")
        except DoNotDisturbError:
            print("Cleaning Rescheduled")


class FoodDelivery:
    def deliver(self, order, dnd):
        try:
            if dnd:
                raise DoNotDisturbError
            print("Food Delivered" if order else "No order placed")
        except DoNotDisturbError:
            print("Delivery Rescheduled")


services = [
    (CleaningService(), (True, False)),
    (FoodDelivery(), (True, False)),
    (FoodDelivery(), (False, True))
]

for service, args in services:
    service.deliver(*args)