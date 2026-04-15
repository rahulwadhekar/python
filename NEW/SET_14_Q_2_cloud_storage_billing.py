class StorageQuotaExceededError(Exception):
    pass


class CloudStorage:
    def calculate_bill(self, data):
        pass


class StandardTier(CloudStorage):
    def calculate_bill(self, data):
        if data > 100:
            raise StorageQuotaExceededError
        return data * 10


class EnterpriseTier(CloudStorage):
    def calculate_bill(self, data):
        if data <= 1000:
            return 5000
        return 5000 + (data - 1000) * 5


try:
    s = StandardTier()
    print(s.calculate_bill(150))

except StorageQuotaExceededError:
    print("Storage limit exceeded")