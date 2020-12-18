# pcost.py
#
# Exercise 1.27
import csv
running_total = 0

f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)

for this_line in rows:
    shares = int(this_line[1])
    cost = float(this_line[2])
    line_total = shares * cost
    running_total += line_total

print('Total cost', running_total)