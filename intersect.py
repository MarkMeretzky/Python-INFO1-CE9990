"""
intersect.py

Print the intersection and difference of two sets.
"""

import sys
import itertools

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
    "Abraham Lincoln",        #16
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

listOfVicePresidents = [
    None,
    "John Adams",             # 1
    "Thomas Jefferson",       # 2
    "Aaron Burr",             # 3
    "George Clinton",         # 4
    "Elbridge Gerry",         # 5
    "Daniel D. Tompkins",     # 6
    "John C. Calhoun",        # 7
    "Martin Van Buren",       # 8
    "Richard M. Johnson",     # 9
    "John Tyler",             #10
    "George M. Dallas",       #11
    "Millard Fillmore",       #12
    "William R. King",        #13
    "John C. Breckinridge",   #14
    "Hannibal Hamlin",        #15
    "Andrew Johnson",         #16
    "Schuyler Colfax",        #17
    "Henry Wilson",           #18
    "William A. Wheeler",     #19
    "Chester A. Arthur",      #20
    "Thomas A. Hendricks",    #21
    "Levi P. Morton",         #22
    "Adlai Stevenson",        #23
    "Garret Hobart",          #24
    "Theodore Roosevelt",     #25
    "Charles W. Fairbanks",   #26
    "James S. Sherman",       #27
    "Thomas R. Marshall",     #28
    "Calvin Coolidge",        #29
    "Charles G. Dawes",       #30
    "Charles Curtis",         #31
    "John N. Garner",         #32
    "Henry A. Wallace",       #33
    "Harry S. Truman",        #34
    "Alben W. Barkley",       #35
    "Richard Nixon",          #36
    "Lyndon B. Johnson",      #37
    "Hubert Humphrey",        #38
    "Spiro Agnew",            #39
    "Gerald Ford",            #40
    "Nelson Rockefeller",     #41
    "Walter Mondale",         #42
    "George H. W. Bush",      #43
    "Dan Quayle",             #44
    "Al Gore",                #45
    "Dick Cheney",            #46
    "Joe Biden",              #47
    "Mike Pence"              #48
]

#Skip the dummy element.
setOfPresidents = set(listOfPresidents[1:])
setOfVicePresidents = set(listOfVicePresidents[1:])

#everyone who was a president, a vice president, or both
union = setOfPresidents | setOfVicePresidents

#people who served in both offices
intersection = setOfPresidents & setOfVicePresidents

#presidents who were never vice president
onlyPresidents = setOfPresidents - setOfVicePresidents

#vice presidents who were never president
onlyVicePresidents = setOfVicePresidents - setOfPresidents

#Must specify fillvalue because the three sets are of different lengths.
threeColumns = itertools.zip_longest(sorted(onlyPresidents),
   sorted(intersection), sorted(onlyVicePresidents), fillvalue = "")

#Widest name is 22 characters: William Henry Harrison.
f = "{:22} {:22} {}"
print(f.format("Only POTUS", "POTUS & VP", "Only VP"))
print(f.format("----------", "----------", "-------"))

for left, middle, right in threeColumns:
    print(f.format(left, middle, right))

sys.exit(0)
