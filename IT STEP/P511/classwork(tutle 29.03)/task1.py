import turtle as t

t.color("red")
for i in range(4):
    t.left(90)
    t.forward(20)
t.penup()
t.forward(50)
t.color("green")
t.pendown()
for i in range(3):
    t.left(120)
    t.forward(20)
t.penup()
t.forward(50)
t.color("blue")
t.pendown()
for i in range(5):
    t.left(72)
    t.forward(20)

t.done()