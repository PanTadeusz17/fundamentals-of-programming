###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math

r = float(input('Enter radius of the circle: '))
area = r**2 * math.pi 
circumference = 2 * math.pi * r
print(f'Area of the circle is {area:.2f}')
print(f'Circumference of the circle is {circumference:.2f}')