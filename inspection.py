"""
inspection.py

Import this module to get inspection.range, which yields the inspections
of the restaurant with the given CAMIS number.
"""

import sys
import urllib.request
import io
import csv
import datetime

def inspections(camis):
    "Yield the inspections of the restaurant with the given CAMIS."
    if not isinstance(camis, int):
        raise TypeError(f"camis must be int, not {type}.")
    if camis <= 0:
        raise ValueError(f"camis must be positive, not {camis}.")

    url = "https://data.cityofnewyork.us/api/views/43nn-pn8j/rows.csv"

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
    lines = csv.reader(fileFromString)
    next(lines)                               #Skip the header line.

    #Make a list of the inspections of the restaurant we're interested in.
    inspections = [line for line in lines if int(line[0]) == camis]
    fileFromString.close()

    #Sort by inspection date field.
    inspections.sort(key =
        lambda item: datetime.datetime.strptime(item[8], "%m/%d/%Y").date())

    for inspection in inspections:
        yield inspection


if __name__ == "__main__":
    generator = inspections(41320866)   #Wo Hop, 17 Mott Street, Chinatown
    firstInspection = next(generator)
    print(firstInspection[1], firstInspection[8]) #DBA and CAMIS
    print(firstInspection[11])                    #violation description
    sys.exit(0)
