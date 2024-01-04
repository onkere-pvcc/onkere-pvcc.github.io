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
import math

# Create a turtle screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle object
clock_turtle = turtle.Turtle()
clock_turtle.speed(0)  # Set the drawing speed (0 is fastest)

# Function to draw a circle
def draw_circle(radius):
    clock_turtle.penup()
    clock_turtle.goto(0, -radius)
    clock_turtle.pendown()
    clock_turtle.circle(radius)

# Function to draw clock ticks
def draw_ticks(radius, num_ticks):
    angle = 360 / num_ticks
    for _ in range(num_ticks):
        clock_turtle.penup()
        clock_turtle.goto(0, -radius)
        clock_turtle.pendown()
        clock_turtle.forward(0.1 * radius)
        clock_turtle.penup()
        clock_turtle.goto(0, 0)
        clock_turtle.right(angle)

# Draw the clock face
draw_circle(150)  # Outer circle
draw_circle(140)  # Inner circle
draw_circle(10)   # Center point
draw_ticks(140, 12)  # Draw 12 ticks for hours

# Close the turtle graphics window when done
wn.exitonclick()
