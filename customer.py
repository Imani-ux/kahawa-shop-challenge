class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be a string.")
        if not 1 <= len(name) <= 15:
            raise ValueError("Customer name must be between 1 and 15 characters long.")
        self._name = name
        self._orders = []  # Store orders for this customer

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not 1 <= len(value) <= 15:
            raise ValueError("Customer name must be between 1 and 15 characters long.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))  # Unique coffees

    def create_order(self, coffee, price):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance.")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")

        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)  
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        from order import Order
        customer_spending = {}
        for order in coffee.orders():
            if order.customer not in customer_spending:
                customer_spending[order.customer] = 0
            customer_spending[order.customer] += order.price

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)