"""
served.py

Print in alphabetical order one copy of the name of each /~meretzkm/python/ file
that has been served out by the web server on the host oit2.scps.nyu.edu.
"""

import sys

filename = "/var/log/httpd/access_log-20170612"   #Fedora Linux

try:
    lines = open(filename)
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

served = set()              #Start with an empty set.

for line in lines:          #line is a string.
    fields = line.split()   #fields is a list of strings.
    filename = fields[6]    #filename is a string.
    if "/~meretzkm/python/" in filename:
        served.add(filename)

lines.close()

for i, filename in enumerate(sorted(served), start = 1):
    print("{:3} {}".format(i, filename))

sys.exit(0)
