#Using python classes

class Item:
    #Constructor
    def __init__(self, name:str,price:float, quantity=0 ):
        # print(f'An instance created for a {name}')
        #run validation to the received arguments
        assert price >=0, f"price {price} is not greater than or eqaul to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        #Assign to the self object dynamically
        self.name = name
        self.price  = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price *self.quantity

#Create instances of the class object

item1 = Item('Phone',100.0,5)
item2 = Item('Laptop',1000.0,3)

#Call class methods on class objects

print(item1.calculate_total_price())
print(item2.calculate_total_price())
