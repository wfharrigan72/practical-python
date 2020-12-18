# bounce.py
#
# Exercise 1.5
drop_height = 100
bounce_ratio = (3/5)
last_height = drop_height
number_of_bounces = 10

for bounce in range(1,(number_of_bounces + 1)):
    this_bounce_height = bounce_ratio * last_height
    print(bounce,round(this_bounce_height,4))
    last_height = this_bounce_height
