# Write a program that prints the next 20 leap years.

import datetime

current_year = datetime.datetime.now().year

if current_year % 4 != 0:
    add = 4 - (current_year % 4)
    current_year += add
for i in range(20):
    print(current_year)
    current_year += 4