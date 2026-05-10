from tkinter import Tk,Label,Button
tk=Tk()
tk.title("Clicker game!")
score=0
time=30
timer_label=Label(tk,text="Time:60",font=('Arial',14))
def score_up():
    global score
    if not time==0:
        score+=1
        score_label.config(text=f"Score:{score}")
def count_time():
    global time
    time-=1
    timer_label.config(text=f"Time:{time}")
    if time>0:
        tk.after(1000,count_time)
    else:
        timer_label.config(text="Times up!")
click_label=Label(tk,text="Click!",font=('Arial',15),)
score_label=Label(tk,text=f"Score:{score}",font=('Arial',15))
btn=Button(tk,text="Press me!",font=('Arial',15),command=score_up)
timer_label.pack()
score_label.pack()
btn.pack()
click_label.pack()
count_time()
tk.mainloop()