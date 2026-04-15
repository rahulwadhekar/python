class MembershipExpiredError(Exception):
    pass


class GymMember:
    def check_access(self):
        pass


class MonthlyMember(GymMember):
    def check_access(self, valid):
        if not valid:
            raise MembershipExpiredError
        print("Access during off-peak hours")


class AnnualVIPMember(GymMember):
    def check_access(self, valid):
        if not valid:
            raise MembershipExpiredError
        print("24/7 Access Granted")


try:
    m = MonthlyMember()
    m.check_access(False)

except MembershipExpiredError:
    print("Membership expired, please renew")