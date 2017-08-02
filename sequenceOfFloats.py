"""
sequenceOfFloats.py

Loop through a sequence of floats.
"""

import sys
import float   #We wrote this module.  It's in the file float.py.

for f in float.range(0.0, 1.0, 10):   #a sequence of 11 floats
    print(f)
print()

for f in float.range(0.0, 10.0, 3):   #a sequence of 4 floats
    print(f)
print()

r = float.range(0.0, 1.0, 10)
print("type(r) =", type(r))
      
if .7 in r:
    print(".7 is in the range.")
else:
    print(".7 is not in the range.")

sys.exit(0)
