class DoorOpenError(Exception):
    pass


class Appliance:
    def start_cycle(self):
        pass


class WashingMachine(Appliance):
    def __init__(self, door_closed):
        self.door_closed = door_closed

    def start_cycle(self):
        if not self.door_closed:
            raise DoorOpenError
        print("Washing Machine: Started")


class Refrigerator(Appliance):
    def start_cycle(self):
        print("Refrigerator: Cooling adjusted")


try:
    wm = WashingMachine(False)
    wm.start_cycle()

except DoorOpenError:
    print("Error: Door is open!")