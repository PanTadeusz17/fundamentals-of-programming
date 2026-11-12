

ticket = int(input('Enter the ticket (hours of parking): '))
fee = 0

if ticket == 1 or ticket == 2:
    fee += 5    
elif ticket >= 3 and ticket <= 6:
    fee += 15
elif ticket > 6:
    fee += 20

print(f'Your fee is {fee}zl.')
    