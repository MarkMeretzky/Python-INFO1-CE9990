"""
week.py

Class range is an interable for iterating through 7 consecutive datetime.date
or datetime.datetime objects, depending on the type of the startingDate passed
to the __init__ method.
"""

import datetime

class range(object):
    "An iterable for iterating through 7 consecutive datetime.datetime objects."

    def __init__(self, startingDate):
        assert isinstance(startingDate, datetime.date)
        self.startingDate = startingDate

    def __iter__(self):
        return Iterator(self)


class Iterator(object):

    def __init__(self, r):
        assert isinstance(r, range)
        self.r = r
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 7:
            raise StopIteration
        result = self.r.startingDate + datetime.timedelta(days = self.i)
        self.i += 1
        return result


if __name__ == "__main__":
    import sys
    now = datetime.datetime.now()
    startingDate = datetime.date(now.year, now.month, now.day)
    for d in range(now):
        print(d.strftime("%a %Y-%m-%d"))
    sys.exit(0)
