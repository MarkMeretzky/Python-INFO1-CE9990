"""
nestedloops.py

Output the chorus of "Lucy in the sky with diamonds".
"""

import sys

outer = 1
while outer <= 3:

    inner = 1
    while inner <= 3:
        print("Lucy in the sky with diammonds")
        inner += 1

    print("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaah")
    print()
    outer += 1

sys.exit(0)
