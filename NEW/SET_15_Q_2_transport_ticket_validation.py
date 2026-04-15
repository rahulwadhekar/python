class InvalidZoneError(Exception):
    pass


class Ticket:
    def validate_ticket(self, zone):
        pass


class BusTicket(Ticket):
    def validate_ticket(self, zone):
        print("Valid for all zones")


class TrainTicket(Ticket):
    def __init__(self, valid_zone):
        self.valid_zone = valid_zone

    def validate_ticket(self, zone):
        if zone != self.valid_zone:
            raise InvalidZoneError
        print("Valid ticket")


try:
    t = TrainTicket(2)
    t.validate_ticket(3)

except InvalidZoneError:
    print("Invalid zone! Pay surcharge")