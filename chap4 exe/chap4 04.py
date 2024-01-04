#-------------------------------------------------------------------------------
# Name:        module8
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

tess = turtle.Turtle()
wn = turtle.Screen()

tess.speed(10)
tess.pensize(2)
tess.color('blue')
wn.bgcolor('lightgreen')

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

def draw_grid(t, sz):
    for i in range(4):
        draw_square(t, sz)
        t.left(90)

def main():
    for i in range(5):
        draw_grid(tess, 100)
        tess.left(18)

main()

turtle.done()

