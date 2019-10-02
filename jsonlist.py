"""
jsonlist.py

Convert a string that looks like a list of numbers
into an actual Python list of numbers.
"""

import sys
import json                #JavaScript Object Notation 

s = "[10, 20, 30, 40,50]"  #deliberately omitted a space
print("type(s) = {type(s)}")
print(f"s = {s}")
print()

#Convert the string of characters into a list of numbers.
try:
    listOfNumbers = json.loads(s)
except json.JSONDecodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

#Now that we have a list of numbers,
#we can loop through the numbers with a for loop.
print(f"type(listOfNumbers) = {type(listOfNumbers)}")
for n in listOfNumbers:
    print(n)
print()

#Convert the list of numbers back into a string of characters.
print("Pretty print the listOfNumbers.")

try:
    s = json.dumps(listOfNumbers)
except TypeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s)
sys.exit(0)
