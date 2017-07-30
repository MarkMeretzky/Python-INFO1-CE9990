"""
import.py

Demonstrate that we can import a module we wrote.
"""

import sys
import date   #the date.py that we wrote

print("The following module has been loaded:")
print(sys.modules["date"])   #sys.modules is a dictionary.
print()

d = date.Date(12, 31, 2017)
print("d = ", d)
print("type(d) =", type(d))

sys.exit(0)
