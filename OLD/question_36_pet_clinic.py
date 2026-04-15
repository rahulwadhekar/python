class VaccinationOverdueError(Exception):
    pass


class Dog:
    def schedule_appointment(self, years):
        try:
            if years > 2:
                raise VaccinationOverdueError
            print("Dog: Vaccination scheduled")
        except VaccinationOverdueError:
            print("Dog: High priority (overdue)")


class Cat:
    def schedule_appointment(self, years):
        try:
            if years > 2:
                raise VaccinationOverdueError
            print("Cat: Vaccination scheduled")
        except VaccinationOverdueError:
            print("Cat: High priority (overdue)")


pets = [(Dog(), 1), (Cat(), 3), (Dog(), 4)]

for pet, years in pets:
    pet.schedule_appointment(years)