class OutOfAmmoError(Exception):
    pass


class Player:
    def attack(self):
        pass


class Sniper(Player):
    def __init__(self, ammo):
        self.ammo = ammo

    def attack(self):
        try:
            if self.ammo == 0:
                raise OutOfAmmoError
            print("Sniper: 100 damage")
            self.ammo -= 1
        except OutOfAmmoError:
            print("Reloading...")


class Medic(Player):
    def attack(self):
        print("Medic: Heal +50")


players = [Sniper(0), Medic()]

for p in players:
    p.attack()