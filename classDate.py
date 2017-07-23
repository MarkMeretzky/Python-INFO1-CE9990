"""
classDate.py

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its methods.
"""

import sys

class Date(object):
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
        assert isinstance(month, int) and 1 <= month and month <= 12
        assert isinstance(day, int) and 1 <= day and day <= Date.lengths[month]
        assert isinstance(year, int)
        self.year = year
        self.month = month
        self.day = day

    #These three methods are getters.
    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day
        
    #When you give a Date to print,
    #you're really printing the return value of this function.
    def __str__(self):
        return "{:02}/{:02}/{}".format(self.month, self.day, self.year)

    #Return a number in the range 1 to 365 inclusive: the sum of the lengths of
    #all the months preceding the month that contains myself, plus my day.
    def dayOfYear(self):
        return sum(Date.lengths[1:self.month]) + self.day

    #Move myself 1 day into the future.
    def nextDay(self):
        if self.day < Date.lengths[self.month]:
            self.day += 1
        else:
            self.day = 1         #Go to the first day of the next month.
            if self.month < len(Date.lengths) - 1:
                self.month += 1
            else:
                self.month = 1   #Go to the first month of the next year.
                self.year += 1

    #Move myself n days into the future.
    def nextDays(self, n):
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.nextDay()       #Call the method in line 56.

    #Return the number of months in a year.  This function is selfless.
    def monthsInYear():
        return len(Date.lengths) - 1;

    #The definition of class Date ends here.


print("months in year =", Date.monthsInYear())
d = Date(12, 31, 2017)         #Call the method in line 27.
print("type(d) =", type(d))
print()

#These three statements do the same thing:
print("d =", d)
print("d =", str(d))
print("d =", d.__str__())      #Call the method in line 47.
print()

print("month =", d.getMonth()) #Call the method in line 39.
print("day =", d.getDay())     #Call the method in line 42.
print("year =", d.getYear())   #Call the method in line 36.
print()

print("{} is day number {} of the year {}.".format(d, d.dayOfYear(), d.getYear()))
d.nextDay()                    #Call the method in line 56.
print(d, "is the next day.")
d.nextDays(7)                  #Call the method in line 68.
print(d, "is a week later than that.")
sys.exit(0)
