class IntruderAlertError(Exception):
    pass


class Lock:
    def unlock(self):
        pass


class BiometricLock(Lock):
    def unlock(self, match):
        print("Unlocked" if match else "Access Denied")


class PinLock(Lock):
    def __init__(self):
        self.pin = "1234"
        self.count = 0

    def unlock(self, input_pin):
        if input_pin == self.pin:
            print("Unlocked")
            self.count = 0
        else:
            self.count += 1
            print("Wrong PIN")
            if self.count == 3:
                raise IntruderAlertError


try:
    p = PinLock()
    p.unlock("1111")
    p.unlock("2222")
    p.unlock("3333")

except IntruderAlertError:
    print("🚨 Alarm Triggered!")