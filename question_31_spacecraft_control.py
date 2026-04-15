class FuelLineLeakError(Exception):
    pass


class MainEngine:
    def ignite(self, ok):
        try:
            if not ok:
                raise FuelLineLeakError
            print("MainEngine: Ignited (liquid fuel)")
        except FuelLineLeakError:
            print("Leak detected! Engine shutdown.")


class ManeuveringJet:
    def ignite(self, ok):
        try:
            if not ok:
                raise FuelLineLeakError
            print("ManeuveringJet: Ignited (gas)")
        except FuelLineLeakError:
            print("Leak detected! Engine shutdown.")


systems = [(MainEngine(), True), (ManeuveringJet(), True), (MainEngine(), False)]

for system, status in systems:
    system.ignite(status)