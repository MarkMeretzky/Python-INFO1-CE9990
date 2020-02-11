"""
stdin.py

Prompt the user for his or her name.
Read the name from the standard input, and send a geeting to the standard
output. 
"""

import sys

first = input("What is your first name? ")   #final space for legibility
last = input("What is your last name? ")
print(f"Hello, {first} {last}.")

sys.exit(0)
