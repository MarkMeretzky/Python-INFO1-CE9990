"""
listcomprehension.py

Create four new lists of strings from an existing list of strings.
"""

import sys

fortunes = [
    "You will meet a tall, dark stranger",
    "It is the hope and dreams we have that make us great",
    "Someone can read your mind",
    "A refreshing change is in your future",
    "You will be graced by the presence of a loved one soon",
    "Sometimes travel to new places leads to great transformtion",
    "Opportunities surround you if you know where to look",
    "The pleasure of what we enjoy is lost by wanting more",
    "Remember, after rain there's always sunshine",
    "Hard work is always appreciated"
]

#This does not make a copy of the list.
#allFortunes = fortunes

#One way to create a copy of a list.
#allFortunes = []
#for fortune in fortunes:
#    allFortunes.append(fortune)

#Another way to create a copy of a list.
#allFortunes = fortunes.copy()

#A third way to make a copy of a list.
allFortunes = [fortune for fortune in fortunes]
for fortune in allFortunes:
    print(fortune)

print()

bedFortunes = [fortune + " in bed" for fortune in fortunes]
for fortune in bedFortunes:
    print(fortune)

print()

shortFortunes = [fortune for fortune in fortunes if len(fortune) <= 40]
for fortune in shortFortunes:
    print(fortune)

print()

shortBedFortunes = \
    [fortune + " in bed" for fortune in fortunes if len(fortune) <= 40]

for fortune in shortBedFortunes:
    print(fortune)

sys.exit(0)
