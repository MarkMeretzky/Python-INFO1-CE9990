"""
graphpaperunittest.py

These unit tests test the function draw in the file graphpaper.py.
draw expects four positive integer arguments.

test_raise makes sure draw raises a TypeError exception
if one of its four arguments is a non-integer.

test_range makes sure draw raises a ValueError exception
if one of its four arguments is a non-positive integer.

test_return makes sure draw returns the correct value.
"""

import unittest
import graphpaper

class TestGraphpaper(unittest.TestCase):

    def test_raise(self):
        n = 4   #number of arguments of graphpaper.draw
        badArgs = [None, "", 1.0, (), [], {}]    #True and False are ints.
        for i in range(n):
            for j in range(len(badArgs)):
                with self.assertRaises(TypeError):
                    args = [1 for k in range(n)] #a list of n copies of 1
                    args[i] = badArgs[j]         #Introduce a bad argument.
                    graphpaper.draw(*args

    def test_range(self):
        n = 4   #number of arguments of graphpaper.draw
        for i in range(n):
            with self.assertRaises(ValueError):
                args = [1 for j in range(n)] #a list of n copies of 1
                args[i] = 0                  #Introduce a bad argument.
                graphpaper.draw(*args)

    def test_return(self):
        n = 5   #maximum dimension
        for rowsOfBoxes in range(1, n):
            for columnsOfBoxes in range(1, n):
                for rowsOfSpaces in range(1, n):
                    for columnsOfSpaces in range(1, n):
                        top = "+" + columnsOfSpaces * "-"
                        mid = "|" + columnsOfSpaces * " "
                        tops = columnsOfBoxes * top + "\n"
                        mids = columnsOfBoxes * mid + "\n"
                        correct = rowsOfBoxes * (tops + rowsOfSpaces * mids)
                        self.assertEqual(correct, graphpaper.draw(
                            rowsOfBoxes, columnsOfBoxes,
                            rowsOfSpaces, columnsOfSpaces
                        ))


if __name__ == '__main__':
    unittest.main(verbosity = 2)
    #No need to sys.exit here, because we never return from unittest.main
    #(unless the exit = False argument is given to unittest.main).
