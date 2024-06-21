import datetime
class Flight:

    def __init__(self, from_where, to_where, time, reis, ticket):
        self.from_where = from_where
        self.to_where = to_where
        self.time = time
        self.reis = reis
        self.ticket = ticket

cholpon = Flight("New York", "Los Angeles", datetime.datetime(2024, 7, 1, 8, 30), "AA123", f"{350}$")
alisher = Flight("London", "Paris", datetime.datetime(2024, 7, 2, 10, 15), "BA456", f"{200}$")
guzelia = Flight("Tokyo", "Sydney", datetime.datetime(2024, 7, 3, 14, 0), "JL789", f"{300}$")

print(cholpon.from_where, cholpon.to_where, cholpon.time, cholpon.reis, cholpon.ticket)
print(alisher.from_where, alisher.to_where, alisher.time, alisher.reis, alisher.ticket)
print(guzelia.from_where, guzelia.to_where, guzelia.time, guzelia.reis, guzelia.ticket)
