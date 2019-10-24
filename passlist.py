"""
passlist.py

Pass a list or tuple to a function that expects one argument (line 24),
and to a function that expects to receive each item on the list as a separate
argument (line 25).
"""

import sys

def threeArgs(arg0, arg1, arg2):
    "Receive and print 3 arguments."
    print(f"threeArgs: {arg0} {arg1} {arg2}")


def oneArg(arg0):
    "Receive and print 1 argument that is a list or tuple."
    assert isinstance(arg0, list) or isinstance(arg0, tuple)
    print(f'oneArg:    {" ".join(arg0)}')
     

threeArgs("Moe", "Larry", "Curly")
stooges = ["Moe", "Larry", "Curly"]
oneArg(stooges)
threeArgs(*stooges)   #The asterisk unpacks the list.
     
sys.exit(0)
