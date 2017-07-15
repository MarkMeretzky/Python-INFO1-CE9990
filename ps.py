"""
ps.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os

infile = os.popen("ps -A -o comm")   #Create a child process and a pipe.
lines = infile.readlines()           #lines is a list of lines.
status = infile.close()

if status != None:                   #status is supposed to be None.
    print("\"ps -A -o comm\" produced exit status", status)
    sys.exit(1)

lines = set(lines[1:])                          #Remove 1st item & extra copies.
lines = [line.rstrip() for line in lines]       #Remove trailing newline.
lines = [line.split("/")[-1] for line in lines] #Remove all but last component.
lines = sorted(lines)

for i, line in enumerate(lines):
    print("{:3} {}".format(i, line))

sys.exit(0)
