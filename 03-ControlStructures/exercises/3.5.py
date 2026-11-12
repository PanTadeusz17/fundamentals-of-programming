###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

if month == 2:
    days = 28
elif month==1 or month==3 or month % 2 == 1 :
    days = 31 ## months with 31 days
elif month % 2 == 0 :
    days = 30 ## months with 30 days

## February 28 days 

print(f'Month {month} has {days} days')