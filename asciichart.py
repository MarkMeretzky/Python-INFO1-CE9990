"""
asciichart.py

Print the printable ASCII characters (the ones in the range 32 to 126 inclusive)
and their code numbers in decimal (base 10), octal (base 8), hexadecimal (base 16), and binary (base 2).

The formatted string:

1. Print the character whose code number is i.
2. Print i in decimal, left padded with spaces if necessary to use a minimum of 7 characters.
3. Print i in octal, left-padded with spaces if necessary to use a minimum of 5 characters.
4. Print i in uppercase hexadecimal, left-padded with zeroes if necessary to use a minimum of 2 characters.
5. Prit i in binary, left-padded with zeroes if necessary to use a minimum of 8 characters
"""

import sys

print("  decimal octal hex   binary")

for i in range(32, 127):
    print(f"{i:c} {i:7} {i:5o}  {i:02X} {i:08b}")

sys.exit(0)
