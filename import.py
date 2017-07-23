"""
import.py

Demonstrate that we can import a module we wrote.
"""

import sys
import date   #the date.py that we wrote

d = date.Date(12, 31, 2017)
print(d)
sys.exit(0)
