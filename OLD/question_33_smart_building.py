class FilterCloggedError(Exception):
    pass


class Heater:
    def regulate_temp(self, temp, airflow_ok):
        try:
            if not airflow_ok:
                raise FilterCloggedError
            print("Heater ON" if temp < 18 else "Heater OFF")
        except FilterCloggedError:
            print("Heater: Maintenance required")


class AC:
    def regulate_temp(self, temp, airflow_ok):
        try:
            if not airflow_ok:
                raise FilterCloggedError
            print("AC ON" if temp > 24 else "AC OFF")
        except FilterCloggedError:
            print("AC: Maintenance required")


devices = [(Heater(), 15, True), (AC(), 26, True), (AC(), 25, False)]

for device, temp, airflow in devices:
    device.regulate_temp(temp, airflow)