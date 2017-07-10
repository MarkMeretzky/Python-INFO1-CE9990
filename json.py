"""
json.py

Convert a string that looks like a list of numbers
into an actual list of numbers.
"""

import sys
import json                #JavaScript Object Notation 

s = "[10, 20, 30, 40,50]"  #deliberately omitted a space
print("type(s) =", type(s))
print("s =", s)
print()

#Convert the string of characters into a list of numbers.
try:
    listOfNumbers = json.loads(s)
except json.JSONDecodeError as jSONDecodeError:
    print(jSONDecodeError)
    sys.exit(1)

#Now that we have a list of numbers,
#we can loop through the numbers with a for loop.
print("type(listOfNumbers) =", type(listOfNumbers))
for n in listOfNumbers:
    print(n)
print()

#Convert the list of numbers back into a string of characters.
print("Pretty print the listOfNumbers.")
print()

try:
    print(json.dumps(listOfNumbers))
except TypeError as typeError:
    print(typeError)
    sys.exit(1)

sys.exit(0)
