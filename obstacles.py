import turtle as t
import random


canvas=t.Screen()
canvas.bgcolor('green')
obstacles=[]
obstacle2s=[]
game_over=False
restarted=False
touched=False
score=0
canvas.listen()


def move(x,y, turtle_name):
    turtle_name.penup()
    turtle_name.goto(x,y)


def hide():
     coin.hideturtle()


def show():
     coin.showturtle()


def moveit():
    hide()
    canvas.ontimer(show,3000)
    move(random.randint(-300,300),random.randint(-300,300),coin)
    coin.showturtle()
    coin.shape('square')
    coin.color('light blue')
     

dodger=t.Turtle()
writer=t.Turtle()
writer.hideturtle()
writer.penup()
writer2=t.Turtle()
writer2.hideturtle()
writer2.penup()


def set_turtle(turtlename):
    turtlename.speed('fastest')
    turtlename.pendown()
    if turtlename==dodger:
        turtlename.shape('circle')
        turtlename.color('blue')
        move(-200,0,dodger)
    else:
        turtlename.shape('square')
        turtlename.color('yellow')


set_turtle(dodger)


obstacle1=t.Turtle()
set_turtle(obstacle1)
obstacles.append(obstacle1)
move(150,random.randint(-150,150),obstacle1)


obstacle2=t.Turtle()
set_turtle(obstacle2)
obstacles.append(obstacle2)
move(150,random.randint(-150,150),obstacle2)


obstacle3=t.Turtle()
set_turtle(obstacle3)
obstacles.append(obstacle3)
move(150,random.randint(-150,150),obstacle3)


obstacle4=t.Turtle()
set_turtle(obstacle4)
obstacle2s.append(obstacle4)
move(random.randint(-150,150),150,obstacle4)


obstacle5=t.Turtle()
set_turtle(obstacle5)
obstacle2s.append(obstacle5)
move(random.randint(-300,300),300,obstacle5)


coin=t.Turtle()
coin.shape('square')
coin.color('light green')
move(random.randint(-300,300),random.randint(-300,300),coin)


def coin_show():
     move(random.randint(-300,300),random.randint(-300,300),coin)
     coin.shape('square')
     coin.color('light blue')


def up():
    if not game_over:
        dodger.sety(dodger.ycor()+20)
        


def down():
    if not game_over:
        dodger.sety(dodger.ycor()-20)
        


def left():
    if not game_over:
        dodger.setx(dodger.xcor()-20) 


def right():
    if not game_over:
        dodger.setx(dodger.xcor()+20)


def reset():
    global obstacle
    for obstacle in obstacles:
        move(300,random.randint(-150,150),obstacle)
        shift(obstacle)
    for obstacle in obstacle2s:
        move(random.randint(-150,150),300,obstacle)
        place_horizontal(obstacle)
    move(random.randint(-300,300),random.randint(-300,300),coin)
    move(-200,0,dodger)


def restart():
    global game_over
    writer.clear()
    dodger.color('blue')
    dodger.goto(-200,0)
    game_over=False
    reset()


def shift(obstacle_name):
    global game_over,score
    if not game_over:
        obstacle_name.setx(obstacle_name.xcor()-20)
        if obstacle_name.xcor()<-300:
            move(300,random.randint(-300,300),obstacle_name)
        if dodger.distance(obstacle_name)<20:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        if dodger.xcor()<-300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        elif dodger.xcor()>300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        elif dodger.ycor()<-300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        elif dodger.ycor()>300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        canvas.ontimer(lambda:shift(obstacle_name),10)
    else:
        canvas.onkey(restart,'r')


def place_horizontal(obstacle):
    global game_over,score
    if not game_over:
        obstacle.sety(obstacle.ycor()-20)
        if obstacle.ycor()<-300:
            move(random.randint(-150,150),300,obstacle)
        if dodger.distance(obstacle)<20:
            dodger.color('red')
            game_over=True
            writer.goto(0,0)
            writer.pendown()
            writer.write("Game over!",align='center',font=('Arial',50))
            if dodger.xcor()<-300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
            elif dodger.xcor()>300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
            elif dodger.ycor()<-300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
            elif dodger.ycor()>300:
                dodger.color('red')
                game_over=True
                writer.goto(0,0)
                writer.pendown()
                writer.write("Game over",align='center',font=('Arial',50))
                writer.penup()
        canvas.ontimer(lambda:place_horizontal(obstacle),10)
    else:
        canvas.onkey(restart,'r')


def coinyloop():
    global touched,score
    if not game_over:
        if dodger.distance(coin)<60:
            touched=True
        if touched:
            score=score+1
            writer2.goto(-150,150)
            writer2.clear()
            writer2.pendown()
            writer2.write(f"Score:{score}")
            writer2.penup()
            canvas.ontimer(coin_show,2000)
        canvas.ontimer(coinyloop,50)


dodger.penup()
obstacle1.penup()
canvas.onkey(up,'Up')
canvas.onkey(down,'Down')
canvas.onkey(left,'Left')
canvas.onkey(right,'Right')


writer2.goto(-150,150)
writer2.pendown()
writer2.write(f"Score:{score}",align='center',font=('Arial',25))
writer2.penup()


for obstacle in obstacles:
    shift(obstacle)
for obstacle in obstacle2s:
    place_horizontal(obstacle)
coinyloop()
canvas.mainloop()
#t.done()