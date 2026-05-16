import turtle as t
import random
from itertools import cycle as c
t.colormode(255)
t.register_shape('rectangle',(
    (-300,275),(300,275),(300,300),(-300,300)
))
t.penup()
t.goto(-300,275)
t.color(255,0,0)
t.shape('rectangle')
t.pendown()
t.speed('fastest')
t.done()