principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 0
extra_payment_end_month = 12
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        sum = principal * (1+rate/12) - payment - extra_payment
        if  sum > 0:
            principal = principal * (1+rate/12) - payment - extra_payment
            total_paid = total_paid + payment+principal
        else:
            total_paid = total_paid + pricipal
            principal = 0
    else:
        sum = principal = principal * (1+rate/12) - payment
        if sum > 0:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        else:
            total_paid = total_paid + principal
            principal = 0

    months = months + 1
    print('Month: ', months, 'Total paid:', total_paid, 'Principal:', principal)
