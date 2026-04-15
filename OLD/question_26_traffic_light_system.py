class SensorFailureError(Exception):
    pass


class VehicleLight:
    def change_state(self, sensor_ok):
        try:
            if not sensor_ok:
                raise SensorFailureError
            print("VehicleLight: Green → Yellow → Red")
        except SensorFailureError:
            print("VehicleLight: Blinking Yellow")


class PedestrianLight:
    def change_state(self, sensor_ok):
        try:
            if not sensor_ok:
                raise SensorFailureError
            print("PedestrianLight: Walk → Don't Walk")
        except SensorFailureError:
            print("PedestrianLight: Blinking Yellow")


lights = [(VehicleLight(), True), (PedestrianLight(), True), (VehicleLight(), False)]

for light, status in lights:
    light.change_state(status)