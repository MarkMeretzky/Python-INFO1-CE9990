"""
sparse1.py

Make a sparse list, i.e., a list whose items are mostly None.
"""

import sys

buildings = [
    None, #dummy
    None, #  1st Street
    None, #  2nd Street
    None, #  3rd Street
    None, #  4th Street
    None, #  5th Street
    None, #  6th Street
    None, #  7th Street
    None, #  8th Street
    None, #  9th Street
    None, # 10th Street
    None, # 11th Street
    None, # 12th Street
    None, # 13th Street
    "The Con Ed Building", # 14th Street
    None, # 15th Street
    None, # 16th Street
    None, # 17th Street
    None, # 18th Street
    None, # 19th Street
    None, # 20th Street
    None, # 21st Street
    None, # 22nd Street
    "The Met Life Tower", # 23rd Street
    None, # 24th Street
    None, # 25th Street
    None, # 26th Street
    None, # 27th Street
    None, # 28th Street
    None, # 29th Street
    None, # 30th Street
    None, # 31st Street
    None, # 32nd Street
    None, # 33rd Street
    "The Empire State Building", # 34th Street
    None, # 35th Street
    None, # 36th Street
    None, # 37th Street
    None, # 38th Street
    None, # 39th Street
    None, # 40th Street
    None, # 41st Street
    "Grand Central Terminal", # 42nd Street
    None, # 43rd Street
    None, # 44th Street
    None, # 45th Street
    None, # 46th Street
    None, # 47th Street
    None, # 48th Street
    "The RCA Building", # 49th Street
    None, # 50th Street
    None, # 51st Street
    None, # 52nd Street
    None, # 53rd Street
    None, # 54th Street
    None, # 55th Street
    None, # 56th Street
    None, # 57th Street
    None, # 58th Street
    "The Plaza", # 59th Street
    None, # 60th Street
    None, # 61st Street
    None, # 62nd Street
    None, # 63rd Street
    None, # 64th Street
    None, # 65th Street
    None, # 66th Street
    None, # 67th Street
    None, # 68th Street
    None, # 69th Street
    None, # 70th Street
    None, # 71st Street
    "The Dakota", # 72nd Street
    None, # 73rd Street
    None, # 74th Street
    None, # 75th Street
    None, # 76th Street
    None, # 77th Street
    None, # 78th Street
    None, # 79th Street
    None, # 80th Street
    None, # 81st Street
    "The Met", # 82nd Street
    None, # 83rd Street
    None, # 84th Street
    None, # 85th Street
    None, # 86th Street
    None, # 87th Street
    "The Guggenheim", # 88th Street
    None, # 89th Street
    None, # 90th Street
    None, # 91st Street
    None, # 92nd Street
    None, # 93rd Street
    None, # 94th Street
    None, # 95th Street
    None, # 96th Street
    None, # 97th Street
    None, # 98th Street
    None, # 99th Street
    "Mount Sinai" #100th Street
]

while True:
    try:
        st = int(input("Please type a street number (e.g., 42): "))
    except:  #if user did not type a valid int
        sys.exit(0)

    if 0 <= st and st < len(buildings) and buildings[st] != None:
        b = buildings[st]
    else:
        b = "Nothing famous"

    print(b, "is on that street.")
    print()
