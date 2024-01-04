#-------------------------------------------------------------------------------
# Name:        module7
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_square(name, size):
    for i in range(4):
        name.forward(size)
        name.left(90)

    # Move the turtle to the next position
    name.penup()
    name.backward(10)
    name.right(90)
    name.forward(10)
    name.left(90)
    name.pendown()

window = turtle.Screen()
window.bgcolor('lightgreen')
window.title("nkere_om")

x = turtle.Turtle()
x.color('hotpink')
x.pensize(3)

for i in range(5):
    draw_square(x, 20 + 20 * i)

window.mainloop()

