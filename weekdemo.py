"""
weekdemo.py

Demonstrate the generator week.range.
"""

import sys
import datetime
import week

#startingDate and d are objects of class datetime.date.
startingDate = datetime.date(2017, 12, 31)

for d in week.range(startingDate):
    print(d.strftime("%a %Y-%m-%d"))

sys.exit(0)
