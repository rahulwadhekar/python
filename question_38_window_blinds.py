class MotorJammedError(Exception):
    pass


class RollerBlind:
    def adjust(self, ok):
        try:
            if not ok:
                raise MotorJammedError
            print("RollerBlind: Moving up/down")
        except MotorJammedError:
            print("RollerBlind: Motor jammed")


class VenetianBlind:
    def adjust(self, ok):
        try:
            if not ok:
                raise MotorJammedError
            print("VenetianBlind: Rotating slats")
        except MotorJammedError:
            print("VenetianBlind: Motor jammed")


blinds = [(RollerBlind(), True), (VenetianBlind(), True), (RollerBlind(), False)]

for blind, status in blinds:
    blind.adjust(status)