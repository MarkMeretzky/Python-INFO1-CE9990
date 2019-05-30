"""
floatdemo.py

Demonstrate the generator float.range.
"""

import sys
import float   #the module float.py that we wrote

#The built-in range: print the integers from 0 to 10 inclusive.
for i in range(10 + 1):
    print(i)
print()

try:
    #The range we wrote: print 11 equally spaced numbers from 0.0 to 10.0 inclusive.
    for f in float.range(0.0, 1.0, 10):
        print(f)
    print()

    if .7 in float.range(0.0, 1.0, 10):
        print(".7 is in the float.range.")
    else:
        print(".7 is not in the float.range.")

except TypeError as error:
    print(error)
    sys.exit(1)
except ValueError as error:
    print(error)
    sys.exit(1)

sys.exit(0)
