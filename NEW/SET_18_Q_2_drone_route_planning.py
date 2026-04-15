class BatteryTooLowError(Exception):
    pass


class Drone:
    def plan_route(self, battery):
        pass


class LightweightDrone(Drone):
    def plan_route(self, battery):
        if battery < 30:
            raise BatteryTooLowError
        print("Direct aerial route")


class HeavyLiftDrone(Drone):
    def plan_route(self, battery):
        if battery < 50:
            raise BatteryTooLowError
        print("Commercial flight path")


try:
    d = LightweightDrone()
    d.plan_route(20)

except BatteryTooLowError:
    print("Reassigning to another drone")