"""
pandas.py

Do the same thing as two statements of pandas (lines 21 and 24),
using only the machinery covered in class.
"""

import sys
import csv
import pandas
import datetime

data = pandas.read_csv("Returns.csv")
data["Date"] = pandas.DatetimeIndex(data["Date"])

#top N themes.
n = 2

#Get top n Exp and Perf values by theme.  These are the two yellow statements.

top3LongExp = \
    data.groupby("Date")["Long Exp"].apply(lambda x: x.nlargest(n).sum())

top3LongPerf = \
    data.groupby("Date") \
    .apply(lambda x:x['Long Perf'][x['Long Exp'].nlargest(n).index].sum())

print("top3LongExp =")
print(top3LongExp)
print()

print("top3LongPerf =")
print(top3LongPerf)
print()

filename = "Returns.csv"
try:
    csvfile = open(filename, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print(f'Sorry, could not find file "{filename}".', file = sys.stderr)
    sys.exit(1)
except PermissionError:
    print(f'Sorry, no permission to open file "{filename}".', file = sys.stderr)
    sys.exit(1)

reader = csv.reader(csvfile)
next(reader) #The first line in the CSV file is a line of headers.  Skip it.

#lines is a list of tuples, each containing 3 items: date, long exp, long perf

lines = [(datetime.datetime.strptime(line[0], "%m/%d/%y").date(),
    float(line[2]), float(line[3])) for line in reader]

csvfile.close()

#dates is a list of datetime.date objects in chronological order, no duplicates.
dates = sorted(set([line[0] for line in lines]))

#For each date, sum the n highest exps.
print("my top3LongExp =")

for date in dates:
    today = [line[1] for line in lines if line[0] == date]
    highestExps = sorted(today)[-n:]
    print(f'{date:14}{sum(highestExps):.6e}')

print()

#For each date, find the n lines with the highest exps,
#and then sum the n corresponding perfs.
print("my top3LongPerf =")

for date in dates:
    today = [line for line in lines if line[0] == date]
    highestExps = sorted(today, key = lambda item: item[1])[-n:]
    s = sum([line[2] for line in highestExps]) #line[1] is exp, line[2] is perf.
    print(f'{date:14}{s:9.2f}')

sys.exit(0)
