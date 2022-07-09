from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1100x500")
root.config(bg="cyan")
root.title("Language Translator")

lang = list(LANGUAGES.values())
label1 = Label(root,text="Language Translator",bg="cyan")
label1.place(relx=0.5, rely = 0.1, anchor=CENTER)

input_label = Label(root,text="Enter Text",bg="white")
label1.place(relx=0.02, rely = 0.2, anchor=W)
src_language=ttk.Combobox(root,values=lang,width=20,state="readonly")
src_language.place(relx=0.13,rely=0.2,anchor=W)
src_language.set('engilsh')

output_label = Label(root,text="Output Text",bg="white")
label1.place(relx=0.81, rely = 0.2, anchor=E)
dst_language=ttk.Combobox(root,values=lang,width=20,state="readonly")
dst_language.place(relx=0.98,rely=0.2,anchor=E)
dst_language.set('Choose language')

input_text=Text(root,height=11,width=16,bg="white")
input_text.place(relx=0.02,rely=0.5,anchor=W)

output_text=Text(root,height=11,width=16,bg="white")
output_text.place(relx=0.98,rely=0.5,anchor=E)

def translate():
    translator=Translator()
    try:
        trans=translator.translate(text=input_text.get(1.0,END),src=src_language.get(),dest=dst_language.get())
        output_text.delete(1.0,END)
        output_text.insert(EMD,trans.text)
    except:
        print("try again")
        
btn = Button(root,text = "translate",command=translate)
btn.place(relx=0.5,rely=0.85,anchor=CENTER)
root.mainloop()




