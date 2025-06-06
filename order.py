

class Order:
    _all_orders = [] 

    def __init__(self, customer, coffee, price):
        
        from customer import Customer 
        from coffee import Coffee     
      
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class.")
        
       
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class.")
        
       
        if not (isinstance(price, float) or isinstance(price, int)):
            raise TypeError("Price must be a float or int.")
        float_price = float(price) 
        if not (1.0 <= float_price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = float_price 
        
        Order._all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
       
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
       
        from coffee import Coffee 
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("Price must be a float or int.")
        float_value = float(value) 
        if not (1.0 <= float_value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = float_value

    def __repr__(self):
        return f"<Order Customer: {self.customer.name}, Coffee: {self.coffee.name}, Price: {self.price:.2f}>"