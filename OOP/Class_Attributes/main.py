#Using class attributes
#self is the instance inself that we get every time a new instance is created
class Item():
    '''
    #class attributes

    '''
    #class attributes
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        assert price >=0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quanity {quantity} is not greater than or equal to zero"

        #Assigning to the self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) # Append to the list defined at class level every time a new item is added

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price*self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7 # Modifies the pay_rate at instance level
item2.apply_discount()
print(item2.price)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#we can get the name of all the items added to the list 
for instance in Item.all:
    print(instance.name)

print(Item.all)

#print(Item.__dict__) #Returns all the attributes for class level
# print(item1.__dict__) # Returns all the attributes for instance level