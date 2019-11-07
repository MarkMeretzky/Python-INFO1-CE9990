"""
importer.py
Demonstrate that we can import a module we wrote.
"""

import sys
import os   #operating system

try:
    import date   #the date.py that we wrote
except ModuleNotFoundError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(f"The current directory is {os.getcwd()}")
print("The import statement searches the following directories.")
for i, dir in enumerate(sys.path, start = 1):
    print(i, dir)
print()

print("The following module has been loaded:")
print(sys.modules["date"])   #sys.modules is a dictionary.
print(f"date.__file__ = {date.__file__}")
print()

try:
    d = date.Date(12, 31, 2019)
except TypeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
except ValueError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

print(f"d = {d}")
print(f"type(d) = {type(d)}")

sys.exit(0)
