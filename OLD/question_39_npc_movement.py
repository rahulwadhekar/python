class PathBlockedError(Exception):
    pass


class Merchant:
    def move(self, ok):
        try:
            if not ok:
                raise PathBlockedError
            print("Merchant: Moving safely")
        except PathBlockedError:
            print("Merchant: Waiting, path blocked")


class Enemy:
    def move(self, ok):
        try:
            if not ok:
                raise PathBlockedError
            print("Enemy: Chasing player")
        except PathBlockedError:
            print("Enemy: Waiting, path blocked")


npcs = [(Merchant(), True), (Enemy(), True), (Enemy(), False)]

for npc, status in npcs:
    npc.move(status)