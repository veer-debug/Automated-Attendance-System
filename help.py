from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("DEVLOPER")
        
        title_ibl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        img4=Image.open(r"Images\help.png")
        img4=img4.resize((1900,1070))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        
        bgimage=Label(self.root,image=self.photoimg4)
        bgimage.place(x=5,y=45,width=1520,height=735)
        
         
        # f_lbl=Label(bgimage,image=self.photoimg4)
        # f_lbl.place(x=60,y=130,width=250,height=300)
        
        R1=Label(bgimage,text="Email:20211468@sbsstc.ac.in",font=(" ",35,"bold"),bg="white",fg="red")
        R1.place(x=400,y=280)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
    