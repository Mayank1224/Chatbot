import tkinter as tk
from tkinter import *
root = tk.Tk()
root.maxsize(700, 700)
root.minsize(300, 300)

def send():
    send = "You => " +  e.get()
    txt.insert(END, "\n" + send)
    if(e.get() == "hello"):
        txt.insert(END, "\n" + "Bot => hi")

    elif(e.get() == "hi"):
        txt.insert(END, "\n" + "Bot => hello")

    elif(e.get() == "ok techbot"):
        txt.insert(END, "\n" + "Bot => Hey! What i can do for you")

    elif(e.get() == "what is your name"):
        txt.insert(END, "\n" + "Bot => I am techbot")

    elif(e.get() == "what you can do"):
        txt.insert(END, "\n" + "Bot => I can do anything what you want")

    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot => I am good and what about you")

    elif(e.get() == "i am also good"):
        txt.insert(END, "\n" + "Bot => That's great!")

    elif(e.get() == "who made you"):
        txt.insert(END, "\n" + "Bot => I was made by Mayank, Dharmender and Kunal")

    elif(e.get() == "what are you doing"):
        txt.insert(END, "\n" + "Bot => I am here to help you")

    elif(e.get() == "what i can do in free time"):
        txt.insert(END, "\n" + "Bot => You can read books, play games, meditate etc.")
    
    elif(e.get() == "ok thanks"):
        txt.insert(END, "\n" + "Bot => Your welcome")

    else:
        txt.insert(END, "\n" + "Bot => Sorry I didn't get it")
    e.delete(0,END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e=Entry(root, width=100)
send=Button(root, text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("CHATBOT")
root.mainloop()