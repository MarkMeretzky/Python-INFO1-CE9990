"""
nestedloops.py

Output the chorus of "Lucy in the Sky with Diamonds".
"""

import sys

for outer in range(3):   #means range(0, 3)
    
    for inner in range(3):
        print("Lucy in the sky with diamonds")

    print(f'A{28 * "a"}h')
    print()

sys.exit(0)
