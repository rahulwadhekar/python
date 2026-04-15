class DeviceOfflineError(Exception):
    pass


class SmartDevice:
    def __init__(self, status):
        self.status = status

    def operate(self):
        pass


class SmartLight(SmartDevice):
    def operate(self):
        if not self.status:
            raise DeviceOfflineError
        print("Light brightness adjusted")


class SmartThermostat(SmartDevice):
    def operate(self):
        if not self.status:
            raise DeviceOfflineError
        print("Temperature adjusted")


devices = [SmartLight(True), SmartThermostat(False)]

for d in devices:
    try:
        d.operate()
    except DeviceOfflineError:
        print("Device is offline")