"""
do2.py

Demonstrate a dictionary.
"""

import sys

notes = {
    "do": "deer, a female deer",
    "re": "drop of golden sun",
    "me": "name I call myself",
    "fa": "long, long way to run",
    "so": "needle pulling thread",
    "la": "note to follow so",
    "ti": "drink with jam and bread"
}

while True:
    try:
        note = input("Please type a note (e.g., do): ")
    except EOFError:
        sys.exit(0)

    try:
        definition = notes[note]
    except KeyError:
        print("Sorry, \"", note, "\" is not a note.", sep = "")
        print()
        continue   #Go back up to the word "while".
    
    print(note.capitalize(), ", a ", definition, ".", sep = "")
    print()
