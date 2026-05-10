import turtle as t
import random



t.colormode(255)
color=None
correct=False
counting=True
gameover=False
current=None
score=0
time=3
lives=3
colors=['red','orange','yellow','green','blue','purple']
current=None
canvas=t.Screen()
canvas.bgcolor(0,0,0)
canvas.listen()


def move(x,y,turtle):
    turtle.penup()
    turtle.goto(x,y)


player=t.Turtle()
player.shape('circle')
player.color(255,255,255)
move(0,0,player)


writer1=t.Turtle()
move(0,50,writer1)
writer1.hideturtle()
writer1.pendown()
writer1.color(255,255,255)


red=t.Turtle()
move(-150,150,red)
red.shape('square')
red.color(colors[0])


orange=t.Turtle()
move(-75,150,orange)
orange.shape('square')
orange.color(colors[1])


yellow=t.Turtle()
move(0,150,yellow)
yellow.shape('square')
yellow.color(colors[2])


green=t.Turtle()
move(75,150,green)
green.shape('square')
green.color(colors[3])


blue=t.Turtle()
move(50,150,blue)
blue.shape('square')
blue.color(colors[4])


purple=t.Turtle()
move(150,150,purple)
purple.shape('square')
purple.color()


def countdown():
    global counting,time,score,lives,correct
    if counting:
        time-=1
        canvas.ontimer(1000,countdown)
        if time==0:
            counting=False
            if correct:
                score+=1
            else:
                lives-=1
                if lives==0:


def up():
    global gameover
    if not gameover:
        player.sety(player.ycor()+20)



def down():
    global gameover
    if not gameover:
        player.sety(player.ycor()-20)


def right():
    global gameover
    if not gameover:
        player.setx(player.xcor()+20)


def left():
    global gameover
    if not gameover:
        player.setx(player.xcor()-20)


canvas.onkey(up,"Up")
canvas.onkey(down,"Down")
canvas.onkey(right,"Right")
canvas.onkey(left,"Left")
t.done()