"""
access_log.py

Print the lines in the Apache web server's access_log file that mention the
Python course.
"""

import sys

#Fedora Linux
filename = "/var/log/httpd/access_log-20190325"

try:
    lines = open(filename)
except FileNotFoundError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
except PermissionError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

for line in lines:
    if "/~meretzkm/python/" in line:
        print(line, end = "")

lines.close()
sys.exit(0)
