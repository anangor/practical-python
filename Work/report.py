# report.py
#
# Exercise 2.4
import csv
import sys

def read_port(f_name):
    portfolio = []
    f = open(f_name)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            holding = {'name': row[0], 'shares' : int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        except:
            print('Something is missing in the line')
    f.close()
    return(portfolio)

def read_prices(rows):
    prices = {}
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except:
            pass
    return(prices)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

f = open('Data/prices.csv', 'r')
rows = csv.reader(f)

portfolio = read_port(filename)
prices = read_prices(rows)

total = 0

for s in portfolio:
    total += s['shares']*prices[s['name']] - s['shares']*s['price']

print(total)
