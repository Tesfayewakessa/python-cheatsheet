#Us sing set to manipulate data in python
'''
Similar to lists and tuples, sets are another compound data represntation

sets are unordered collection of data with no repeating elements. Sets are represented with curly brackets like dictionaries
It is commonly used for membership testing, removing dublicates from a sequense and computing mathematical operations
Sets are mutable. This means the items can be changed.

Sets have a bunch of methods aavailable
add()                               adds an element to the set
clear()                             clear all the elements of the set
copy()                              returns a copy of the set
difference()                        returns a set containing the difference between two or more sets
difference_update                   removes the items in the set that are also specified in another set
discard()                           removes the specified element
intersection()                      returns a set that is an intersection between two or more sets
intersection_update()               removes an element in a set that is not presents in another specified set
isdijoint()                         returns whether two sets have an intersection or not
issubset()                          returns whether this set contains another set or not
issuperset()                        returns whether this set contains another set or not
pop()                               removes an element from a set
remove()                            removes thespecified elelemt
symmetric_difference()              returns a set with symmetric difference of two sets
symmetric_difference_update()       inserts the symmetric difference from this set and another
union()                             returns a set containing the union of the two sets
update()                            update a set with another set or any other iterable
'''
#empty set
color_set = set()

#add members to the set
color_set.add('Red')
print(color_set)

#add multiple items
color_set.update(["Green","Yellow"])
print(color_set)
#non empty set----lsit input
n = set([1,2,3,4,5])
print(n)
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket) # the duplicate element will be removed

##fast membership test
'orange' in basket
'crabgrass' in basket
a = set('Ethiopia tikdem')
b =  set ('great Ethipia')
a - b # letters in a but not in b
a | b # letters in a or b
a & b #letters in a and b
a ^ b # letters in a or b but not both

#set comprehension
c = {x for x in a if x not in b}
print(c)

#built-in set function
d = tuple(x for x in a & b)
print(d)
e = set(d)# it accepts tuple
print(e)

#iterate for set
for n in e:
    print(n)

#remove the last item from a set
e.pop()
print(e)

#remove a specified item from a set
num_set= set([0,1,2,3,4,5,6])
num_set.remove(0)

#discard() function
num_set.discard(3) #removes an element from a set if it is in the set.otherwise do nothing

#intersection of sets
#In mathematics, the intersection A ∩ B of two sets A and B is the set that contains all elements of A 
# that also belong to B (or equivalently, all elements of B that also belong to A), but no other elements.
setx  = set(['Blue','Yellow'])
sety  = set(['Red','Yellow'])
setz = setx & sety
print(setz)
#Union of sets

#In set theory, the union (denoted by ∪) of a collection of sets is the set of all distinct elements in the collection. 
# It is one of the fundamental operations through which sets can be combined and related to each other.
#Union

setx  = set(['Blue','Yellow'])
sety  = set(['Red','Yellow'])
setz = setx  | sety
print(setz)

#set difference
setd = setx - sety

#symmetric difference

sete = setx ^ sety

#issubset() issuperset()
issubset = setx <= sety #returns true or false
issupperset = setx >= sety

#copy function
setf = setx.copy() # creates a shallow exact copy

#clear() function
setf.clear()

print(setf)
