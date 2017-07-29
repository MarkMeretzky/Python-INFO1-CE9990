"""
tree.py

Print the tree of currently running processes listed by the macOS ps command.
"""

import sys
import os

class Process(object):
    def __init__(self, pid, ppid, command):
        assert isinstance(pid, int) and isinstance(command, str)
        self.pid = pid
        self.command = command
        self.children = [] #This newborn process has no children yet,but it will
        if pid > 0:
            parent = root.find(ppid)
            assert parent != None
            parent.children.append(self)

    def find(self, pid):
        "Find the process with the given pid. Search myself and my descendants."
        assert isinstance(pid, int)
        if self.pid == pid:
            return self
        for child in self.children:
            process = child.find(pid)
            if process != None:
                return process
        return None

    def print(self, indent):
        "Print this process and all its descendants."
        assert isinstance(indent, str)
        print("{} {:5} {}".format(indent, self.pid, self.command))
        for child in self.children:
            child.print(indent + 5 * " ")


infile = os.popen("ps -A -o 'pid ppid command'")
lines = infile.readlines()           #lines is a list of lines.
status = infile.close()

if status != None:                   #status is supposed to be None.
    print("\"ps -A -o 'pid ppid command'\" produced exit status", status)
    sys.exit(1)

root = Process(0, 0, "")  #The root process is its own parent.

for line in lines[1:]:    #Skip the header line.
    fields = line.split()
    pid = int(fields[0])
    ppid = int(fields[1])
    command = line[12:].rstrip()
    process = Process(pid, ppid, command) 

root.print("")
sys.exit(0)
