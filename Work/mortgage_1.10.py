# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_year = 5
years_of_extra_payments = 4
extra_payment = 1000
total_paid = 0.0
month = 1
year = 1

print ('Month','Payment','Remaining')
while principal > 0:
    if (year >= extra_payment_start_year) and (year <= (extra_payment_start_year + years_of_extra_payments)):
        total_payment = payment + extra_payment
    else:
        total_payment = payment

    if total_payment > principal:
        total_payment = principal
        principal = principal - total_payment
    else:
        principal = principal * (1+rate/12) - total_payment

    total_paid = total_paid + total_payment

    print (month,round(total_paid,2),round(principal,2))
    month += 1
    if (month % 12) == 0:
        year +=1

print('Total paid', round(total_paid,2))