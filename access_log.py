"""
access_log.py

Print the lines in the Apache web server's access_log file that mention the
Python course.
"""

import sys

#Fedora Linux
filename = "/var/log/httpd/access_log-20170612"

try:
    lines = open(filename)
except FileNotFoundError:
    print(f"Sorry, could not find file \"{filename}\".")
    sys.exit(1)
except PermissionError:
    print(f"Sorry, no permission to open file \"{filename}\".")
    sys.exit(1)

for line in lines:
    if "/~meretzkm/python/" in line:
        print(line, end = "")

lines.close()
sys.exit(0)
