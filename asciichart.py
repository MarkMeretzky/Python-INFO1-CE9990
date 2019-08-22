"""
asciichart.py

Print the printable ASCII characters (the ones in the range 32 to 126 inclusive)
and their code numbers in decimal, octal, and hexadecimal.

The formatted string:

1. Print the character whose code number is i.
2. Print i in decimal, left padded with spaces if necessary to make it a total of 7 characters.
3. Print i in octal, left-padded with spaces if necessary to make it a total of 5 characters.
4. Print i in uppercase hexadecimal, left-padded with zeroes if necessary to make it a total of 3 characters.
"""

import sys

print("  decimal octal hex")

for i in range(32, 127):
    print(f"{i:c} {i:7} {i:5o} {i:03X}")

sys.exit(0)
