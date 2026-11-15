###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

if month == 2:
    days = 28 ## February 28 days 
elif (month <= 7 and month % 2 == 1) or (month >= 8 and month % 2 == 0):
    days = 31 ## months with 31 days
else:
    days = 30 ## months with 30 days

print(f'Month {month} has {days} days')