Speed = int(input('Enter vehicle speed: '))
TooSlow = Speed < 40
TooFast = Speed > 140

if TooFast is True:
    print('Car is going too fast!')

elif TooSlow is True:
    print('Car is going too slow!')

else:
  print('Car is going good speed!')  

