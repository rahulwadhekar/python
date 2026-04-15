class IntruderAlertError(Exception):
    pass


class BiometricLock:
    def unlock(self, match):
        if match:
            print("Unlocked")
        else:
            print("Access Denied")


class PinLock:
    def __init__(self):
        self.correct_pin = "1234"
        self.attempts = 0

    def unlock(self, pin):
        try:
            if pin == self.correct_pin:
                print("Unlocked")
                self.attempts = 0
            else:
                self.attempts += 1
                print("Wrong PIN")

                if self.attempts == 3:
                    raise IntruderAlertError
        except IntruderAlertError:
            print("🚨 Alarm Triggered!")


bio = BiometricLock()
pin = PinLock()

bio.unlock(True)
pin.unlock("1111")
pin.unlock("2222")
pin.unlock("3333")