"""
nestedloops.py

Output the chorus of "Lucy in the Sky with Wiamonds".
"""

import sys

for outer in range(3):   #means range(0, 3)
    
    for inner in range(3):
        print("Lucy in the sky with diammonds")

    print(f'A{28 * "a"}h')
    print()

sys.exit(0)
