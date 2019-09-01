"""
split.py

Split a string into a list of strings.
"""

import sys

preamble = """\
We hold these truths to be self-evident,
that all men are created equal,
that they are endowed by their Creator with certain unalienable Rights,
that among these are Life, Liberty, and the pursuit of Happiness."""

print(preamble)                  #preamble is one big string.  It is not a list.
print()

phrases = preamble.split(",\n")   #phrases is a list of 4 strings
for phrase in enumerate(phrases, start = 1):
    print(phrase)

print()

words = preamble.split()         #words is a list of 35 strings
for word in enumerate(words, start = 1):
    print(word)

sys.exit(0)
