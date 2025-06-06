# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Hilda")
customer2 = Customer("tinah")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

Order(customer1, coffee1, 4.0)  # Order 1: Hilda buys Latte @ 4.0
Order(customer2, coffee1, 5.0)  # Order 2: tinah buys Latte @ 5.0
Order(customer1, coffee2, 4.5)  # Order 3: Hilda buys Espresso @ 4.5

print(f"Customer 1: {customer1.name}")
print(f"{coffee1.name} Customers:", [c.name for c in coffee1.customers()])
print(f"{coffee1.name} Num Orders:", coffee1.num_orders())