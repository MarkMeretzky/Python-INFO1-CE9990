"""
popular.py

List the most popular /~meretzkm/python/" web page on oit2.scps.nyu.edu,
and the number of times it was downloaded.
"""

import sys

#Fedora Linux
filename = "/var/log/httpd/access_log-20190325"

try:
    lines = open(filename)
except FileNotFoundError:
    print(f'Sorry, could not find file "{filename}".')
    sys.exit(1)
except PermissionError:
    print(f'Sorry, no permission to open file "{filename}".')
    sys.exit(1)

#How many times does each Python file appear in the access_log?
count = {}   #Start with an empty dictionary.

for line in lines:
    fields = line.split() #fields is a list of strings.
    filename = fields[6]
    if "/~meretzkm/python/" in filename \
        and (fields[8] == "200" or fields[8] == "304"):
        if filename not in count:
            count[filename] = 0
        count[filename] += 1

if len(count) == 0:
    sys.exit(1) #No "/~meretzkm/python/" lines in access_log?  Sounds suspicious.

#Find the most popular Python file and the number of times it was downloaded.
downloads = 0

for filename in count:    #Loop through all the keys in the dictionary.
    if count[filename] > downloads:
        #This file is more popular than any we've seen so far.
        mostPopular = filename
        downloads = count[filename]

print(downloads, mostPopular)
sys.exit(0)
