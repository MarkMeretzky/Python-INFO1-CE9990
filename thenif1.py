"""
thenif1.py

Do we always need to perform both comparisons?
"""

import sys

receipts = input("How much were our receipts? ")
receipts = int(receipts)

expenditures = input("How much were our expenditures? ")
expenditures = int(expenditures)

print()   #Skip a line.

if receipts <= expenditures:
    print("We're not making any money.")

if receipts < expenditures:
    print("In fact, we're losing money.")

sys.exit(0)
