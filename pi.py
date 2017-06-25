"""
pi.py

Compute the value of pi using the Monte Carlo method.
Generate n random points, each lying in the 1 by 1 square whose lower left
corner is at the origin.  Count how many of these points fall in the upper right
quadrant of the unit circle centered at the origin.  The fraction count/n is the
fraction of the square that is occupied by the quadrant.
"""

import sys
import random
import math

n = 10_000_000   #how many pairs of random numbers.  Underscores ignored.
count = 0

i = 0
while i < n:
    x = random.random()         #a random number in the range 0 <= x < 1
    y = random.random()         #another random number in the same range
    distance = math.hypot(x, y) #distance from (0, 0) to (x, y)
    if distance <= 1:           #if the point (x, y) is in or on the circle,
        count += 1
    i += 1

estimatedPi = 4 * count / n     #4 is the area of the 2 by 2 square
print("estimated pi = ", estimatedPi)
print("     real pi = ", math.pi)
print("       error = ", abs(estimatedPi - math.pi))
sys.exit(0)
