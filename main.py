import re
from tkinter import *
lang = 0
def comingSoon(event):
    coming = Toplevel()
    global locale
    text = Label(coming,text=locale[1],font="Helvetica 18")
    text.pack()
    coming.focus_set()
    coming.transient(root)
    coming.grab_set()
    coming.wait_window()
    butSoon.destroy()
def chooseEnglish(event):
    global lang
    lang=1
def chooseRussian(event):
    global lang
    lang=2
def chooseCustom(event):
    global lang
    lang=3
root = Tk()
text = Label(root,text="Choose you locale",font="Arial 18")
text.pack()
butEng = Button(root, text="English",width=30,height=5,bg="white",fg="black")
butEng.bind("<Button-1>",chooseEnglish)
butEng.pack()
butRus = Button(root, text="Русский",width=30,height=5,bg="white",fg="black")
butRus.bind("<Button-2>",chooseRussian)
butRus.pack()
butCst = Button(root, text="Custom",width=30,height=5,bg="white",fg="black")
butCst.bind("<Button-3>",chooseCustom)
butCst.pack()
butSoon = Button(root, text="I want to play!",width=30,height=5,bg="white",fg="black")
butSoon.bind("<Button-4>",comingSoon)
butSoon.pack()
locales = open('lang.tgg', 'r', 1)
localestring = locales.readline()
i = 0
locale = {}
while localestring:
    wordL = ""
    if(lang==1):
        word = re.findall(r'[\d]+ (.+)\/.+\/.+', localestring)
    if(lang==2):
        word = re.findall(r'[\d]+ .+\/(.+)\/.+', localestring)
    if(lang==3):
        word = re.findall(r'[\d]+ .+\/.+\/(.+)', localestring)
    word = ''.join(wordL)
    association = { i : word }
    locale.update(association)
    localestring = locales.readline()
    i = i + 1

root.mainloop()
