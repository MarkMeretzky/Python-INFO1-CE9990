"""
weekdemo.py

Demonstrate the generator week.range.
"""

import sys
import datetime
import week   #This is the week.py we wrote.

#startingDate and d are objects of class datetime.date.
startingDate = datetime.date(2017, 12, 31)

for d in week.range(startingDate):  #the range we wrote in week.py
    print(d.strftime("%a %Y-%m-%d"))

sys.exit(0)
