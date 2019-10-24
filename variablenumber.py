"""
variablenumber.py

Pass a variable number of arguments to a function.
"""

import sys

def myPrint(*args):
    assert isinstance(args, tuple)
    listOfStrings = [str(arg) for arg in args]
    oneBigString = " ".join(listOfStrings)
    print(f"myPrint received {len(args)} argument(s): {oneBigString)}")

myPrint()                        #0 arguments
myPrint(10)                      #1 argument
myPrint(10, 20)                  #2 arguments
myPrint("Moe", "Larry", "Curly") #3 arguments

myList = [10, 20, 30, 40]
myPrint(myList)                 #1 argument, but that argument is a list
myPrint(*myList)                #4 arguments
sys.exit(0)
