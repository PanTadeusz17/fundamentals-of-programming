###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures
# First square
pen.penup()
pen.goto(-250, 200)
pen.pendown()
figures.draw_square(pen, 80)

# Second square
pen.penup()
pen.goto(-250, 0)
pen.pendown()
figures.draw_square(pen, 60)

# First triangle
pen.penup()
pen.goto(-50, 120)
pen.pendown()
figures.draw_triangle(pen, 90)

# Second triangle
pen.penup()
pen.goto(-50, -80)
pen.pendown()
figures.draw_triangle(pen, 70)

# First rectangle
pen.penup()
pen.goto(120, 200)
pen.pendown()
figures.draw_rectangle(pen, 120, 60)

# Second rectangle
pen.penup()
pen.goto(120, 0)
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()