"""
float.py

float.range is like the built-in range, except that the numbers can be floats.
"""

import builtins

def range(start, end, n):
    "Print n+1 equally spaced numbers, from start to end inclusive."

    if not isinstance(start, float) and not isinstance(start, int):
        raise TypeError(f"start must be float or int, not {type(start)}")
        
    if not isinstance(end, float) and not isinstance(end, int):
        raise TypeError(f"end must be float or int, not {type(end)}")

    if not isinstance(n, int):
        raise TypeError(f"n must be int, not {type(n)}")

    if n <= 0:
        raise ValueError(f"n must be positive, not {n}")

    for i in builtins.range(n + 1):   #the built-in range
        yield start + (end - start) * i / n


if __name__ == "__main__":
    import sys

    for f in range(0.0, 1.0, 10):     #the range defined in this file
        print(f)

    sys.exit(0)
