class PayloadTooHeavyError(Exception):
    pass


class Quadcopter:
    def takeoff(self, weight):
        try:
            if weight > 2:
                raise PayloadTooHeavyError
            print("Quadcopter flying with weight:", weight)
        except PayloadTooHeavyError:
            print("Quadcopter: Payload too heavy!")


class Octocopter:
    def takeoff(self, weight):
        try:
            if weight > 10:
                raise PayloadTooHeavyError
            print("Octocopter flying with weight:", weight)
        except PayloadTooHeavyError:
            print("Octocopter: Payload too heavy!")


drones = [(Quadcopter(), 1), (Quadcopter(), 3), (Octocopter(), 8), (Octocopter(), 12)]

for drone, weight in drones:
    drone.takeoff(weight)