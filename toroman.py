"""
toroman1.py

Convert an integer to a Roman numeral.
"""

import sys

def getInt(prompt):
    "Let the user input one integer."
    assert isinstance(prompt, str)

    try:
        s = input(prompt + " ")
    except EOFError:
        sys.exit(0)

    try:
        i = int(s)
    except ValueError:
        print(f"Sorry, \"{s}\" is not an integer.")
        sys.exit(1)

    return i


ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM", "MMMM"]

def toRoman(n):
    "Convert one integer to a Roman numeral."
    assert isinstance(n, int) and 1 <= n and n <= 4999

    s = thousands[n // 1000]
    n %= 1000                #Chop off the thousands place; means n = n % 1000

    s += hundreds[n // 100]  #means s = s + hundreds[n // 100]
    n %= 100                 #Chop off the hundreds place; means n = n % 100

    s += tens[n // 10]       #means s = s + tens[n // 10]
    n %= 10                  #Chop off the tens place; means n = n % 10

    s += ones[n]             #means s = s + ones[n]
    return s


while True:
    while True:
        n = getInt("Please type an integer in the range 1 to 4999 inclusive:")
        if 1 <= n and n <= 4999:
            break
        print(f"Sorry, {n} is out of range.")

    romanNumeral = toRoman(n)
    print(f"{n} = {romanNumeral}")
    print()
