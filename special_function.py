import turtle as t
import random
import math
number=None
t.reset()
colors=['Red','Orange','Yellow','Green','Blue','Indigo','Violet']

def is_out_of_bounds(sides, length, x_p, y_p):
    # circumradius = how far the shape reaches from its starting point
    radius = length / (2 * math.sin(math.pi / sides))
    half_w = t.window_width() / 2
    half_h = t.window_height() / 2
    return (x_p + radius > half_w or x_p - radius < -half_w or
            y_p + radius > half_h or y_p - radius < -half_h)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def draw_shape(sides,length,sidecolor,fillcolor,x_p,y_p):
    move(x_p,y_p)
    t.color(sidecolor)
    t.fillcolor(fillcolor)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(180-((sides-2)*180/sides))
    t.end_fill()
while True:
    number = t.numinput("Sides", "How many sides?", minval=3)
    length = t.numinput("Length", "How long is each side?", minval=1)
    x_pos  = t.numinput("Position", "Enter the x position:", minval=-300, maxval=300)
    y_pos  = t.numinput("Position", "Enter the y position:", minval=-300, maxval=300)
    side_color=colors[random.randint(0,6)]
    fill_color=colors[random.randint(0,6)]
    if is_out_of_bounds(number, length, x_pos, y_pos):
        answer = t.textinput("Warning!", "Shape may go off screen! Draw anyway? (y/n)")
        if answer != 'y':
            continue
    draw_shape(int(number), int(length), side_color, fill_color, x_pos, y_pos)
    going = t.textinput("Continue?", "Draw another shape? (y/n)")
    if going != 'y':
        break
    t.reset()
t.done()


    