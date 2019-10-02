"""
do1.py

Demonstrate how they programmed before they invented dictionaries.
notes is a list of seven lists.
"""

import sys

notes = (
    ("do", "deer, a female deer"),
    ("re", "drop of golden sun"),
    ("me", "name I call myself"),
    ("fa", "long, long way to run"),
    ("so", "needle pulling thread"),
    ("la", "note to follow so"),
    ("ti", "drink with jam and bread")
)

while True:
    try:
        n = input("Please type a note (e.g., do): ")
    except EOFError:
        sys.exit(0)

    for note in notes:   #note is a list of two strings
        if note[0] == n:
            print(f"{n.capitalize()}, a {note[1]}.")
            break        #Break out of the for loop, skipping the else.
    else:
        #Arrive here if the break was not executed,
        #i.e., if the for loop did not find n.
        print(f'Sorry, "{n}" is not a note.')
        
    print()
