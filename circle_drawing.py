import turtle as t
going=y
times=None
fill_color=None
x_pos=None
y_pos=None
size=None
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def draw_loop(size,space,sidecolor,fillcolor,x_p,y_p,amount):
    move(x_p,y_p)
    t.color(sidecolor)
    t.fillcolor(fillcolor)
    t.begin_fill()
    for i in range(amount)
        t.circle(size)
        move(x_p+space,y_p+space)
while going==y
    fill_color=input("Choose a color(red,orange,yellow,green,blue,purple)")
    try:
        times=round(int(input("Enter the amount of times.(1-5)")))
    except ValueError:
        print("That's not a number!")
    if not times in range(1,6):
        print("Not through 1 and 5!")
        while not times in range(1,6):
            try:
                times=round(int(input("Enter the amount of times.(1-5)")))
            except ValueError:
                print("That's not a number!")
            if not times in range(1,6):
                print("Not through 1 and 5!")
    else:
        try:
            x_pos=round(int(input("Enter the amount of x.(1-50)")))
        except ValueError:
            print("That's not a number!")
        if not x_pos in range(1,51):
            print("Not through 1 and 50!")
            while not x_pos in range(1,51):
                try:
                    x_pos=round(int(input("Enter the amount of x.(1-50)")))
                except ValueError:
                    print("That's not a number!")
                if not times in range(1,51):
                    print("Not through 1 and 50!")
        else:
            try:
                y_pos=round(int(input("Enter the amount of y.(1-50)")))
            except ValueError:
                print("That's not a number!")
            if not y_pos in range(1,51):
                print("Not through 1 and 50!")
                while not y_pos in range(1,51):
                    try:
                        y_pos=round(int(input("Enter the amount of y.(1-50)")))
                    except ValueError:
                        print("That's not a number!")
                    if not y_pos in range(1,51):
                        print("Not through 1 and 50!")
            else:
                try:
                    size=round(int(input("Enter the size.(1-30)")))
                except ValueError:
                    print("That's not a number!")
                if not size in range(1,31):
                    print("Not through 1 and 30!")
                    while not size in range(1,31):
                        try:
                            size=round(int(input("Enter the size.(1-30)")))
                        except ValueError:
                            print("That's not a number!")
                        if not size in range(1,31):
                            print("Not through 1 and 30!")