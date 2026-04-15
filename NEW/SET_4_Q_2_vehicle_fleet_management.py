class RouteTooLongError(Exception):
    pass


class Vehicle:
    def calculate_fuel_efficiency(self):
        pass


class Truck(Vehicle):
    def calculate_fuel_efficiency(self, weight):
        return 10 - (weight * 0.1)


class DeliveryVan(Vehicle):
    def calculate_fuel_efficiency(self, stops):
        return 15 - (stops * 0.2)


try:
    truck = Truck()
    distance = 500
    if distance > 400:
        raise RouteTooLongError
    print("Truck Efficiency:", truck.calculate_fuel_efficiency(20))

except RouteTooLongError:
    print("Route too long! Assigning fallback vehicle.")