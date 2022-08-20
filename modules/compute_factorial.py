# define a function to compute the factorial of a positive integer

def fact(n):
    val = 1
    while(n>0):
        val*=n
        n-=1
        if(n<=1):
            break
    else: # Display a message if n is not a positive integer or zero
        print(f"Please input a corect number ---- ")
        return
    return val

def factorialdata(n):
    result = [] #create a list of inputs n
    while n>0:
        result.append(n)
        n-=1
        if n==0:
            break
    else: # Display a message if n is not a positive integer or zero
        print(f"Please input a corect number ---- ")
        return
    return result