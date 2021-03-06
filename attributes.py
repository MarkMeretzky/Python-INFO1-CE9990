"""
attributes.py
Demonstrate that the values in a dictionary can belong to different data types.
"""

import sys

attributes = {
    "name":           "Mark",            #string
    "zipcode":        10003,             #int
    "age":            64.25,             #float
    "citizenship":    True,              #bool
    "leaning":        "flaming liberal", #string
    "favorite years": (1968, 2001, 2019) #tuple
}

while True:
    for key in sorted(attributes.keys()):
        print(f"\t{key}")   #Indent with one tab character.

    print()
    
    try:
        key = input("What attribute do you want to see (e.g., name)? ")
    except EOFError:
        sys.exit(0)

    try:
        print(f"The attribute {key} is {attributes[key]}.")
    except KeyError:
        print(f'Sorry, "{key}" is not an attribute.')

    print()
