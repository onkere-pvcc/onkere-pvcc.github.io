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
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("nkere_om")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(0)

for x in range(5):
  for i in range(5):
    tess.forward(100)
    tess.right(144)
  tess.penup()
  tess.forward(350)
  tess.right(144)
  tess.pendown()


wn.mainloop()
