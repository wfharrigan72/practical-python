# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_stop_month = 108
extra_payment = 1000
total_paid = 0.0
month = 1

while principal > 0:
    if (month >= extra_payment_start_month) and (month <= extra_payment_stop_month):
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment
    month += 1

print('Total paid', total_paid)