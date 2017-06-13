"""
thenif2.py

Need to perform the second comparison only if the first comparison was true.
(If the first comparison was false, the second comparison would be a
waste of time.)
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
