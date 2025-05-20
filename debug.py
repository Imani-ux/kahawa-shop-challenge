from customer import Customer
from coffee import Coffee
from order import Order


customer1 = Customer("Asha")
customer2 = Customer("Imani")
coffee1 = Coffee("Kahawa")
coffee2 = Coffee("black-kahawa")


order1 = customer1.create_order(coffee1, 5.50)
order2 = customer1.create_order(coffee2, 4.00)
order3 = customer2.create_order(coffee1, 6.00)


print(f"Asha's orders: {customer1.orders()}")
print(f"Imani's coffees: {customer2.coffees()}")
print(f"Espresso's customers: {coffee1.customers()}")


print(f"Espresso's total orders: {coffee1.num_orders()}")
print(f"Latte's average price: {coffee2.average_price()}")


most_aficionado = Customer.most_aficionado(coffee1)
if most_aficionado:
    print(f"Most aficionado of Espresso: {most_aficionado.name}")
else:
    print("No orders for Espresso yet.")