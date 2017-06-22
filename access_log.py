"""
access_log.py

Print the lines in the Apache web server's access_log file that mention the
Python course.
"""

import sys

#Fedora Linux
filename = "/var/log/httpd/access_log-20170612"

try:
    inputfile = open(filename)
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

for line in inputfile:
    if line.find("/~meretzkm/python/") >= 0:
        print(line, end = "")

inputfile.close()
sys.exit(0)
