class CriticalTemperatureError(Exception):
    pass


class Machine:
    def run_diagnostics(self):
        pass


class ConveyorBelt(Machine):
    def run_diagnostics(self, temp):
        if temp > 90:
            raise CriticalTemperatureError
        print("Conveyor: OK")


class PackagingArm(Machine):
    def run_diagnostics(self, temp):
        if temp > 90:
            raise CriticalTemperatureError
        print("Packaging Arm: OK")


try:
    m = ConveyorBelt()
    m.run_diagnostics(100)

except CriticalTemperatureError:
    print("Emergency Shutdown Triggered!")