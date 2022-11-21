from tkinter import *
from googletrans import *
from googletrans import Translator

root = Tk()

root.geometry("900x600")
root.title("Language Translater")

root.configure(bg="magenta")

label_title = Label(root, text="LANGUAGE TRANSLATOR", bg = "magenta", fg="gold", font=("Freestyle Script",30,"bold"))
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label=Label(root,text="Enter Text", bg="magenta", fg="gold", font=("Freestyle Script",20))
label.place(relx=0.1, rely=0.2,anchor=W)

ta = Text(root, fg="gold",font=("Freestyle Script",15),height = 10, wrap = WORD, width = 50, padx=5,pady=5)
ta.place(relx=0.1,rely=0.5,anchor=W)

root.mainloop()


