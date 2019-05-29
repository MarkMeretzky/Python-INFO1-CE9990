"""
classDate.py

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its instance methods.
"""

import sys

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
        assert isinstance(year, int)
        assert isinstance(month, int) and 1 <= month and month <= 12
        assert isinstance(day, int) and 1 <= day and day <= Date.lengths[month]
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
        return f"{self.month:02}/{self.day:02}/{self.year:04}"

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
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.nextDay()     #Call the instance method in line 62.

    def monthsInYear():
        "Return the number of months in a year.  This function is selfless."
        return len(Date.lengths) - 1;

    #The definition of class Date ends here.


print("months in year =", Date.monthsInYear())
d = Date(12, 31, 2019)         #Call the instance method in line 32.
print("type(d) =", type(d))
print()

#These three statements do the same thing:
print("d =", d)
print("d =", str(d))
print("d =", d.__str__())      #Call the instance method in line 54.
print()

print("month =", d.getMonth()) #Call the instance method in line 46.
print("day =", d.getDay())     #Call the instance method in line 50.
print("year =", d.getYear())   #Call the instance method in line 42.
print()

print(f"{d} is day number {d.dayOfYear()} of the year {d.getYear()}.")
d.nextDay()                    #Call the instance method in line 62.
print(f"{d}is the next day.")
d.nextDays(7)                  #Call the instance method in line 74.
print(f"{d}is a week after that.")
sys.exit(0)
