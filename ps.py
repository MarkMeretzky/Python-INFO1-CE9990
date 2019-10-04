"""
ps.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os

infile = os.popen("ps -A -o comm")   #Create a child process and a pipe.
lines = infile.readlines()           #lines is a list of lines.
i = infile.close()

if i:                                #i is supposed to be None.
    if i > 0:
        print(f'"ps -A -o comm" produced exit status {i >> 8}.')
    else:
        print(f'"ps -A -o comm" was killed by signal number {-i} before it could produce an exit status.')
    sys.exit(1)

lines = set(lines[1:])                          #Remove 1st item & extra copies.
lines = [line.rstrip() for line in lines]       #Remove trailing newline.
lines = [line.split("/")[-1] for line in lines] #Remove all but last component.
lines = sorted(lines)

for i, line in enumerate(lines, start = 1):
    print(f"{i:3} {line}")

sys.exit(0)
