import random as rd
import turtle as t

def draw_sqare(color : tuple):
    t.color(color)
    t.pendown()
    for i in range(4):
        t.left(90)
        t.forward(50)
    t.penup()

for i in range(36):
    color = [rd.random() for _ in range(3)]
    print(color)
    draw_sqare(color)
    t.left(10)
    