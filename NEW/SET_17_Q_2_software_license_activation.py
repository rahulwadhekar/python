class MaxActivationsReachedError(Exception):
    pass


class License:
    def activate_software(self):
        pass


class SingleUserLicense(License):
    def __init__(self):
        self.count = 0

    def activate_software(self):
        if self.count >= 1:
            raise MaxActivationsReachedError
        self.count += 1
        print("Activated for single user")


class CorporateLicense(License):
    def __init__(self):
        self.count = 0

    def activate_software(self):
        if self.count >= 10:
            raise MaxActivationsReachedError
        self.count += 10
        print("Activated for 10 users")


try:
    lic = SingleUserLicense()
    lic.activate_software()
    lic.activate_software()

except MaxActivationsReachedError:
    print("Activation limit reached!")