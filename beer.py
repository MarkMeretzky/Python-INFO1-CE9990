"""
beer.py

Output the lyrics to "A Hundred Bottles of Beer on the Wall. 
"""

import sys

for b in range(100, -1, -1):
    print(f"{b} bottles of beer on the wall,")
    print(f"{b} bottles of beer on the wall--")
    print("If one of those bottles should happen to fall,")
    print(f"{b} bottles of beer on the wall.")

    print()
    #time.sleep(3)

sys.exit(0)
