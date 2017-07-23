"""
import.py

Demonstrate that we can import a module we wrote.
"""

import sys
import date   #the date.py that we wrote

d = date.Date(12, 31, 2017)
print(d)
print()

print("The following module has been loaded:")
print(sys.modules["date"])
print()

print("The date module has the following", len(dir(date)), "attributes:")
print()

for i, name in enumerate(dir(date), start = 1): #dir(date) is a list of strings
    obj = eval("date." + name)   #obj is the object whose name is date.name
    if name == "__doc__":
        s = "printed separately below"
    elif isinstance(obj, dict):
        s = "a dictionary of " + str(len(obj)) + " items"
    elif isinstance(obj, str):
        s = "\"" + obj + "\""
    else:
        s = obj
    print("{} {:12} {:14} {}".format(i, name, str(type(obj)), s))

print()

print("date.__doc__ =", date.__doc__)
sys.exit(0)
