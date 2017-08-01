"""
date.py

This file is a Python module.  You can import this module by saying
import date
at the top of your Python script.
Then in your script, you can use class date.Date
"""

class Date(object):
    """
    Class Date demonstrates class and instance attributes, class and instance methods.
    It is a simple date class, containing year, month, and day integers.
    """

    lengths = [
        None,
        31, #January
        28, #February
        31, #March
        30, #April
        31, #May
        30, #June
        31, #July
        31, #August
        30, #September
        31, #October
        30, #November
        31  #December
    ]

    def __init__(self, month, day, year):
        if not isinstance(year, int):
            raise TypeError("year must be int, not " + str(type(year)))
        if not isinstance(month, int):
            raise TypeError("month must be int, not " + str(type(month)))
        if month < 1 or month > Date.monthsInYear():
            raise ValueError("month must be in range 1 to " +
                Date.monthsInYear() + " inclusive, not " + str(month))
        if not isinstance(day, int):
            raise TypeError("day must be int, not " + str(type(day)))
        if day < 1 or day > Date.lengths[month]:
            raise ValueError("day must be in range 1 to " +
                Date.lengths[month] + " inclusive, not " + str(day))
        self.year = year
        self.month = month
        self.day = day

    #These three methods are getters.

    def getYear(self):
        "Return my year."
        return self.year

    def getMonth(self):
        "Return the number of my month (1 to 12 inclusive)."
        return self.month

    def getDay(self):
        "Return the number of my day (1 to the length of my month, inclusive)."
        return self.day

    def __str__(self):
        "Return a string that looks like the contents of myself."
        return "{:02}/{:02}/{:04}".format(self.month, self.day, self.year)

    def dayOfYear(self):
        "Return my day of the year: a number in the range 1 to 365 inclusive."
        return sum(Date.lengths[1:self.month]) + self.day

    def nextDay(self):
        "Move myself one day into the future."
        if self.day < Date.lengths[self.month]:
            self.day += 1
        else:
            self.day = 1       #Go to the first day of the next month.
            if self.month < len(Date.lengths) - 1:
                self.month += 1
            else:
                self.month = 1 #Go to the first month of the next year.
                self.year += 1

    def nextDays(self, n):
        "Move myself n days into the future."
        if not isinstance(n, int):
            raise TypeError("n must be int, not " + str(type(n)))
        if n < 0:
            raise ValueError("n must be nonnegative, not " + str(n))
        for i in range(n):
            self.nextDay()     #Call the instance method in line 71.

    def monthsInYear():
        "Return the number of months in a year.  This function is selfless."
        return len(Date.lengths) - 1;

    #The definition of class Date ends here.


if __name__ == '__main__':
    import sys
    import datetime
    now = datetime.datetime.now()
    #Create a Date object holding today's date.
    d = Date(now.month, now.day, now.year)
    print("Today is ", d, ".", sep = "")
    sys.exit(0)
