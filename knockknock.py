"""
knocker.py

Invite the user to tell a knock-knock joke.  Laugh appreciatively.
"""

import sys

kk = input("Tell me a knock-knock joke. ")
name = input("Who's there? ")
punchline = input(name + " who? ")
print("Ha" + 5 * "ha" + "!")
sys.exit(0)
