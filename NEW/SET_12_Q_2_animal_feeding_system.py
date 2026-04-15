class OverfeedingError(Exception):
    pass


class Animal:
    def feed(self, qty):
        pass


class Carnivore(Animal):
    def feed(self, qty):
        if qty > 10:
            raise OverfeedingError
        print("Fed meat:", qty)


class Herbivore(Animal):
    def feed(self, qty):
        if qty > 20:
            raise OverfeedingError
        print("Fed plants:", qty)


try:
    a = Carnivore()
    a.feed(15)

except OverfeedingError:
    print("Warning: Overfeeding detected")