import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("red")
    elif 100 <= height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

    t.begin_fill()
    t.left(90)

    if height >= 0:
        t.forward(height)
    else:
        t.forward(0)  # Set the bar height to 0 for negative values

    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)

    if height >= 0:
        t.forward(height)
    else:
        t.forward(0)  # Set the bar height to 0 for negative values

    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, -200, 240, -160, 260, 220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
