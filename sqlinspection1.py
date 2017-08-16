"""
sqlinspection1.py

Store the NYC restaurant inspection results in one table in an SQLite database.
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

createTable = """\
create table inspections (
    CAMIS integer,
    DBA text,
    BORO text,
    BUILDING text,
    STREET text,
    ZIPCODE integer,
    PHONE text,
    CUISINE_DESCRIPTION text,
    INSPECTION_DATE text,
    ACTION text,
    VIOLATION_CODE text,
    VIOLATION_DESCRIPTION text,
    CRITICAL_FLAG text,
    SCORE integer,
    GRADE text,
    GRADE_DATE text,
    RECORD_DATE text,
    INSPECTION_TYPE text
)"""

insert = "insert into inspections values (" + 17 * "?, " + "?)"

#Reformat the dates from "mm/dd/yyyy" to "yyyy-mm-dd"
#so that "order by" can use them.

update = """\
update inspections
set INSPECTION_DATE =
    substr(INSPECTION_DATE, 7, 4) || "-" ||
    substr(INSPECTION_DATE, 1, 2) || "-" ||
    substr(INSPECTION_DATE, 4, 2),
GRADE_DATE =
    substr(GRADE_DATE, 7, 4) || "-" ||
    substr(GRADE_DATE, 1, 2) || "-" ||
    substr(GRADE_DATE, 4, 2),
RECORD_DATE =
    substr(RECORD_DATE, 7, 4) || "-" ||
    substr(RECORD_DATE, 1, 2) || "-" ||
    substr(RECORD_DATE, 4, 2)"""

#Wo Hop, 17 Mott Street, Chinatown.

select = """\
select DBA, INSPECTION_DATE, VIOLATION_DESCRIPTION from inspections
where CAMIS == 41320866
order by INSPECTION_DATE"""

#Create the database file, the table, and the rows.

try:
    connection = sqlite3.connect("inspections.db")
    cursor = connection.cursor()
    cursor.execute(createTable)
    next(rows)   #Don't store first line of CSV file into the SQLite table.
    cursor.executemany(insert, rows)
    fileFromString.close()
    cursor.execute(update)
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
