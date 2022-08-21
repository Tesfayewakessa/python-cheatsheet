#Python classes

'''
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object,
allowing new instances of that type to be made.

Python classes provide all the standard features of Object-Oriented Programming.
Class inheritance allows multiple bases classes to inherit from one another.
A drived class inherits from base/parent class an doverride any methods of it base class/classes, a method can call the method of
a base class with the same name


Simplest form of class definition looks like thsi
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-n>

Class definitions, like function definitions (def statements) must be executed before they have any effect

''' 
#The basics
from telnetlib import DO


class MyClass:
    '''
    Class attributes--- variables directly defined within the class. These attributes are equally shared by all objects of the class
    '''
    i = 12345 #class attribute
    
    def f(self):
        return 'Hello world!'

#using the class
MyClass.i # retrns the int
MyClass.f # returns the function f object
MyClass.__doc__ #magic/dunder method that returns the text literal

#instantiate the class
x = MyClass()
x.i # returns an int
x.f() # returns the class method

'''
Notice how self is passed as the first arg!!!!
We pass the methods instance object self as the first arg!

so x.f() is equivalent to MyClass.f(x)
'''

'''
Class with special initiial state - we use __init__
Allows us to pass args to class for greater flexibility
'''
class Myclass:
    #pass
    #class attributes that could be globally used through out the class
    #define __init__ method
    def __init__(self,int1): #int1 is the parameter
        self.int1 = int1 #variable = parameter
    
    def f(self):
        new = self.int1*3
        return new
#Create instance of the class
x = Myclass(4)
x.int1 #returns the int
x.f()  # returns the class method

#Instance objects------> we can and delete attributes to our object
x.counter = 1 # add an atribute and assign value
while x.counter < 10:
    x.counter*=2
print(x.counter)

del x.counter # delete the data attributes

#Class and Instance Variables

class Dog:
    '''
    This dog class will get the name  and adds the tricks the dogs can play
    '''
    kind = 'canine' # class variable shared by all instances
    def __init__(self,name):
        self.name = name # instance variable that is unique to each instance
        self.tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)


dog1 = Dog('Fido')
dog2 = Dog('Buddy')
dog1.kind
dog1.add_trick('HighJump')
dog1.add_trick('Sniffing')
dog1.name

dog1.tricks

#Inheritance
'''
class DrivedClassName(Base1, Base2,....):
    <statement-1>
    .
    .
    .
    <statement-n>

Execution of a drived class definition proceeds the same as for a base class. When a class object is constructed, the base class is remembered.
This is used for resolving attribute references: if a requested attribute is not found in the class, the search  proceeds to look in the base class.
This rule is applieed recursively if the base class itself is derived from other class

'''
class Mapping:
    '''
    private variable example within inherited class
    checkout __update ----this is called name mangling
    Is done without regard to syntactical position

    '''
    def __init__(self, iterable):
        self.iterable = iterable
        self.items_list = []
    def update(self):
        for item in self.iterable:
            self.items_list.append(item)
#inheriting class
class MappingSubClass(Mapping):
    def update(self, keys, values):#provide new signiture for update method
        for item in zip(keys,values):
            self.items_list.append(item)

m = MappingSubClass([1,2,3,4])
m.items_list
m.update(["one","two","three"], ["these", "are", "values"])
m.items_list

