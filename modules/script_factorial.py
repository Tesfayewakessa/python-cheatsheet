#script_factorial.py

def calFactorial(n):
    fact = 1
    while n > 0:
        fact*=n
        n-=1
        if (n<=1):
            break
    else:
        #Display the message if n is not a positive integer
        print(f"Please enter a valid number to compute the factorial----")
        return
    return fact

def factorialData(n):
    result = []
    while n>0:
        result.append(n)
        n-=1
        if n==0:
            break
    else:
        print(f"Please input a correct number ----")
        return
    return result

if __name__=="__main__":
    import sys
    calFactorial(int(sys.argv[1]))
    calFactorial(int(sys.argv[2]))