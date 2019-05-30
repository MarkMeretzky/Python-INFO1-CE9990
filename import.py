"""
import.py

Demonstrate that we can import a module we wrote.
"""

print("The import statement is about to search the following directories.")
for i, dir in enumerate(sys.path):
    print(i, dir)
print()

import sys
import date   #the date.py that we wrote

print("The following module has been loaded:")
print(sys.modules["date"])   #sys.modules is a dictionary.
print()

try:
    d = date.Date(12, 31, 2019)
except TypeError as error:
    print(error)
    sys.exit(1)
except ValueError as error:
    print(error)
    sys.exit(1)

print("d =", d)
print("type(d) =", type(d))

sys.exit(0)
