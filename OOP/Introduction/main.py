#A breif intro to an item class
class item:
    '''
    Store management system
    things the class could do:
            track the items we have in our store
            Create a variable to start tracking our items
            Calculate total price
    '''
    def calculate_total_price(self,x,y):
        return x*y

#how to create an instance of a class
item1 =  item()

#Assign attributes
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

#Calling methods from instances of a class
print(item1.calculate_total_price(item1.price, item1.quantity))

#How to create an instance of a class. We could create as much instance as we would like to
item2 = item()

#Assign attributes
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3

#Calling methods from instances of a class

print(item2.calculate_total_price(item2.price, item2.quantity))