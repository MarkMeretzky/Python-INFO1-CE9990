"""
dateunittest.py

This script runs the unit tests for class date.Date in module date.
"""

import unittest
import date
import datetime

class TestDateMethods(unittest.TestCase):

    def test_monthsInYear(self):
        "Does date.monthsInYear return the correct value?"
        self.assertEqual(date.Date.monthsInYear(), datetime.date.max.month)

    def test_init(self):
        "Does date.__init__ construct the correct object?"
        now = datetime.datetime.now() #so we can get the current year
        jan1 = datetime.date(now.year, 1, 1)
        daysInYear = TestDateMethods.daysInYear(now.year)
        
        for i in range(daysInYear):
            c = jan1 + datetime.timedelta(days = i)
            d = date.Date(c.month, c.day, c.year)
            self.assertEqual(d.getYear(), c.year)
            self.assertEqual(d.getMonth(), c.month)
            self.assertEqual(d.getDay(), c.day)
            self.assertEqual(d.dayOfYear(), c.timetuple().tm_yday)
            self.assertEqual(str(d), c.strftime("%m/%d/%Y"))

    def test_nextDay(self):
        "Does date.nextDay increment the Date object?"
        now = datetime.datetime.now()
        jan1 = datetime.date(now.year, 1, 1)
        daysInYear = TestDateMethods.daysInYear(now.year)
        
        for i in range(daysInYear):
            c = jan1 + datetime.timedelta(days = i)
            d = date.Date(c.month, c.day, c.year)
            d.nextDay()
            tomorrow = c + datetime.timedelta(days = 1)
            self.assertEqual(str(d), tomorrow.strftime("%m/%d/%Y"))

    def test_nextDays(self):
        "Does date.nextDays advance the Date object?"
        now = datetime.datetime.now()
        jan1 = datetime.date(now.year, 1, 1)
        daysInYear = TestDateMethods.daysInYear(now.year)
        
        for i in range(daysInYear):
            for j in range(2 * daysInYear):
                c = jan1 + datetime.timedelta(days = i)
                d = date.Date(c.month, c.day, c.year)
                d.nextDays(j)
                tomorrow = c + datetime.timedelta(days = j)
                self.assertEqual(str(d), tomorrow.strftime("%m/%d/%Y"))

    def test_nextDays_raise(self):
        "Does date.Date.nextDays raise exceptions correctly?"
        badArgs = (None, "", 1.0, (), [], {})
        now = datetime.datetime.now()
        d = date.Date(now.month, now.day, now.year)

        #Bad data type for argument.
        for badArg in badArgs:
            with self.assertRaises(TypeError):
                d.nextDays(badArg)

        #Bad value for argument.
        with self.assertRaises(ValueError):
            d.nextDays(-1)

    def test_init_raise(self):
        "Does date.Date.__init__ raise exceptions correctly?"
        badArgs = (None, "", 1.0, (), [], {})
        now = datetime.datetime.now()

        #Bad data type for year, month, day arguments.
        for badArg in badArgs:
            with self.assertRaises(TypeError):
                d = date.Date(now.month, now.day, badArg)
        for badArg in badArgs:
            with self.assertRaises(TypeError):
                d = date.Date(badArg, now.month, now.year)
        for badArg in badArgs:
            with self.assertRaises(TypeError):
                d = date.Date(now.month, badArg, now.year)

        #Bad value for month argument.
        with self.assertRaises(ValueError):
            d = date.Date(0, now.day, now.year)
        with self.assertRaises(ValueError):
            d = date.Date(datetime.date.max.month + 1, now.day, now.year)

        #Bad value for day argument.
        for month in range(1, datetime.date.max.month + 1):
            with self.assertRaises(ValueError):
                d = date.Date(month, 0, now.year)

            with self.assertRaises(ValueError):
                d = date.Date(month, 0, now.year)
            daysInThisMonth = TestDateMethods.daysInMonth(month, now.year)
            with self.assertRaises(ValueError):
                d = date.Date(month, daysInThisMonth + 1, now.year)

    @staticmethod
    def daysInYear(year):
        "Return the number of days in the given year."
        firstDayOfThisYear = datetime.date(year,     1, 1)
        firstDayOfNextYear = datetime.date(year + 1, 1, 1)
        delta = firstDayOfNextYear - firstDayOfThisYear
        return delta.days

    @staticmethod
    def daysInMonth(month, year):
        "Return the number of days in the given month of the given year."

        if month < datetime.date.max.month:
            nextMonth = month + 1
            yearOfNextMonth = year
        else:
            nextMonth = 1
            yearOfNextMonth = year + 1

        firstDayOfNextMonth = datetime.date(yearOfNextMonth, nextMonth, 1)
        firstDayOfThisMonth = datetime.date(year, month, 1)
        delta = firstDayOfNextMonth - firstDayOfThisMonth 
        return delta.days
            

if __name__ == '__main__':
    unittest.main(verbosity = 2)
