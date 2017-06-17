"""
subscript.py

Demonstrate string subscripting (i.e., indexing).
"""

import sys

s = "counterclockwise"

#Don't bother to print the period at the end of each sentence.
print("The value of s is", s)
print("The type of s is", type(s))
print("The length of s is", len(s))
print()

print("The first character is", s[0])
print("The second character is", s[1])
print("The third character is", s[2])
print("The fifteenth character is", s[14])
print()

print("The last character is", s[-1])
print("The next-to-last character is", s[-2])
print("The third-from-last character is", s[-3])

sys.exit(0)
