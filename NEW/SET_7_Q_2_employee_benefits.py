class InvalidHoursError(Exception):
    pass


class Worker:
    def calculate_benefits(self):
        pass


class FullTimeWorker(Worker):
    def calculate_benefits(self):
        print("Benefits: Health Insurance + Paid Leave")


class PartTimeWorker(Worker):
    def calculate_benefits(self, hours):
        if hours < 0 or hours > 168:
            raise InvalidHoursError
        print("Benefits: ₹", hours * 100)


try:
    f = FullTimeWorker()
    f.calculate_benefits()

    p = PartTimeWorker()
    p.calculate_benefits(180)

except InvalidHoursError:
    print("Invalid working hours entered!")