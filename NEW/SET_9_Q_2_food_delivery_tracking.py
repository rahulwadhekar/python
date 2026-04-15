class RestaurantClosedError(Exception):
    pass


class Order:
    def estimated_delivery_time(self):
        pass


class StandardOrder(Order):
    def estimated_delivery_time(self, distance):
        return distance * 5


class ExpressOrder(Order):
    def estimated_delivery_time(self, hour):
        if hour > 23:
            raise RestaurantClosedError
        return 20


try:
    order = ExpressOrder()
    print(order.estimated_delivery_time(24))

except RestaurantClosedError:
    print("Restaurant closed! Come tomorrow.")