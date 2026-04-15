class OutOfAmmoError(Exception):
    pass


class Sniper:
    def __init__(self, ammo):
        self.ammo = ammo

    def attack(self):
        try:
            if self.ammo == 0:
                raise OutOfAmmoError
            print("Sniper: 100 damage")
            self.ammo -= 1
        except OutOfAmmoError:
            print("Sniper: Reloading...")
            self.ammo = 5


class Medic:
    def attack(self):
        print("Medic: +50 HP")


players = [Sniper(0), Sniper(2), Medic()]

for p in players:
    p.attack()