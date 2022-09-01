import csv

class Item:
    #class attributes
    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    #contructor
    def __init__(self,name:str,price:float,quanity=0):
        #run validation on the received arguments
        assert price >=0, f"Price {price} ia not greater than or equal to zero"
        assert quanity >=0, f"Quantity {quanity} is not greater than or equal to zero"

        #Assign to self object
        self.name = name
        self.quantity = quanity
        self.price = price

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate

    @classmethod#canonly be accessed from class level only
    def instantiate_from_csv(cls):
        with open('D:\AGV_Bot\OOP\ClassVsStaticMethods\codesnippets\items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        #print out the content
        # for item in items:
            # print(item)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quanity=int(item.get('quantity')),
                )

    @staticmethod
    def is_integer(num):
        #for instance count out the floats that are point zero, like 5.0, 10.0
        if isinstance(num, float):
            #count out the floats
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
#access class methods
# Item.instantiate_from_csv()
# print(Item.all)

#Accessing a static method
print(Item.is_integer(12))