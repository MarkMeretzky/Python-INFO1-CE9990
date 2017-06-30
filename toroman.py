"""
toroman1.py

Convert an integer to Roman numerals.
"""

import sys

def getInt(prompt):
    assert isinstance(prompt, str)
    try:
        s = input(prompt + " ")
    except EOFError:
        sys.exit(0)

    try:
        i = int(s)
    except ValueError:
        print("Sorry, \"", s, "\" is not an integer.", sep = "")
        sys.exit(1)

    return i


thousands = ["", "M", "MM", "MMM", "MMMM"]
hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

def toRoman(i):
    assert isinstance(i, int) and 1 <= i and i <= 4999
    s = thousands[i // 1000]
    i %= 1000               #Chop off the thousands place; means i = i % 1000

    s += hundreds[i // 100] #means s = s + hundreds[i // 100]
    i %= 100                #Chop off the hundreds place; means i = i % 100

    s += tens[i // 10]      #means s = s + tens[i // 10]
    i %= 10                 #Chop off the tens place; means i = i % 10

    s += ones[i]            #means s = s + ones[i]
    return s
    

while True:
    while True:
        i = getInt("Please type an integer in the range 1 to 4999 inclusive:")
        if 1 <= i and i <= 4999:
            break
        print("Sorry,", i, "is out of range.")

    romanNumeral = toRoman(i)
    print(i, "=", romanNumeral)
    print()
