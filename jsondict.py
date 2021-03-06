"""
jsondict.py

Convert a string that looks like a dictionary into an actual Python dictionary.
"""

import sys
import json                #JavaScript Object Notation 

s = """\
{
   "name":           "Mark",
   "age":            64,
   "favorite years": [1965, 1982, 1995],
   "IKEA language":  {"Billy": "bookcase", "Sladda": "bike", "Klippan": "sofa"}
}"""

print(f"type(s) = {type(s)}")
print(f"s = {s}")
print()

#Convert the string of characters into a dictionary.
try:
    dictionary = json.loads(s)
except json.JSONDecodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(f"type(dictionary) = {type(dictionary)}")

#Now that we have a dictionary,
#we can loop through the items with a for loop.
for key, value in dictionary.items():
    print(f"{key} = {value}")
print()

#Convert the dictionary back into a string of characters.
print("Pretty print the dictionary.")

try:
    s = json.dumps(dictionary, indent = 4, sort_keys = True)
except TypeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(s)
sys.exit(0)
