#Using modules in python

'''
In python, we are able to write a long program and save as a module. This is known as creating script.
We are able to import modules across modules and into the python interpretor. This helps us avoid repeating ourselves
It is a simple way to organize a program which contains program codes, variables .... in one single file

The name of the module is the name of the file name with .py extension

Modules will not be executed unless they are called in a program or an interpreter

To define a module, we can use python ide, notepad++ or any suitable editor

'''

from modules.functions import demo_func
from modules.compute_factorial import factorialdata, fact
def funct_1(arg:int):
    x = [y for y in range(2,10,2)]
    x.append(arg)
    print(x)

def func_2(number:int, power:int):
    print(pow(number,power))
demo_int = demo_func(1)
funct_1(demo_int)
func_2(2,demo_int)
fact(2)
factorialdata(2)

#executing modules as a script
