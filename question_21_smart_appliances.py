class DoorOpenError(Exception):
    pass


class WashingMachine:
    def __init__(self, door_closed):
        self.door_closed = door_closed

    def start_cycle(self):
        try:
            if not self.door_closed:
                raise DoorOpenError
            print("WashingMachine: Running cycle")
        except DoorOpenError:
            print("Error: Door is open!")


class Refrigerator:
    def start_cycle(self, temp):
        if temp > 5:
            print("Refrigerator: High cooling")
        else:
            print("Refrigerator: Normal cooling")


devices = [WashingMachine(False), WashingMachine(True), Refrigerator()]

for device in devices:
    try:
        device.start_cycle(8)
    except TypeError:
        device.start_cycle()