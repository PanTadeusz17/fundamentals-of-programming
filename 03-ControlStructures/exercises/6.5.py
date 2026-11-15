

temperature = float(input('Enter the temperature in Celsius: '))

if temperature > 35:
    print('It is extremely hot!')
elif temperature > 30 and temperature < 36:
    print('It is hot.')
elif temperature >= 15 and temperature < 31:
    print('It is warm.')
elif temperature >= 0 and temperature < 15:
    print('It is cold.')
elif temperature < 0:
    print('Frost Warning!')