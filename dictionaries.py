#Using python dictionaries
'''
Dictionaries are used to store values in key:value pair format.

Dictionaries have a bunch of methods available.

clear()         Removes all the elements from the dictionary
copy()          Returns a copy of the dictionary
fromkeys()      Returns a dictionary with the specified keys and value
get()           Returns the value of the specified key if it is available in the dictionary. Else returns default
items()         Returns a list containing a tuple for each key value pair
keys()          Returns a list containing the dictionary's keys
pop()           Removes the element with the specified key
popitem()       Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()        Updates the dictionary with the specified key-value pairs
values()        Returns a list of all the values in the dictionary

Dictionaries are mutable, it means the item values can be changed

'''
#empty dictionary
dicta = {}
#dict with key-value pair
some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'},
    'a_key_5': ('a_tuple','as','a','value'),
    'a_key_6': ('a_set','as','a','value'),
}

#get dict value by key
some_dict['a_key']
print(some_dict)

#altering a dict value
some_dict['a_key'] = "value1"
print(some_dict)

#Access value using get method
some_dict.get('a_key')
print(some_dict)

#add key-value pair to a dictionary in a number of ways
#1 add new value by new key
some_dict['a_key_7'] = 'new_value'
#2 use the update() method for dictionaries
some_dict.update({'w':3})
print(some_dict)
some_dict.update({1:2, 3:4, 5:6, 7:8})
print(some_dict)
#length of dict
len(some_dict)
print(some_dict)

##get all keys
print(some_dict.keys()) #dict_keys(['a_key', 'a_key_2', 'a_key_3', 'a_key_4', 'a_key_5', 'a_key_6'])

#get all values
print(some_dict.values()) #dict_values(['value1', 'a_value_2', ['a_list', 'as', 'a value'], {'a_dict': 'as a value'}, ('a_tuple', 'as', 'a', 'value'), ('a_set', 'as', 'a', 'value')])


#dict comprehension
some_dict1 = {x:x**2 for x in (2,4,6)}

#built_in dict function
some_dict2 = dict(a =2, b = 3, c = 4) #creates a dictionary object

#iterate over python dictionaries using for loops

dict2 = {'Red':1,'Green':2,'Yellow':3,'Blue':4}
for key,val in dict2.items():
    print(key +" has a value of ", dict2[key])

#Remove a key from a dictionary
if 'Red' in dict2:
    del dict2['Red']
print(dict2)

#Sort dictionaries by key
dicta = {}
for key in sorted(dict2):
    print("%s: %s" %(key,dict2[key]))
    dicta.update({key:dict2[key]})
    sorted(dict2) #Returns a list containing all keys
print(dicta)

#finding max and min of a python dictionary
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

#Concatinate a python dictionaries into one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)
#merging dictionaries with double asterix synthax
dic5 = {**dic1,**dic2,**dic3}
dic5
assert(dic4==dic5)
#Test whether a dictionary has a spefic key or not
fruits = {}
fruits["apple"] = 1
fruits["mango"] = 2
fruits["banana"] = 4

# Use in.
if "mango" in fruits:
    print("Has mango")
else:
    print("No mango")

# Use in on nonexistent key.
if "orange" in fruits:
    print("Has orange")
else:
    print("No orange")

#define defualt values with .get() and .setdefault()

