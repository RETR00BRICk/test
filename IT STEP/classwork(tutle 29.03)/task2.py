import turtle as t

def draw_house():
    t.color("yellow")
    t.begin_fill()
    for i in range(4):
        t.left(90)
        t.forward(100)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(120)
    t.color("red")
    t.right(180)
    t.begin_fill()
    for i in range(3):
        t.forward(140)
        t.left(120)
    t.end_fill()
    t.penup()

def draw_star():
    t.color("blue")
    t.pendown()
    for i in range(5):
        t.left(144)
        t.forward(200)
    t.penup()

draw_house()
t.forward(400)
draw_star()
t.done()