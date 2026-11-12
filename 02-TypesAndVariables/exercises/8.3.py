###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

Celsius = float(input('Enter Celsius temperature: '))
Kelvin = Celsius + 273.15
Fahrenheit = (Celsius * 1.8) + 32

print(f'Temperature converted to Kelvins: {Kelvin:.2f}')
print(f'Temperature converted to Fahrenheit: {Fahrenheit:.2f}')