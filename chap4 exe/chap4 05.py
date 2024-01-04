import turtle

def make_window(colr, ttle):
    """Setup window with given background color and title"""
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(color, size):
    """Sets up a new turtle with the given color and pensize"""
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.speed(0)
    return t

# Setup the canvas and turtle
wn = make_window("lightgreen", "Turtle Pattern")
tess = make_turtle("blue", 2)

def draw_pattern(angle):
    tess.pendown()
    step = 5
    for _ in range(51):
        tess.forward(step)
        tess.right(angle)
        tess.forward(step)
        tess.right(angle)
        step = step + 5

# Actual part that draws the pattern
tess.right(180)

# Draw the first spiral
tess.penup()
tess.goto(-200, 0)
draw_pattern(90)

# Draw the second spiral
tess.penup()
tess.goto(200, 0)
draw_pattern(91)

wn.mainloop()
