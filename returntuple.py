"""
returntuple.py

A function that returns a tuple of items.
"""
import sys

def stats(myList):
    "Return the minimum, maximum, and average of the numbers in a list."
    assert isinstance(myList, list) or isinstance(myList, tuple)
    assert len(myList) > 0   #Don't divide by zero in the next statement.
    return (min(myList), max(myList), sum(myList) / len(myList)) #outer parens unnecessary

myList = [10, 20, 50, 30, 20]
(minimum, maximum, average) = stats(myList) #parens around the three variables are unnecessary

print("minimum =", minimum)
print("maximum =", maximum)
print("average =", average)
sys.exit(0)
