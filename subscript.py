"""
subscript.py

Demonstrate string subscripting (i.e., indexing).
"""

import sys

s = "counterclockwise"

#Don't bother to print the period at the end of each sentence.
print(f"The value of s is {s}.")
print(f"The type of s is {type(s)}.")
print(f"The length of s is {len(s)}.")
print()

print(f"The first character is {s[0]}.")
print(f"The second character is {s[1]}.")
print(f"The third character is {s[2]}.")
print(f"The sixteenth character is {s[15]}.")
print()

print(f"The last character is {s[-1]}.")
print(f"The next-to-last character is {s[-2]}.")
print(f"The third-from-last character is {s[-3]}.")

sys.exit(0)
