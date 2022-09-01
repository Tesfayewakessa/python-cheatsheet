#Ingheriting class
from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0,broken_phones = 0):
        super().__init__(name, price, quantity)

    #run validation on the received arguments
        assert broken_phones >=0, f"Broken_phones {broken_phones} are not greater than or equal to zero!"
        #Assign to self object
        self.broken_phones = broken_phones