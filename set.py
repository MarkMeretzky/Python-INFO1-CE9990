"""
set.py
Print one copy of the name of each president, in chronological order. 
"""

import sys

listOfPresidents = [
    None,
    "George Washington",      # 1
    "John Adams",             # 2
    "Thomas Jefferson",       # 3
    "James Madison",          # 4
    "James Monroe",           # 5
    "John Quincy Adams",      # 6
    "Andrew Jackson",         # 7
    "Martin Van Buren",       # 8
    "William Henry Harrison", # 9
    "John Tyler",             #10
    "James K. Polk",          #11
    "Zachary Taylor",         #12
    "Millard Fillmore",       #13
    "Franklin Pierce",        #14
    "James Buchanan",         #15
    "Abrajam Lincoln",        #16
    "Andrew Johnson",         #17
    "Ulysses S. Grant",       #18
    "Rutherford B. Hayes",    #19
    "James A. Garfield",      #20
    "Chester A. Arthur",      #21
    "Grover Cleveland",       #22 (non-consecutive)
    "Benjamin Harrison",      #23
    "Grover Cleveland",       #24 (non-consecutive)
    "William McKinley",       #25
    "Theodore Roosevelt",     #26
    "William Howard Taft",    #27
    "Woodrow Wilson",         #28
    "Warren G. Harding",      #29
    "Calvin Coolidge",        #30
    "Herbert Hoover",         #31
    "Franklin D. Roosevelt",  #32
    "Harry S. Truman",        #33
    "Dwight D. Eisenhower",   #34
    "John F. Kennedy",        #35
    "Lyndon B. Johnson",      #36
    "Richard Nixon",          #37
    "Gerald Ford",            #38
    "Jimmy Carter",           #39
    "Ronald Reagan",          #40
    "George H. W. Bush",      #41
    "Bill Clinton",           #42
    "George W. Bush",         #43
    "Barack Obama",           #44
    "Donald Trump"            #45
]

dictionaryOfPresidents = {}   #Start with an empty dictionary.

for president in listOfPresidents[1:]:             #Skip the dummy item.
    if not president in dictionaryOfPresidents:
        dictionaryOfPresidents[president] = None   #Seeing him for the first time.
        print(president)

sys.exit(0)
