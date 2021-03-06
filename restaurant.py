"""
restaurant.py

Output the inspection results for Wo Hop, 17 Mott Street, NY, NY 10013
"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.

filename = "DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

try:
    csvfile = open(filename)
except FileNotFoundError:
    print(f'Sorry, could not find file "{filename}".', file = sys.stderr)
    sys.exit(1)
except PermissionError:
    print(f'Sorry, no permission to open file "{filename}".', file = sys.stderr)
    sys.exit(1)

lines = csv.reader(csvfile)

for line in lines:              #During each iteration, line is a list of strings.
    if line[0] == "41320866":   #CAMIS number for Wo Hop 17
        print(line[1], line[8]) #name and inspection date
        print(line[11])         #violation description
        print()

csvfile.close()
sys.exit(0)
