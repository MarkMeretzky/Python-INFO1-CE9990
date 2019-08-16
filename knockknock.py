"""
knocker.py

Invite the user to tell a knock-knock joke.  Laugh appreciatively.
"""

import sys

try:
    kk = input("Tell me a knock-knock joke. ")
except EOFError:
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit(1)

try:
    name = input("Who's there? ")
except EOFError:
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit(1)

try:
    punchline = input(f"{name} who? ")
except EOFError:
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit(1)

print(f"Ha{5 * ' ha'}!")
sys.exit(0)
