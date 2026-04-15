class SensorFailureError(Exception):
    pass


class TrafficLight:
    def change_state(self):
        pass


class VehicleLight(TrafficLight):
    def change_state(self, sensor_ok):
        if not sensor_ok:
            raise SensorFailureError
        print("Vehicle: Green → Yellow → Red")


class PedestrianLight(TrafficLight):
    def change_state(self, sensor_ok):
        if not sensor_ok:
            raise SensorFailureError
        print("Pedestrian: Walk → Don't Walk")


try:
    light = VehicleLight()
    light.change_state(False)

except SensorFailureError:
    print("Blinking Yellow Mode Activated")