#using python to manipulate lists
'''
Python knows a number of compound data types that are use to store or group together values

Amoung compound adta types, list is is the most versatile


lists are written as comma separated values or items between square brackets

lists are mutable. That means, the items are can be changed

lists have a bunch of available methods

append()        addes an element at the end of the list
clear()         removes all the elements of a list
copy()          returns a copy of the list
count()         retruns the number of elements with the specified value
extend()        all the elements of a list or any iterable to the end of the current list
index()         returns the index of the first element with the specified value
insert()        adds an element at the specified position 
pop()           removes the element at the specified position and returns the removed value
remove()        removes the first item with the specified value
reverse()       reverses the order of the list
sort()          sorts the list

'''
# basic example

squares = [1,4,9,16,25]
squares
squares.pop() #removes and returns 25

assert(squares == squares.copy())

squares.append(49)
squares

squares.append(36)
squares
squares.sort()
squares
squares.insert(2,"Apple") #inserts a string apple at the third position
from collections import Counter
numElementCount = Counter(squares)# returns a dictionary
numElementCount
#get the count for each element
numElementCount[1]
#get most common item as follows
most_common = numElementCount.most_common()
most_common #[(1, 1), (4, 1), (9, 1), (16, 1), (25, 1)]
most_common[0] #(1, 1)
most_common[0][1] # 1
#remove an element at position 3
squares.remove("apple")
squares.sort(key=None, reverse=False)
squares.reverse()

#indexing
'''
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 | E | T | H | I | O | P | I | A | N |   | C | O | D | E | R | 
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
-16                             -8   -7  -6  -5  -4  -3  -2  -1

'''
#indexing returns the item or value

squares[0]
squares[-1]
squares[-3:]
#using [::] first: is for start, second : is for stop
squares[::]
# create a copy of a list
squares[:]
assert(squares[:]==squares.copy())

#concatination or glueing together

squares + squares[:] + squares.copy()
squares

#modifying or altering items

cubes = [1,8,27,65,125] # 65 was supposed to be 64 as 4 ** 3  
#inserting element using indexing
cubes[3] = 64
cubes
#list methods 

cubes.append(216) #adds the cube of 6

cubes

len(cubes)

#list of strings

words = ['ab','cde','fghi','jklmn']
len(words)

#list nesting

a = [squares,cubes,words] # [[1, 4, 9, 16, 36, 49], [1, 8, 27, 64, 125, 216], ['ab', 'cde', 'fghi', 'jklmn']]
a[0][1] #4


#list comprehension

y = []

for x in range(10): #range(0,10,1)
    y.append(x)
y
y = [x**2 for x in range(10)]
y

#built-in function list()

x = list(('Tes','trying','to','code','using','python'))
x

#Compare two lists

list1, list2 = [3,5,7,9],[3,5,7,9]
print(list1 == list2)
list1.sort(key=None, reverse=True)
print(list1 == list2.sort()) #order and compare

#Getting the index of an element contained in a list
list3 = list1 + list2
#define the index from which we want to start
list3.index(3,3) # returns the index of 3 list3 starting from position 3
list3.index(3,3,5) # returns the index position of 3 starting from position and ending at position 5 excluding 5

# Using lists as queues
from collections import deque
color_list = deque(["Red", "Blue", "Green", "Black"])
#append to the queue when data arrives
color_list.append("White") #white arrives
print(color_list)

color_list.append("Yellow") #Yellow arrives

print(color_list)

color_list.popleft() #The first to arrive now leaves
color_list.popleft() #The second to arrive now leaves and returned as value

print(color_list)# remaining queue in order of arrival

#best practices

# use enumerate instead of range(len())------------enumerate gives index and value
data = [1,2,3,-3,-4]
#sort data in ascending order
data = sorted(data)
#sort data in eescending order
data = sorted(data, reverse=True)
print(data)
for indx, val in enumerate(data):
    if val<0:
        data[indx] = 0
print(data)

nameData = [{"name":"Tati","Age":46},{"Name":"Mita","Age":47}]
sortedName = sorted(nameData,key=lambda x: x['Age']) #sorted by specified key function
sortedName