"""
week2.py

Class range is an interable for iterating through 8 consecutive datetime.date
or datetime.datetime objects, depending on the type of the startingDate passed
to the __init__ method.
"""

import datetime

class range(object):
    "An iterable for iterating through 8 consecutive datetime.datetime objects."

    def __init__(self, startingDate):
        assert isinstance(startingDate, datetime.date)
        self.startingDate = startingDate

    def __iter__(self):
        return Iterator(self.startingDate)


class Iterator(object):

    def __init__(self, startingDate):
        self.startingDate = startingDate
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 7:
            raise StopIteration
        result = self.startingDate + datetime.timedelta(days = self.i)
        self.i += 1
        return result


if __name__ == "__main__":
    import sys
    startingDate = datetime.datetime.today()
    for d in range(startingDate):
        print(d.strftime("%a %Y-%m-%d"))
    sys.exit(0)
