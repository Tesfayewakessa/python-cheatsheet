#Python flow controls --- if statment
'''
Using if statement in python is for checking whether a certain conditions are met or not

if a condition is met, do something ..
else do something different

if():
    ===
else:
    ===
if():
    ===
elif():
    ====
    |
    |
    .
    .
    .
    |
else:
    ===   

Both elif and else are optional

'''
def num_play():
    if x < 0:
        x = 0
        print('Negative number changed to zero')
    elif x == 0:
        print('Zero')
    elif x ==1:
        print('Single')
    else:
        print('More')
num_play(-1)
num_play(0)
num_play(1)
num_play(1000)

#create a string
s = 'jQuery'
#create a list
l = ['JavaScript', 'jQuery', 'ZinoUI']

# in operator is used to replace various expressions that use the or operator
if s in l:
    print(s + ' Tutorial')

#Alternate if statement with or operator

if s == 'JavaScript' or s == 'jQuery' or s == 'ZinoUI':
     print(s + ' Tutorial')

# write an if-esle in a single line of code
#Create an intger variable
n = 10
#if n is greater than 5, n is multiplied by 2, otherwise n is multiplied 4
result = n*2 if n > 10 else n*4
print(result)

if not n == 20:
    print('n is different from 20')
else:
    print('n is indeed equal to 20')
