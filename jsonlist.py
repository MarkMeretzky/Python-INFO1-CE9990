"""
jsonlist.py

Convert a string that looks like a list of ints
into an actual Python list of ints.
"""

import sys
import json                #JavaScript Object Notation 

s = "[10, 20, 30, 40,50]"  #deliberately omitted a space
print("type(s) = {type(s)}")
print(f"s = {s}")
print()

#Convert the string of characters into a list of ints.
try:
    listOfInts = json.loads(s)
except json.JSONDecodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

#Now that we have a list of ints,
#we can loop through the ints with a for loop.
print(f"type(listOfInts) = {type(listOfInts)}")
for n in listOfInts:
    print(n)
print()

#Convert the list of ints back into a string of characters.
print("Pretty print the listOfInts.")

try:
    s = json.dumps(listOfInts)
except TypeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s)
sys.exit(0)
