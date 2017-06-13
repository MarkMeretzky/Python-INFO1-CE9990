"""
elif.py

Steer the computer in one of three possible directions using if/elif/else.
"""

import sys

receipts = input("How much were our receipts? ")
receipts = int(receipts)

expenditures = input("How much were our expenditures? ")
expenditures = int(expenditures)

print()   #Skip a line.

if receipts < expenditures:
    print("We're losing money.")
elif receipts == expenditures:
    print("We're breaking even.")
else:
    print("We're making money.")

sys.exit(0)
