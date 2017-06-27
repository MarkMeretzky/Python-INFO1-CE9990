"""
findmonth2.py

Demonstrate a list as an alternative to a long chain of if/elif/else.
"""

import sys

try:
    month = input("Please type a month, e.g., January: ")
except EOFError:
    sys.exit(1)

months = [
    None,        # 0
    "January",   # 1
    "February",  # 2
    "March",     # 3
    "April",     # 4
    "May",       # 5
    "June",      # 6
    "July",      # 7
    "August",    # 8
    "September", # 9
    "October",   #10
    "November",  #11
    "December",  #12
]

n = len(months)

for i in range(1, n):
    if month == months[i]:
        break
else:
    #Arrive here if we did not execute the break.
    print("Bad month \"", month, "\".", sep = "")
    sys.exit(1)

print("Thank you, ", month, " is month number ", i, ".", sep = "")
sys.exit(0)
