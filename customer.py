

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter    
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters long")
        self._name = value

    def orders(self):
       
        from order import Order 
        return [order for order in Order._all_orders if order.customer == self]
            
    def coffees(self):
        
        from coffee import Coffee 
       
        from order import Order
        return list({order.coffee for order in self.orders()})
            
    def create_order(self, coffee, price):
        
        from order import Order 
        order = Order(self, coffee, price)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
       
        from coffee import Coffee 
       
        from order import Order
        
      
        if not isinstance(coffee, Coffee):
             raise TypeError("Provided object must be a Coffee instance.")

        customer_spending = {}
        for order in coffee.orders(): 
            customer = order.customer
            price = order.price
            customer_spending[customer] = customer_spending.get(customer, 0) + price
        
        if not customer_spending:
            return None
        
        most_spent_customer = max(customer_spending, key=customer_spending.get)
        return most_spent_customer

    def __repr__(self):
        return f"<Customer Name: {self.name}>"