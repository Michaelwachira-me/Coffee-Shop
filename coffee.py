

class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value    

    def orders(self):
        
        from order import Order 
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
       
        from customer import Customer
        
        from order import Order
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        coffee_orders = self.orders() 
        if not coffee_orders:
            return 0.0
        return sum(order.price for order in coffee_orders) / len(coffee_orders)

    def __repr__(self):
        return f"<Coffee Name: {self.name}>"