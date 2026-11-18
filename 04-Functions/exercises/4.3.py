import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input('Enter length of the first side: '))
b = float(input('Enter length of the second side: '))
c = float(input('Enter length of the third side: '))

result = triangle_area(a, b, c)
print(f'The area of a triangle with sides {a}, {b}, {c} is {result}')