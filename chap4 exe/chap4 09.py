#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_star(side_length):
    for _ in range(5):
        turtle.forward(side_length)
        turtle.right(144)

# Set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Nkere_om")

# Set up the turtle
star_turtle = turtle.Turtle()
star_turtle.color("blue")
star_turtle.pensize(2)
star_turtle.speed(1)

# Draw the star
draw_star(100)

# Close the drawing window when done
turtle.done()
