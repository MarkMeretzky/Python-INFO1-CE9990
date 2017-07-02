"""
attributes.py

Demonstrate that the values in a dictionary can belong to different data types.
"""

import sys

attributes = {
    "name":        "Mark",           #string
    "zipcode":     10705,            #int
    "age":         61.9,             #float
    "citizenship": True,             #bool
    "leaning":     "flaming liberal" #string
}

while True:
    for key in sorted(attributes.keys()):
        print(key)

    print()
    
    try:
        key = input("What attribute do you want to see? ")
    except EOFError:
        sys.exit(0)

    try:
        value = attributes[key]
    except KeyError:
        print("Sorry, \"", key, "\" is not an attribute.", sep = "")
        print()
        continue   #Go back up to the word "while"

    t = str(type(value))   #t is a string such as "<class 'int'>".
    print(key, " is the ", t[8:-2], " ", value, ".", sep = "")
    print()
