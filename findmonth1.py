"""
findmonth1.py

Demonstrate how they programmed before they invented lists.
"""

import sys

try:
    month = input("Please type a month, e.g., January: ")
except EOFError:
    sys.exit(0)

if month == "January":
    i = 1
elif month == "February":
    i = 2
elif month == "March":
    i = 3
elif month == "April":
    i = 4
elif month == "May":
    i = 5
elif month == "June":
    i = 6
elif month == "July":
    i = 7
elif month == "August":
    i = 8
elif month == "September":
    i = 9
elif month == "October":
    i = 10
elif month == "November":
    i = 11
elif month == "December":
    i = 12
else:
    print("Bad month \"", month, "\".", sep = "")
    sys.exit(1)

print("Thank you, ", month, " is month number ", i, ".", sep = "")
sys.exit(0)
