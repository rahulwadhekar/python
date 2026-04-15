class DoNotDisturbError(Exception):
    pass


class RoomService:
    def deliver(self):
        pass


class CleaningService(RoomService):
    def deliver(self, empty, dnd):
        if dnd:
            raise DoNotDisturbError
        print("Cleaning done" if empty else "Room not empty")


class FoodDelivery(RoomService):
    def deliver(self, present, dnd):
        if dnd:
            raise DoNotDisturbError
        print("Food delivered" if present else "Guest not present")


try:
    s = CleaningService()
    s.deliver(True, True)

except DoNotDisturbError:
    print("Service rescheduled")