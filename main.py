from tkinter import *
from tkinter import ttk
import tkinter
import os
import datetime
from time import strftime
from PIL import Image,ImageTk,ImageFilter
from student import Student
from train import train
from face_recognition import Face_Recognition
from devloper import Devloper
from help import Help
from attendance import Attendance




class Face_Recogination_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recoginition System")
        self.root.title("Home Page")
        self.root.iconbitmap(r"Images\logo.ico")
        
        # --------------------------------------------------------------
        
        img1=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\14.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=5,y=0,width=500,height=130)
        
        
        img2=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\01_home.png")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=500,height=130)
        
        
        img3=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\12_home.webp")
        img3=img3.resize((500,130))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1015,y=0,width=500,height=130)
        
        
        
        # background image
        img4=Image.open(r"Images\back_home.png")
        img4=img4.resize((1530,650))
        self.photoimg4=ImageTk.PhotoImage(img4)
        # img4=img4.filter(ImageFilter.BLUR)
        
        bgimage=Label(self.root,image=self.photoimg4)
        bgimage.place(x=5,y=130,width=1510,height=650)
        # -------------------------------------------------------------
        
        title_ibl=Label(bgimage,text="AUTOMATE  ATTENDANCE  SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_ibl.place(x=-3,y=0,width=1530,height=45)
        
        
        # time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_ibl,font=('times new roman',18,'bold'),background='white',foreground='red')
        lbl.place(x=1300,y=(-15),width=200,height=70)
        time()
        
        # student Buttens
        img5=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\03_home.jpg")
        img5=img5.resize((150,150))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bgimage,image=self.photoimg5,command=self.student_detail,cursor="hand2")
        b1.place(x=160,y=100,width=150,height=150)

        b1_1=Button(bgimage,text="Student ",command=self.student_detail,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_1.place(x=160,y=240,width=150,height=30)
        
        # Detect face butten
        img6=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\06_home.webp")
        img6=img6.resize((150,150))
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b2=Button(bgimage,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=150,height=150)

        b1_2=Button(bgimage,text="Face Detector ",cursor="hand2",command=self.face_data,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_2.place(x=500,y=240,width=150,height=30)
        
        # Attandance face butten
        img7=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\05_home.png")
        img7=img7.resize((150,150))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b3=Button(bgimage,image=self.photoimg7,cursor="hand2",command=self.attendance)
        b3.place(x=800,y=100,width=150,height=150)

        b1_3=Button(bgimage,text="Attendance ",cursor="hand2",command=self.attendance,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_3.place(x=800,y=240,width=150,height=30)
        
        # Help butten
        img8=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\11_home.png")
        img8=img8.resize((150,150))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b4=Button(bgimage,image=self.photoimg8,cursor="hand2",command=self.help)
        b4.place(x=1100,y=100,width=150,height=150)

        b1_4=Button(bgimage,text="Help ",cursor="hand2",command=self.help,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_4.place(x=1100,y=240,width=150,height=30)
        
        # Train face butten
        img9=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\07_home.jpg")
        img9=img9.resize((150,150))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b5=Button(bgimage,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=160,y=400,width=150,height=150)

        b1_5=Button(bgimage,text="Train ",cursor="hand2",command=self.train_data,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_5.place(x=160,y=550,width=150,height=30)
        
        # Photo button
        img10=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\09_home.jpg")
        img10=img10.resize((150,150))
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b6=Button(bgimage,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=400,width=150,height=150)

        b1_6=Button(bgimage,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_6.place(x=500,y=550,width=150,height=30)
        
        # DEveloper butten
        img11=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\10_home.png")
        img11=img11.resize((150,150))
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b7=Button(bgimage,image=self.photoimg11,cursor="hand2",command=self.devl_oper)
        b7.place(x=800,y=400,width=150,height=150)

        b1_7=Button(bgimage,text="Developer ",cursor="hand2",command=self.devl_oper,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_7.place(x=800,y=550,width=150,height=30)
        
        
        # EXIT butten
        img12=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\08_home.jpg")
        img12=img12.resize((150,150))
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b8=Button(bgimage,image=self.photoimg12,cursor="hand2",command=self.Iexit)
        b8.place(x=1100,y=400,width=150,height=150)

        b1_8=Button(bgimage,text="Exit ",cursor="hand2",command=self.Iexit,font=("times new roman",18,"bold"),bg="black",fg="red")
        b1_8.place(x=1100,y=550,width=150,height=30)
        
        
        
    def open_img(self):
        os.startfile("data")
        
        
    def Iexit(self):
        self.Iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.Iexit>0:
            self.root.destroy()
        else:
            return 
    
        
        
        
        
    # =========================functioion button======================
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
       
    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=train(self.new_window)
       
    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition(self.new_window)
       
    def devl_oper(self):
        self.new_window=Toplevel(self.root)
        self.app=Devloper(self.new_window)
       
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    
       
    
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recogination_System(root)
    root.mainloop()
    
    
        