"""
variablekeyword.py

Define a function that accepts a variable number of positional arguments,
followed by a variable number of keyword arguments.
"""

import sys

def PRINT(*args, **namedArgs):
    "Just like the built-in print, but prints in all uppercase."
    assert isinstance(args, tuple) and isinstance(namedArgs, dict)

    ARGS = []
    for arg in args:
        if isinstance(arg, str):
            ARGS.append(arg.upper())
        else:
            ARGS.append(arg)

    NAMEDARGS = {}
    for key, value in namedArgs.items():
        if key == "sep" or key == "end":
            NAMEDARGS[key] = value.upper()
        else:
            NAMEDARGS[key] = value

    print(*ARGS, **NAMEDARGS)


PRINT()                                #0 positional arguments
PRINT(sep = "xxx")
PRINT(end = "n\n")
PRINT(sep = "xxx", end = "n\n")
PRINT(end = "n\n", sep = "xxx")

PRINT("abe")                           #1 positional argument
PRINT("abe", sep = "xxx")
PRINT("abe", end = "n\n")
PRINT("abe", sep = "xxx", end = "n\n")
PRINT("abe", end = "n\n", sep = "xxx")

PRINT("abe", "ike")                    #2 positional arguments
PRINT("abe", "ike", sep = "xxx")
PRINT("abe", "ike", end = "n\n")
PRINT("abe", "ike", sep = "xxx", end = "n\n")
PRINT("abe", "ike", end = "n\n", sep = "xxx")

sys.exit(0)
