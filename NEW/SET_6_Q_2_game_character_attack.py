class ManaDepletedError(Exception):
    pass


class Character:
    def special_attack(self):
        pass


class Mage(Character):
    def __init__(self, mana):
        self.mana = mana

    def special_attack(self):
        try:
            if self.mana < 50:
                raise ManaDepletedError
            self.mana -= 50
            print("Mage: Heavy damage")
        except ManaDepletedError:
            print("Mage: Normal attack")


class Warrior(Character):
    def __init__(self, mana):
        self.mana = mana

    def special_attack(self):
        try:
            if self.mana < 20:
                raise ManaDepletedError
            self.mana -= 20
            print("Warrior: Stun attack")
        except ManaDepletedError:
            print("Warrior: Normal attack")


players = [Mage(40), Warrior(10)]

for p in players:
    p.special_attack()