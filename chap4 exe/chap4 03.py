#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

# Function to draw a regular polygon
def draw_poly(t, n, sz):
    angle = 360 / n  # Calculate the angle for each side
    for _ in range(n):
        t.forward(sz)  # Move forward by the given side length
        t.left(angle)  # Turn left by the calculated angle

# Set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Set up the turtle
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

# Call the draw_poly function to draw a regular polygon
draw_poly(tess, 8, 50)  # Draws an octagon with side length 50 units

# Close the drawing window when done
turtle.done()
