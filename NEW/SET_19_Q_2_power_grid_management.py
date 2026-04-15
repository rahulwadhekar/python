class GridOverloadError(Exception):
    pass


class PowerSource:
    def generate_power(self, condition):
        pass


class SolarPanel(PowerSource):
    def generate_power(self, condition):
        return 5000 if condition == "Sunny" else 0


class WindTurbine(PowerSource):
    def generate_power(self, condition):
        return 6000 if condition == "Stormy" else 2000


try:
    s = SolarPanel().generate_power("Sunny")
    w = WindTurbine().generate_power("Stormy")

    total = s + w
    if total > 10000:
        raise GridOverloadError

    print("Total Power:", total)

except GridOverloadError:
    print("Grid overload! Disconnecting sources")