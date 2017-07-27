"""
variablenumber.py

Pass a variable number of arguments to a function.
"""

import sys

def myPrint(*args):
    assert isinstance(args, tuple)
    for arg in args:
        print(arg)
    print(80 * "-")

myPrint()                        #0 arguments
myPrint(10)                      #1 argument
myPrint(10, 20)                  #2 arguments
myPrint("Moe", "Larry", "Curly") #3 arguments

myList = [10, 20, 30, 40]
myPrint(*myList)                 #1 argument, but that argument is a list
sys.exit(0)
