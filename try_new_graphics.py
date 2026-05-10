from tkinter import*
from itertools import cycle
tk=Tk()
quotes=cycle(["Hello!","Why are you here?","Huh?"])
def clicked():
    thing_to_say=next(quotes)
    label.config(text=thing_to_say)        # text= is required!
btn=Button(tk,text='Click me',command=clicked)
btn.pack()
label=Label(tk,text="Press the button!")   # create the label
label.pack()
tk.mainloop()