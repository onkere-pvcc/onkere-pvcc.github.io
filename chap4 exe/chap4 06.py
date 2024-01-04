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

def make_window(colr, ttle):
  """ setup window with given background color and title """

  w = turtle.Screen()
  w.bgcolor(colr)
  w.title(ttle)
  return w

def make_turtle(color, size):
  """ sets up new turtle with given color and pensize """
  t = turtle.Turtle()
  t.color(color)
  t.pensize(size)
  t.speed(1)
  return t

def draw_poly(t, n, sz):
  """ non-fruitful function that draws a regular polygon """
  t.pendown()
  for i in range(n):
    t.forward(sz)
    t.left(360 / n)
  t.penup()

def draw_equitriangle(t, sz):
  draw_poly(t, 3, sz)

""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", "nkere_om")
tess = make_turtle("blue" , 2)

""" actual part that draws the polygon """
draw_equitriangle(tess, 90)

# Close the drawing window when done
turtle.done()
