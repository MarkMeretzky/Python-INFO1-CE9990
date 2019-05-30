"""
week.py

A range of 7 consecutive objects of class datetime.date or class
datetime.datetime, depending on the type of the startingDate.
"""

import datetime
import builtins

def range(startingDate):
    "Yield a range of 8 dates, starting with the startingDate."
    if not isinstance(startingDate, datetime.date) \
        and not isinstance(startingDate, datetime.datetime):
        raise TypeError("startingDate must be datetime.date or "
            + f"datetime.datetime, not {type(startingDate)}")

    for i in builtins.range(8):
        yield startingDate + datetime.timedelta(days = i)


if __name__ == "__main__":
    import sys
    startingDate = datetime.datetime.now().date()
    
    for d in range(startingDate):
        print(d.strftime("%a %Y-%m-%d"))
        
    sys.exit(0)
