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

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle object
polygon_turtle = turtle.Turtle()
polygon_turtle.speed(1)  # Set the drawing speed (1 is slowest)

# Function to draw a regular polygon
def draw_polygon(num_sides, side_length):
    angle = 360 / num_sides
    for _ in range(num_sides):
        polygon_turtle.forward(side_length)
        polygon_turtle.right(angle)

# Draw an equilateral triangle
draw_polygon(3, 100)

# Move to a new position
polygon_turtle.penup()
polygon_turtle.goto(-150, 0)
polygon_turtle.pendown()

# Draw a square
draw_polygon(4, 100)

# Move to a new position
polygon_turtle.penup()
polygon_turtle.goto(150, 0)
polygon_turtle.pendown()

# Draw a hexagon
draw_polygon(6, 100)

# Move to a new position
polygon_turtle.penup()
polygon_turtle.goto(-200, -150)
polygon_turtle.pendown()

# Draw an octagon
draw_polygon(8, 100)

# Close the turtle graphics window when done
wn.exitonclick()
