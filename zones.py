import turtle as t
import random



t.colormode(255)
color=None
correct=False
counting=True
score=0
time=3
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


def countdown():
    global counting,time,correct,score
    if counting:
        time-=1
        canvas.ontimer(1000,countdown)
        if time==0:
            counting=False
            if correct:
                score+=1


def up():
    player.sety(player.ycor()+20)



def down():
    player.sety(player.ycor()-20)


def right():
    player.setx(player.xcor()+20)


def left():
    player.setx(player.xcor()-20)


canvas.onkey(up,"Up")
canvas.onkey(down,"Down")
canvas.onkey(right,"Right")
canvas.onkey(left,"Left")
t.done()