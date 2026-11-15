x = float(input("x = "))
y = float(input("y = "))

if x == 0 and y == 0:
    position = "in the position (0,0) of the coordinate system"
elif x == 0:
    position = "on the Y axis"
elif y == 0:
    position = "on the X axis"
elif x > 0 and y > 0:
    position = "in the first quadrant of the coordinate system"
elif x < 0 and y > 0:
    position = "in the second quadrant of the coordinate system"
elif x < 0 and y < 0:
    position = "in the third quadrant of the coordinate system"
else:
    position = "in the fourth quadrant of the coordinate system"

print(f"Point P({x},{y}) is {position}")