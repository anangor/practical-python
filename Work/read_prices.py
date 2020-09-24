import csv

def read_prices(rows):
    prices = {}
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except:
            pass
    return(prices)

f = open('Data/prices.csv', 'r')
rows = csv.reader(f)
prices = read_prices(rows)
print(prices)
