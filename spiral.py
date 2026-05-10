import turtle as t
from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])
canvas=t.Screen()
canvas.bgcolor('black')
t.speed('fastest')
def square(size,turtle_name):
    turtle_name.color(next(colors))
    for i in range(4):
        turtle_name.right(90)
        turtle_name.forward(size)
        turtle_name.color(next(colors))

def draw(size,angle,shift):
        t.color(next(colors))
        t.circle(size/2)
        t.right(angle)
        t.penup()
        t.forward(shift)
        t.pendown()
        t.color(next(colors))
        square(size,t)
        t.right(angle)
        t.penup()
        t.forward(shift)
        t.pendown()
        draw(size+1,angle,shift+1)
draw(5,10,5)
t.done()