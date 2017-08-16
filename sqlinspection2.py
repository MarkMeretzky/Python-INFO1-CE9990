"""
sqlinspection2.py

Store the NYC restaurant inspection results in two tables in an SQLite database.
"""

import sys
import urllib.request
import io
import csv
import sqlite3
import datetime
import textwrap   #no output lines will be longer than 80 characters

url = "https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv" \
    "?accessType=DOWNLOAD"

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read()
fileFromUrl.close()

#New York City encoded this file twice, so we have to decode it twice.

try:
    s = sequenceOfBytes.decode("utf-8")   #s is a string
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

#Change s back into a sequence of bytes so we can decode it again.
listOfInts = [ord(c) for c in s]
sequenceOfBytes = bytes(listOfInts)

try:
    s = sequenceOfBytes.decode("utf-8")   #s is a string
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

fileFromString = io.StringIO(s)
rows = csv.reader(fileFromString)

#SQLite commands

createRestaurantsTable = """\
create table restaurants (
    CAMIS integer primary key,
    DBA text,
    BORO text,
    BUILDING text,
    STREET text,
    ZIPCODE integer,
    PHONE text,
    CUISINE_DESCRIPTION text
)"""

createInspectionsTable = """\
create table inspections (
    INSPECTION_DATE text,
    ACTION text,
    VIOLATION_CODE text,
    VIOLATION_DESCRIPTION text,
    CRITICAL_FLAG text,
    SCORE integer,
    GRADE text,
    GRADE_DATE text,
    RECORD_DATE text,
    INSPECTION_TYPE text,
    CAMIS integer,
    foreign key(CAMIS) references restaurants(CAMIS)
)"""

insertIntoRestaurants = "insert into restaurants values (" +  7 * "?, " + "?)"
insertIntoInspections = "insert into inspections values (" + 10 * "?, " + "?)"

#Wo Hop, 17 Mott Street, Chinatown.

select = """\
select restaurants.DBA, inspections.INSPECTION_DATE,
inspections.VIOLATION_DESCRIPTION from restaurants, inspections
where restaurants.CAMIS == 41320866
and restaurants.CAMIS == inspections.CAMIS
order by INSPECTION_DATE"""

#Create the database file, the tables, and the rows.

try:
    connection = sqlite3.connect("inspections.db")
    cursor = connection.cursor()
    cursor.execute(createRestaurantsTable)
    cursor.execute(createInspectionsTable)

    camises = set() #Start with an empty set of integers.
    next(rows)      #Don't store first line of CSV file into the SQLite table.

    for row in rows:
        camis = int(row[0])
        if not camis in camises:
            #This is the first time we have encountered this restaurant.
            camises.add(camis)
            cursor.execute(insertIntoRestaurants, row[:8])

        #Change the three date fields from "mm/dd/yyyy" to "yyyy-mm-dd".
        for i in (8, 15, 16):
            if row[i] != "":
                fields = row[i].split("/")
                row[i] = "-".join((fields[2], fields[0], fields[1]))

        cursor.execute(insertIntoInspections, row[8:] + [camis])
            
    fileFromString.close()   
    connection.commit()
except sqlite3.Error as error:
    print(error)
    sys.exit(1)

#Search the table for all Wo Hop rows.

try:
    cursor.execute(select)
    rows = cursor.fetchall()   #rows is a list
except sqlite3.Error as error:
    print(error)
    sys.exit(1)

for row in rows:
    #Change row[1] (the INSPECTION_DATE) from a string in the format
    #"YYYY-MM-DD" to an object of class datetime.date.
    d = datetime.datetime.strptime(row[1], "%Y-%m-%d").date()
    print(row[0], d.strftime("%A, %B %-d, %Y"))
    
    #Split row[2] (the VIOLATION_DESCRIPTION) into a list of strings
    #that are each at most 80 characters long.
    lines = textwrap.wrap(row[2], width = 80)
    for line in lines:
        print(line)

    print()

try:
    cursor.close()
    connection.close()
except sqlite3.Error as error:
    print(error)
    sys.exit(1)

sys.exit(0)
