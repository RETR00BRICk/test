import turtle as t

'''t.shape("turtle")
t.pensize(5)
t.color("#2eff25")
t.color((0.1, 0.4, 0.6))
t.fillcolor("orange")

t.forward(100)
t.right(80)
t.forward(40)
t.left(50)
t.back(100)

t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(-100,100)
t.pendown()
t.circle(200)'''

screen = t.Screen()
#screen.onkey(lambda: t.up(), 'w')
#screen.onkey(lambda: t.down(), 's')
#screen.onkey(lambda: t.left(), 'a')
screen.onclick(lambda x,y: t.goto(x,y))

screen.listen()

t.done()