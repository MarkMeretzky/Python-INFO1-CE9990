"""
returntuple.py

A function that returns a tuple of items.
"""
import sys

def stats(collection):
    "Return the minimum, maximum, and average value in the collection."
    try:
        _ = iter(collection)
    except TypeError as error:
        print(f"Sorry, an argument of type {type(arg0)} is not iterable.", file = sys.stderr)
        sys.exit(1)

    assert len(collection) > 0 #Don't let line 20 divide by 0.
    listOfBools = [isinstance(item, (int, float)) for item in collection]
    assert all(listOfBools)    #Assert that all the bools are True.

    return (min(collection), max(collection), sum(collection) / len(collection)) #outer parens unnecessary


listOfInts = [10, 20, 50, 30, 20]
(minimum, maximum, average) = stats(listOfInts) #parens around the three variables are unnecessary

print(f"minimum = {minimum}")
print(f"maximum = {maximum}")
print(f"average = {average}")
sys.exit(0)
