principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
months = 0

while principal > 0:
    if months < 12:
        principal = principal * (1+rate/12) - payment- extra
        total_paid = total_paid + payment + extra
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    months = months + 1 

print('Total paid', total_paid, 'months:', months)
