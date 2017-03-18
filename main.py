from tkinter import *
def comingSoon(event):
    text = Label(root,text="Игра станет доступна совсем скоро!",font="Helvetica 18")
    butSoon.destroy()
    text.pack()
root = Tk()
butSoon = Button(root, text="Играть!",width=30,height=5,bg="white",fg="black")
butSoon.bind("<Button-1>",comingSoon)
butSoon.pack()
root.mainloop()
