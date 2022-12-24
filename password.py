from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import random  
import string  


root = Tk()
root.title("Password generator")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.config(bg='#D3D3D3')


def random_string():  
    try:
        length = int(textfield.get())
        assert length >= 7 and length <=16, e
        final_string = ""
        for i in range(length):
            r = (random.choice(string.ascii_letters + string.digits + string.punctuation))
            final_string += r
        w.config(text=final_string)
    except Exception as e:
        messagebox.showerror("Password generator","Invalid Entry!!")

# label 
label1 = Label(root,text="RANDOM PASSWORD GENERATOR",font=("Helvetica",42,'bold'),fg="black",bg="#D3D3D3")
label1.place(x=90,y=80)

label2 = Label(root,text="Enter the length of the password you'd like (minimum 7, maximum 16)",font=("Helvetica",20,'bold'),fg="black",bg="#D3D3D3")
label2.place(x=180,y=180)

textfield=tk.Entry(root,justif="center",width=10,font=("MS",25,"bold"), bg="#404040",border=0,fg="white")
textfield.place(x=360,y=230)
textfield.focus()

Search_icon=PhotoImage(file="buttonFC.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=random_string)
myimage_icon.place(x=340,y=300)





w=Label(text="...",font=("arial",55,"bold"),bg="#D3D3D3",fg="black")
w.place(x=210,y=400)




root.mainloop()
