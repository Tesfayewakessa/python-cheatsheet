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

# create a copy of a list
squares[:]
assert(squares[:]==squares.copy())

#concatination or glueing together

squares + squares[:] + squares.copy()
squares

#modifying or altering items

cubes = [1,8,27,65,125] # 65 was supposed to be 64 as 4 ** 3  

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