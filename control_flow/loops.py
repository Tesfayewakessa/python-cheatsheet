#Python flow control ----- loops

'''
A for statement iterates over an items of a sequence in the order they appear in the sequence.
The built-in range function comes in very handy when iterating over a sequence. A range generates arithmentic progressions

range(start,stop, step)

start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)

'''
#Using for loops on list 
import numbers


animals = ['cat','dog','sheep','goat','horse','donkey']
#iterate over the animal list and print out their name and length of their name
for animal in animals:
    print(animal,len(animal))


#iteratting over a tuple
numbers = (1,2,3,4,5,6,7,8,9)
even_count = 0
odd_count = 0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Number of even numbers is {even_count}")
print(f"Number of odd numbers is {odd_count}")
#Using for loops on dictionaries
users = {
    'Quinn': 'active',
    'Éléonore': 'inactive',
    'John': 'active'
    }

# get keys
for user in users:
    print(user)
print(sorted(users)) # returns sorted list of users


for user, status in users.items():
    if status == 'active':
        #get the name of active users
        #print(user)
        #get the users and their status
        print(user, users[user])
# work on (iterate) copies of the dictionaries
for user, status in users.copy().items():
    if status == "inactive":
        del users[user] #removes inactive users
#print(users)
#Create a dictionary of active users
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = 'active'
    print(active_users)

#Using range function
sum = 0
for i in range(5):
    print(i)
    sum+=i
print(sum)

a = ['I', 'am','having','good','understanding','of','python']
for i in range(len(a)):
    print(i,len(i)) # prints out each element and their length
