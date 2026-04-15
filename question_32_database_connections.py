class ConnectionTimeoutError(Exception):
    pass


class SQLDB:
    def connect(self, time_ms):
        try:
            if time_ms > 5000:
                raise ConnectionTimeoutError
            print("SQLDB: Connected successfully")
        except ConnectionTimeoutError:
            print("SQLDB: Timeout! Retrying...")


class NoSQLDB:
    def connect(self, time_ms):
        try:
            if time_ms > 5000:
                raise ConnectionTimeoutError
            print("NoSQLDB: Connected successfully")
        except ConnectionTimeoutError:
            print("NoSQLDB: Timeout! Retrying...")


dbs = [(SQLDB(), 3000), (NoSQLDB(), 6000)]

for db, t in dbs:
    db.connect(t)