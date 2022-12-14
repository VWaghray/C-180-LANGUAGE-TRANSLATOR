from tkinter import *
from googletrans import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk

root = Tk()

root.geometry("1080x600")
root.title("Language Translater")

root.configure(bg="black")

language = list(LANGUAGES.values())



label_title = Label(root, text="LANGUAGE TRANSLATOR", bg = "black", fg="gold", font=("Freestyle Script",30,"bold"))
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label=Label(root,text="Enter Text", bg="black", fg="gold", font=("Freestyle Script",20))
label.place(relx=0.1, rely=0.2,anchor=W)

cb1 = ttk.Combobox(state = 'readonly', values=language,width=22)
cb1.place(relx=0.3,rely=0.2,anchor=W)
cb1.set("english")

ta1 = Text(root, fg="gold",font=("Freestyle Script",15),height=11, wrap = WORD, width = 60, padx=5,pady=5)
ta1.place(relx=0.02,rely=0.5,anchor=W)
label1=Label(root,text="Output", bg="black", fg="gold", font=("Freestyle Script",20))
label1.place(relx=0.7, rely=0.2,anchor=E)

cb2 = ttk.Combobox(state = 'readonly', values=language,width=22)
cb2.place(relx=0.9,rely=0.2,anchor=E)
cb2.set("Select Output Language")

ta2 = Text(root, fg="gold",font=("Freestyle Script",15), wrap = WORD, width = 60, height=11,padx=5,pady=5)
ta2.place(relx=0.98,rely=0.5,anchor=E)


def Translate():
    translator=Translator()
    try:
        translated = translator.translate(text=ta1.get(1.0,END), src = cb1.get(), dest = cb2.get())
        ta2.delete(1.0,END)
        ta2.insert(END, translated.text)
    except:
        print("Try Again")    
        
btn = Button(text='Translate', bg="magenta", fg="gold", font=("Freestyle Script",20), command=Translate)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)
        
root.mainloop()


