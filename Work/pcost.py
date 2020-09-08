# pcost.py
#
# Exercise 1.27
import gzip

total_cost = 0
with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
    headers = next(file)
    for line in file:
        data = line.split(',')
        total_cost = total_cost + int(data[1])*float(data[2])

print('Total cost', total_cost)
