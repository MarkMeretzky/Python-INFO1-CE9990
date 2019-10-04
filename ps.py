"""
ps.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os

infile = os.popen("ps -A -o comm") #Create a child process and a pipe.
s = infile.read()                  #Slurp all the child's output into one big string.
i = infile.close()

if i:                              #i is supposed to be None.
    if i > 0:
        print(f'"ps -A -o comm" produced exit status {i >> 8}.')
    else:
        print(f'"ps -A -o comm" was killed by signal number {-i} before it could produce an exit status.')
    sys.exit(1)

lines = set(s.splitlines()[1:])   #Discard first line and extra copies of duplicate lines.   
lines = [line.rsplit("/", maxsplit = 1)[-1] for line in lines] #Remove all but last component.
lines = sorted(lines)

for i, line in enumerate(lines, start = 1):
    print(f"{i:3} {line}")

sys.exit(0)
