class DriverUnavailableError(Exception):
    pass


class Ride:
    def calculate_fare(self, distance):
        pass


class StandardRide(Ride):
    def calculate_fare(self, distance):
        return 50 + distance * 10


class PremiumRide(Ride):
    def calculate_fare(self, distance):
        if distance > 100:
            raise DriverUnavailableError
        return 100 + distance * 20


try:
    ride = PremiumRide()
    print("Fare:", ride.calculate_fare(120))

except DriverUnavailableError:
    print("Driver unavailable for long distance")