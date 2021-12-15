import random

import tkinter
root=tkinter.Tk()
root.geometry("700x450")
X=tkinter.Label(root,text='',font=("times",200))
def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    X.config(text=f'{random.choice(number)}')
    X.pack()
b=tkinter.Button(root,text="Roll",command=roll)
b.place(x=330,y=0)


root.mainloop()

