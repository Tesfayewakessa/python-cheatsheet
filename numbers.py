#using python as a calculator

'''
Arithmetic operators:

we have a whool bunch of operators at our disposal
 + Addition
 - Subtruction
 * Multiplication
 / Division
 // Floor division
 % Modulus (remainder of x / y ) or use divmod(x,y)
 ** Exponentian (power of ) | can also use pow(x,y) instead of x**y

 Asignment operators:
 = Equals

 Number types:
 int 
 float

 Built-in function:

 round()  ---> rounds numbers to the specified number of decimals i.e round(number, decimals)
                if decimals is not passed, the result is floor to an int
 

 Finally, python has a hamdy of handling big int's easier to read
 4000000000 can be read as 4_000_000_000
'''
# The basics 
2 + 2 #simple addition
2 - 2 # simple subtruction
2*2 #simple multiplication

# division and mudulus
10/4 #float division
10//4 #integer division
10%2 #modulus
divmod(10,4) #returns a tuple (Division,remainder)
round(10.0234,2)

2**4 # exponentiation
pow(2,4)
assert(2**4 == pow(2,4))
