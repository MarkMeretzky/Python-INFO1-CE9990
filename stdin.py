"""
stdin.py

Prompt the user for their name.
Read the name from the standard input, and send a geeting to the standard
output. 
"""

import sys

first = input("What is your first name? ")
last = input("What is your last name? ")
print("Hello, ", first, " ", last, ".", sep = "")

sys.exit(0)
