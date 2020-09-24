import csv
import sys

def pcost(archiv):
    total_cost = 0
    f = open(archiv)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            total_cost = total_cost + int(row[1])*float(row[2])
        except:
            print('Something is missing in the line')
    f.close()
    return(total_cost)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = pcost(filename)
print('Total cost:', cost)
