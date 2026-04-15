class ShiftLimitExceededError(Exception):
    pass


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        pass


class Doctor(Employee):
    def calculate_salary(self):
        base = 50000
        surgeries = int(input("Enter surgeries: "))
        return base + surgeries * 2000


class Nurse(Employee):
    def calculate_salary(self):
        base = 30000
        overtime = int(input("Enter overtime hours: "))
        if overtime > 20:
            raise ShiftLimitExceededError
        return base + overtime * 500


try:
    d = Doctor("Rahul", 1)
    print("Doctor Salary:", d.calculate_salary())

    n = Nurse("Riya", 2)
    print("Nurse Salary:", n.calculate_salary())

except ShiftLimitExceededError:
    print("Error: Overtime exceeded!")