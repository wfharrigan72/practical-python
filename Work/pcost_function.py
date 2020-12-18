# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    running_total = 0
    f = open(filename, 'rt')
    headers = next(f).split(',')
    
    for line in f:
        this_line = line.split(',')
        try:
            shares = int(this_line[1])
            cost = float(this_line[2])
            line_total = shares * cost
            running_total += line_total
        except ValueError:
            print("Couldn't parse", line)

    return running_total
    
total = portfolio_cost('Data/missing.csv')

print('Total cost', total)