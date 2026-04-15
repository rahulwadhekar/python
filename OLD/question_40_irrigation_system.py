class WaterPressureLowError(Exception):
    pass


class DripIrrigation:
    def water(self, pressure):
        try:
            if pressure < 20:
                raise WaterPressureLowError
            print("DripIrrigation: Slow watering")
        except WaterPressureLowError:
            print("System shutdown: Low pressure")


class RotarySprinkler:
    def water(self, pressure):
        try:
            if pressure < 20:
                raise WaterPressureLowError
            print("RotarySprinkler: Wide spray")
        except WaterPressureLowError:
            print("System shutdown: Low pressure")


systems = [(DripIrrigation(), 30), (RotarySprinkler(), 30), (DripIrrigation(), 10)]

for system, pressure in systems:
    system.water(pressure)