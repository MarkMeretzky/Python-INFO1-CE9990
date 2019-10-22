"""
passlist.py

Pass a list or tuple to a function that expects one argument (line 21),
and to a function that expects to receive each item on the list as a separate
argument (line 22).
"""

import sys

def threeArgs(arg0, arg1, arg2):
    print(f"threeArgs: {arg0} {arg1} {arg2}")

def oneArg(arg0):
    assert isinstance(arg0, list) or isinstance(arg0, tuple)
    print(f'oneArg:    {" ".join(arg0)}')

threeArgs("Moe", "Larry", "Curly")

stooges = ["Moe", "Larry", "Curly"]
oneArg(stooges)
threeArgs(*stooges)
sys.exit(0)
