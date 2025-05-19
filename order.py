# order.py
class Order:
    def __init__(self, customer, coffee, price):
        # Validate customer
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        # Validate coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        # Validate price
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a float")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # Link order to coffee
        coffee.add_order(self)
        # Optionally, link order to customer if needed
        # But customer keeps track via create_order()

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price