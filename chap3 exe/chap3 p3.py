#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      adius
#
# Created:     10/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

# Function to draw the letter "N"
def draw_N():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(140)
    turtle.left(135)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()

# Function to draw the letter "O"
def draw_O():
    turtle.circle(50)

# Set up the turtle screen
turtle.speed(1)  # Set the drawing speed (1 is slowest)
turtle.penup()
turtle.goto(-70, 0)  # Set the starting position for "N"
turtle.pendown()

# Draw the letter "N"
draw_N()

# Move to draw the letter "O"
turtle.penup()
turtle.goto(50, 0)  # Move to the right to draw "O"
turtle.pendown()

# Draw the letter "O"
draw_O()

# Close the turtle graphics window when done
turtle.done()
