class PayloadTooHeavyError(Exception):
    pass


class DeliveryVehicle:
    def takeoff(self, weight):
        pass


class Quadcopter(DeliveryVehicle):
    def takeoff(self, weight):
        if weight > 2:
            raise PayloadTooHeavyError
        print("Quadcopter flying")


class Octocopter(DeliveryVehicle):
    def takeoff(self, weight):
        if weight > 10:
            raise PayloadTooHeavyError
        print("Octocopter flying")


try:
    d = Quadcopter()
    d.takeoff(5)

except PayloadTooHeavyError:
    print("Too heavy! Manual handling required")