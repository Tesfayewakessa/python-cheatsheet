#Using tuples to manipuate data in python

'''
Similar to lists, tuples are another compound data types.
Tuples are  containers that are written as a list of comma separated items/values between paranthesis

Tuples are immutable-----meaning that the items can not be changed. However, a tuples can contain mutable objects
Tuples play like a sort of struct in python----- a wayto pass a little logical, fixed size bundle of values
Tuple has two methods available
count()     Returns the number of times the elements with a specified value appears in the tuple
index()     Returns the index fof the first element with specified value


How operators + and * are used in tuple
'''

#Basic command--tuple packing
#create an empty tuple
empty = ()
print(empty)

#create a tuple with numbers, notation without paranthesis 
x = 1,2,3,4 #tuple containing (1,2,3,4)

# create a tuple with different data type

y = x,False,5,'hello',True,'there'# nested type

y

#trailling comma for creating a tuple of one item
singleton = 'world', # singleton = 'world' makes singleton a string but singleton = 'world', makes singleton a tuple because of the trailing comma

# size of a tuple
len(empty)

len(singleton)

singleton
#Create a tuple from an iterable objects like list
# tuples are immutable but they can contain multiple mutable objects
z = [1,'a',2,'b'],[3,'d',4,'e',5,'f'],[True, False]
print(z)

#indexing ----- used to get item of a tuple
'''
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 | E | T | H | I | O | P | I | A | N |   | C | O | D | E | R | 
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
-16                             -8   -7  -6  -5  -4  -3  -2  -1

'''

item1 = z[0] # returns the item at index zero

print(item1)

#Check whether an element exis in tuple or not
print("a" in z)
print("b",5 in z)
print([1,'a',2,'b'] in z,[3,'d',4,'e',5,'f'] in z )


#converting list to tuple
tuplea = tuple(z[0])
print(tuplea)


#unpacking a tuple in several variables
#The number of variables must be equal to the number of items in a tuple

a1, b1, c1 = z
a1
b1
c1
print(a1 + b1 + c1) #[1, 'a', 2, 'b', 3, 'd', 4, 'e', 5, 'f', True, False] 

# built-in function tuple()
w = tuple(['1',2,3,'a'])# it only takes one argument which iterable
w
#create an empty tuple()
tuplex = tuple()
print(tuplex)

#Adding item in python tuple. Tuples are immutable. So, we can not add elements using indexing
#insead, we have to se merge of tuples using the + operater. i.e add a tuple to a tuple using + operator
tupley = z + w

print(tupley) #([1, 'a', 2, 'b'], [3, 'd', 4, 'e', 5, 'f'], [True, False], '1', 2, 3, 'a')

tuplez = 1,2,3,4,5,6,7
tuplez = tuplez[2:] + tuplez + tuplez[2:]
print(tuplez) #(3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7)

#Converting list to tuple
listz = list(tuplez)

listz.append(8)

#Convert back to tuple

tuplez = tuple(listz)
print(tuplez) #(3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8)

#Cloning a tuple --- creating a copy of the tuple and modify it without affecting the base tuple

from copy import deepcopy
#create a tuple
tupleb = ("HELLO", 5, [], True) 
print(tupleb)# ('HELLO', 5, [], True)
#make a copy of a tuple using deepcopy() function
tupleb_copy = deepcopy(tupleb)
tupleb_copy[2].append(50)
print(tupleb_copy)# ('HELLO', 5, [50], True)
print(tupleb) #('HELLO', 5, [], True)



#tuple comprehension ---uses same approach as list comprehension
u = tuple([x**2 for x in range(10)])
u
#named tuple

from collections import namedtuple
Point  = namedtuple('point','x y')

p = Point(1,2)# Point(x = 1, y = 2) Point(1, y = 2) Point(x = 1, 2)
p[0]
p[1]
p.x
p.y
p._fields # Point._field


#counting the number of times an item appears in a list
tuplec = 2,4,6,7,9,0,12,23,2,4,6
cnt = tuplec.count(4) #If the value passed is not in the tuple, 0 is returned

#remove an item from a tuple

# two approaches to remove an item from a tuple
#approach 1  ---------- convert the tuple to list and use remove method
listc = list(tuplec)
listc.remove(0)
print(listc)
tuplec = tuple(listc)
print(tuplec)

#Approach 2 use the + operator with index

tuplec = tuplec[:5] + tuplec[6:]
print(tuplec)

#getting the index of an item in a list
#use the method index()

tuplec.index(23) # Returns at what index position the value is in the tuple. In this case 5


#How operators + and * are used in tuple
# + operator joins two or tuples together
tuplec = tuplec[:5] + tuplec[6:] + tuplec[:5] + tuplec[6:] 

# * operator repeats the item in the tuple
tup = 5,
tup = tup*5 #(5, 5, 5, 5, 5)
print(tup)
# example
e = ("x",)
n = 2
for i in range(n):
    e = (e,)
    print(x)

x = (2,3)
y = (4,5)

z = x + y # + operator

# built-in function 
print(max(z))
z = sum(z,1) #15 It all all the elments of the the tuple first and adds 1 to it

numberGmaes = {}
numberGmaes[(2,4,6)] = 14
numberGmaes[(6,4,2)] = 16
numberGmaes[(2,4)] = 18

sum = 0

for x in numberGmaes:
    sum+=numberGmaes[x]

print(len(numberGmaes) + sum) #51

