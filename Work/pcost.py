# pcost.py
#
# Exercise 1.27
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
running_total = 0

f = open(filename, 'rt')
headers = next(f).split(',')

for line in f:
    this_line = line.split(',')
    shares = int(this_line[1])
    cost = float(this_line[2])
    line_total = shares * cost
    running_total += line_total

print('Total cost', running_total)