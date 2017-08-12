"""
date2.py

Sort a list of strings that look like dates into chronological order.
"""

import sys
import datetime

dates = [
    "September 1, 1939",
    "October 24, 1929",
    "July 20, 1969",
    "September 11, 2001",
    "November 22, 1963"
]

def score(item):
    "Return the date object that this string looks like."
    dt = datetime.datetime.strptime(item, "%B %d, %Y")
    return dt.date()

dates.sort(key = score)

for date in dates:
    print(date)

sys.exit(0)
