#Using python loop clauses
'''
Python has a few statments and clauses that we can use in loops:
These are:
break       used to exit out of a for or while loop. The purpose of break is end execution of loops(while or for) immediately after the last statement of the loop
            any statement after the break is skipped
continue    used in a while loop to take the control to the top of the loop with executing the rest of the statements coming after continue clause
else
pass

'''
#example for break statement
# the loop breaks after count equal 5. Anthing that comes after the end of the loop is executed
for  n in range(2,10):
    for x in range(2,n): # first loop is for x in range(2,2)
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
        #the else runs when no break caluse occurs
        else:
            print(f"{n} is a prime number")


numbers = (x for x in range(1,9)) #(1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
sum = 0
count = 0
#break in for loop
for x in numbers:
    sum+=x
    count+=1
    if count == 5:
        break
print(f" The sum of the first {count} numbers is {sum}")

# break in while loop
while(count < 10):
    sum+=count
    count+=1
    if count == 5:
        break
print(f" The sum of the first {count} numbers is {sum}")

#continue statement
for x in range(7):
    if (x==3 or x==6): #it will skip at x  = 3,6 and jump to the next loop
        continue
    print(x)


for num in range(2,10):
    if num%2 == 0:
        print(f"found an even number, {num}")
#pass in class
class MyPassClass:
    pass
# pass in function definition
def my_pass_method():
    pass

