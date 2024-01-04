#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

# Define the draw_square function
def draw_square(side_length):
    for _ in range(4):
        turtle.pensize(5)  # Set the pensize to 5
        turtle.color("hotpink")  # Set the pen color to hotpink
        turtle.forward(side_length)  # Move forward by the specified side length
        turtle.left(90)  # Turn left 90 degrees
        turtle.speed(1)

# Set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Draw the squares
for _ in range(5):
    draw_square(20)
    turtle.penup()  # Lift the pen
    turtle.forward(40)  # Move forward to a new starting point
    turtle.pendown()  # Lower the pen

# Close the drawing window when done
turtle.done()
