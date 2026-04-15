class MaximumFineExceededError(Exception):
    pass


class MediaItem:
    def calculate_late_fee(self, days):
        pass


class Book(MediaItem):
    def calculate_late_fee(self, days):
        fine = days * 5
        if fine > 500:
            raise MaximumFineExceededError
        return fine


class DVD(MediaItem):
    def calculate_late_fee(self, days):
        fine = days * 20
        if fine > 500:
            raise MaximumFineExceededError
        return fine


try:
    b = Book()
    print("Book Fine:", b.calculate_late_fee(50))

except MaximumFineExceededError:
    print("Fine exceeds limit, capped at item price")