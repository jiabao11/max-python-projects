import turtle as t
import random


t.colormode(255)
color=None
correct=False
counting=False
gameover=False
current=None
score=0
time=3
lives=3
colors=['red','orange','yellow','green','blue','purple']
current=None
proper=None
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


writer2=t.Turtle()
move(-150,160,writer2)
writer2.hideturtle()
writer2.pendown()
writer2.color(255,255,255)
writer2.write(f"Score:{score}",align='center',font=('Arial',25))
move(-150,150,writer2)
writer2.pendown()



red=t.Turtle()
move(-200,150,red)
red.shape('square')
red.color(colors[0])


orange=t.Turtle()
move(-120,150,orange)
orange.shape('square')
orange.color(colors[1])


yellow=t.Turtle()
move(-40,150,yellow)
yellow.shape('square')
yellow.color(colors[2])


green=t.Turtle()
move(40,150,green)
green.shape('square')
green.color(colors[3])


blue=t.Turtle()
move(120,150,blue)
blue.shape('square')
blue.color(colors[4])


purple=t.Turtle()
move(200,150,purple)
purple.shape('square')
purple.color(colors[5])
pairs={colors[0]:red,colors[1]:orange,colors[2]:yellow,colors[3]:green,colors[4]:blue,colors[5]:purple}


def startcount():
    global counting
    counting=True
    player.goto(0,0)


def switch():
    player.color(255,255,255)


def countdown():
    global counting,time,score,lives,correct,gameover
    startcount()
    if counting:
        time-=1
        move(0,50,writer1)
        writer1.pendown()
        writer1.color(random.choice(colors))
        writer1.write(f"In {time}")
        canvas.ontimer(1000,countdown)
        if time==0:
            counting=False
            if correct:
                score+=1
                writer2.clear()
                writer2.write(f"Score:{score}",align='center',font=('Arial',25))
            else:
                lives-=1
                if lives==0:
                    gameover=True
                    writer1.color(255,255,255)
                    writer1.write('Game over!',align='center',font=('Arial',50))
                else:
                    player.color(255,0,0)
                    canvas.ontimer(switch,100)


def mainloop():
    pass


def sense():
    global proper,correct
    proper=random.choice(list(pairs.values()))
    while counting:
        if proper.distance(player)<60:
            correct=True

def up():
    global gameover
    if not gameover:
        player.sety(player.ycor()+10)



def down():
    global gameover
    if not gameover:
        player.sety(player.ycor()-10)


def right():
    global gameover
    if not gameover:
        player.setx(player.xcor()+10)


def left():
    global gameover
    if not gameover:
        player.setx(player.xcor()-10)


canvas.onkey(up,"Up")
canvas.onkey(down,"Down")
canvas.onkey(right,"Right")
canvas.onkey(left,"Left")
t.done()