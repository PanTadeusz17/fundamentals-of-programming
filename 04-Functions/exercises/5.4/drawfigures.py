import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Side length
side_length = 100

# Draw a square
figures.draw_square(side_length)

# Finish
window.mainloop()