#using getters and setters in python
'''
@class method --- to work with csv data, open,read from it, convert to list and instantiate from the lsit
@static method --- check input properties
@perporty  -----   make input parametrs private

@setters ----  set value
@atgetters ---  get value
'''
import csv
class Item:
    #class attributes
    pay_rate = 0.8 # payment after 20%dicsount
    all = []
    def __init__(self, name:str,price:float, quantity=0):
        #run validations for the received the price and quantity arguments

        assert price>=0 ,f"price {price} is not greater than or equal to zero"
        assert quantity>=0 ,f"quantity {quantity} is not greater than or equal to zero"

        #Assign the iput parameters to the self objects and make the name read-only
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)
        #property decorator = read-only attribute
        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            if(len(value)>10):
                raise Exception("The name is too long")
            else:
                self.__name = value

        def calculate_total_price(self):
            return self.price*self.quantity

        def apply_discount(self):
            self.price = self.price*self.pay_rate

        @classmethod
        def instantiate_from_csv(cls):
            #open file
            with open('item.csv','r') as f:
                #read opened file
                reader =csv.DictReader(f)
                #convert to list
                items = list(reader)
            #check the values
            for item in items:
                print(items)
            #instantiate from list
            for item in items:
                Item(name = item.get('name'),
                    price = item.get('price'),
                    quantity=item.get(quantity),
                    )
        @staticmethod
        def is_integer(num):
            #check whether the input argument is whether an int or float
            if isinstance(num, float):
                return num.is_integer()
            elif isinstance(num,int):
                return True
            else:
                return False

        def __repr__(self):
            return f"{self.__class.__name__}('{name}','{price}','{quantity}'"
