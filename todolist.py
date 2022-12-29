from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox


root = Tk()
root.title("To-do List")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.config(bg='#D3D3D3')


lsb = Listbox(root, height=15, width=50, font=("MS", 20, "bold"), fg='black', bg="white")
lsb.pack()
lsb.place(x=80, y = 110)



def add():
    lsb.insert(END, textfield.get())
    textfield.delete(0,END)
  
def delete():
    # whatever the cursor selects is what should be deleted
    lsb.delete(lsb.curselection())


textfield=tk.Entry(root,width=26,font=("MS",30,"bold"), bg="white",border=0,fg="black")
textfield.place(x=40,y=40)
textfield.focus()


enter_icon=PhotoImage(file="UU.png")
myimage_icon=Button(image=enter_icon,borderwidth=0,cursor="hand2",bg="#D3D3D3",command=add)
myimage_icon.place(x=650,y=42)

garbage_icon=PhotoImage(file="garbage.png")
myimage_icon=Button(image=garbage_icon,borderwidth=-1,cursor="hand2",bg="#D3D3D3",command=delete, highlightthickness=0)
myimage_icon['bg'] = '#D3D3D3'
myimage_icon.place(x=800,y=400)



root.mainloop()
