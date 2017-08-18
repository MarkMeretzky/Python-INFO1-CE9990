"""
date1.py

Create, print, compare, and modify
objects of classes datetime.date and datetime.datetime.
"""

import sys
import datetime

#An object of class datetime.date contains a year, month, day.
d = datetime.date(2017, 12, 31)

#Four ways to print d.
print(d)
print(d.year, "-", d.month, "-", d.day, sep = "")
print(d.strftime("%Y-%m-%d"))                   #strftime returns a string
print(d.strftime("%A, %B %-d, %Y (%-d %b %Y)")) #%-d has no leading zero
print()

#An object of class datetime.datetime also contains an hour, minute, second.
dt = datetime.datetime(2017, 12, 31, 23, 59, 59)

#Three ways to print dt.
print(dt)
print(dt.year, "-", dt.month, "-", dt.day,
    " ", dt.hour, ":", dt.minute, ":", dt.second, sep = "")
print(dt.strftime("%A, %B %-d, %Y %H:%M:%S (%I:%M:%S %p)"))
print()

#Another way to create an object of class datetime.datetime.
dt2 = datetime.datetime.strptime("2018-1-1", "%Y-%m-%d")
print(dt2.strftime("%A, %B %-d, %Y %H:%M:%S (%I:%M:%S %p)"))

#Another way to create an object of class datetime.date.
e = dt2.date()   #Just the year, month, day, but not the hour, minute, second.
print(e.strftime("%A, %B %-d, %Y"))
print()

if d < e:
    print(d, " is earlier than ", e, ".", sep = "")
else :
    print(d, "is later than or equal to ", e, ".", sep = "")

#Move d foreward one day.  delta is the distance: exactly one day.
delta = datetime.timedelta(days = 1)
d += delta   #means d = d + delta
print("d is now ", d, ".", sep = "")

sys.exit(0)
