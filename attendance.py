from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import datetime
from time import strftime
import numpy as np



mydata=[]




class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1180+0+0")
        self.root.title("Face Recoginition System")
        self.root.title("Students")
        self.root.iconbitmap(r"Images\logo.ico")
        
        # --------------------------------------------------------------------------------------------------
        img1=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\13_home.webp")
        img1=img1.resize((500,140))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=5,y=0,width=500,height=140)
        
        
        # ====================variables========================
        self.var_name=StringVar()
        self.var_gen=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_cou=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_tec=StringVar()
        self.var_tot=StringVar()
        self.var_roll=StringVar()
        
        
        
        
        
        img2=Image.open(r"Images\01_home.png")
        img2=img2.resize((500,140))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=500,height=140)
        
        
        img3=Image.open(r"Images\12_home.webp")
        img3=img3.resize((500,140))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1015,y=0,width=500,height=140)
        #-----------------------------------background image----------------------------------------------------------------
        img4=Image.open(r"Images\back_home.png")
        img4=img4.resize((1900,1070))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bgimage=Label(self.root,image=self.photoimg4)
        bgimage.place(x=5,y=140,width=1510,height=650)

        title_ibl=Label(bgimage,text="STUDENT REPORT",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=-3,y=0,width=1540,height=45)
        # time
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_ibl,font=('times new roman',18,'bold'),background='white',foreground='green')
        lbl.place(x=1300,y=-15,width=180,height=70)
        time()
        
        
        
        main_frame=Frame(bgimage,bd=2,bg="red")
        main_frame.place(x=0,y=45,width=1505,height=620)
        botom=Frame(bgimage,bd=2)
        botom.place(x=8,y=115,width=1490,height=420)
        
        botom1=Frame(bgimage,bd=2)
        botom1.place(x=8,y=550,width=1490,height=70)
        
        botom2=Frame(bgimage,bd=2)
        botom2.place(x=0,y=630,width=1550,height=70)
        
        
        #-----------------------------------------searching data---------------------------------------------------------------
        top=Frame(bgimage,bd=2,bg="pink")
        top.place(x=0,y=55,width=1505,height=50)
        
        studentName_lable=Label(top,text="Student Roll_Number",font=("times new roman",18,"bold"),bg="white")
        studentName_lable.grid(row=0,column=0,padx=80,pady=2,sticky=W)
        studentName_entry=ttk.Entry(top,textvariable=self.var_roll,width=50,font=("times new roman",20,"bold"))
        studentName_entry.grid(row=0,column=1,padx=20,pady=5,sticky=W)
        
        
        save_btn=Button(top,text="Search",command=self.search_student,width=17,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=2,padx=100)
        
        
        #======================== lables for results======================
        # ===================Name=================
        studentName_roll=Label(botom,text="Name",font=("times new roman",18,"bold"),bg="white")
        studentName_roll.grid(row=0,column=0,padx=80,pady=60,sticky=W)
        studentroll_entry=ttk.Entry(botom,textvariable=self.var_name,width=15,font=("times new roman",20,"bold"))
        studentroll_entry.grid(row=0,column=1,padx=15,pady=20,sticky=W)
        
        # ======================DOB===============================
        studentName_age=Label(botom,text="DOB",font=("times new roman",18,"bold"),bg="white")
        studentName_age.grid(row=0,column=2,padx=60,pady=20,sticky=W)
        studentage_entry=ttk.Entry(botom,textvariable=self.var_dob,width=15,font=("times new roman",20,"bold"))
        studentage_entry.grid(row=0,column=3,padx=15,pady=20,sticky=W)
        
        # ========================Department=============================
        studentName_Dep=Label(botom,text="Department",font=("times new roman",18,"bold"),bg="white")
        studentName_Dep.grid(row=0,column=4,padx=60,pady=20,sticky=W)
        studentDep_entry=ttk.Entry(botom,textvariable=self.var_dep,width=15,font=("times new roman",20,"bold"))
        studentDep_entry.grid(row=0,column=5,padx=15,pady=20,sticky=W)
        
        # =================Semester===============================================
        studentName_sem=Label(botom,text="Semester",font=("times new roman",18,"bold"),bg="white")
        studentName_sem.grid(row=1,column=0,padx=80,pady=20,sticky=W)
        studentsem_entry=ttk.Entry(botom,textvariable=self.var_sem,width=15,font=("times new roman",20,"bold"))
        studentsem_entry.grid(row=1,column=1,padx=15,pady=20,sticky=W)
        
        # ===============Year================================
        studentName_Year=Label(botom,text="Year",font=("times new roman",18,"bold"),bg="white")
        studentName_Year.grid(row=1,column=2,padx=60,pady=20,sticky=W)
        studentYear_entry=ttk.Entry(botom,textvariable=self.var_year,width=15,font=("times new roman",20,"bold"))
        studentYear_entry.grid(row=1,column=3,padx=15,pady=20,sticky=W)
        
        # =====================Cource===============================
        studentName_Cou=Label(botom,text="Cource",font=("times new roman",18,"bold"),bg="white")
        studentName_Cou.grid(row=1,column=4,padx=60,pady=20,sticky=W)
        studentCou_entry=ttk.Entry(botom,textvariable=self.var_cou,width=15,font=("times new roman",20,"bold"))
        studentCou_entry.grid(row=1,column=5,padx=15,pady=20,sticky=W)
        
        
        # ===============Gender=======================
        studentName_gen=Label(botom,text="Gender",font=("times new roman",18,"bold"),bg="white")
        studentName_gen.grid(row=2,column=0,padx=80,pady=20,sticky=W)
        studentgen_entry=ttk.Entry(botom,textvariable=self.var_gen,width=15,font=("times new roman",20,"bold"))
        studentgen_entry.grid(row=2,column=1,padx=15,pady=60,sticky=W)
        
        # ===============Phone Number=====================
        studentName_ph=Label(botom,text="Phone No.",font=("times new roman",18,"bold"),bg="white")
        studentName_ph.grid(row=2,column=2,padx=60,pady=20,sticky=W)
        studentph_entry=ttk.Entry(botom,textvariable=self.var_phone,width=15,font=("times new roman",20,"bold"))
        studentph_entry.grid(row=2,column=3,padx=15,pady=20,sticky=W)
        
        # =============Teachers========================
        
        studentName_th=Label(botom,text="Teacher",font=("times new roman",18,"bold"),bg="white")
        studentName_th.grid(row=2,column=4,padx=60,pady=20,sticky=W)
        studentth_entry=ttk.Entry(botom,textvariable=self.var_tec,width=15,font=("times new roman",20,"bold"))
        studentth_entry.grid(row=2,column=5,padx=15,pady=20,sticky=W)
        
        
        
        # ========================================Totel attandance==============================
        
        studentName_to=Label(botom1,text="Totel Attandance",font=("times new roman",23,"bold"),bg="white")
        studentName_to.grid(row=0,column=0,padx=100,pady=15,sticky=W)
        studentto_entry=ttk.Entry(botom1,textvariable=self.var_tot,width=25,font=("times new roman",25,"bold"))
        studentto_entry.grid(row=0,column=1,padx=0,pady=0,sticky=W)
        
        
        
        
        
        
        # ==========FUNCTIONS============================FUNCTIONS=====================================Functions=======================FUNCTIONS===


    def search_student(self):
        roll_number = self.var_roll.get()  
        if roll_number: 
            
            self.datas(roll_number)
            self.totel(roll_number)
        else:
            messagebox.showerror("Error", "Please enter Roll Number")

    
    def totel(self,rn):
        conn = mysql.connector.connect(
            host="localhost",
            user='root',
            password='9954',
            database='student'
        )
        k='R_'+str(rn)

        cursor = conn.cursor()

        data = f"select count(ID) from {k}"
        cursor.execute(data)
        data = cursor.fetchone()  
        if data:
            self.var_tot.set(data)
        
        
        cursor.close()
        conn.close() 
        
    def datas(self,rn):
        conn = mysql.connector.connect(
            host="localhost",
            user='root',
            password='9954',
            database='face_recog'
        )
        # k='R'+str(rn)

        cursor = conn.cursor()

        data = f"select * from students where Roll_No='{rn}'"
        cursor.execute(data)
        data = cursor.fetchone()  
        if data:
            # print("Data retrieved from the database:", data)
            self.var_name.set(data[2])  
            self.var_gen.set(data[3])  
            self.var_dep.set(data[4])
            self.var_year.set(data[5])  
            self.var_sem.set(data[6])  
            self.var_cou.set(data[7])  
            self.var_dob.set(data[9])  
            self.var_phone.set(data[11]) 
            self.var_tec.set(data[13])  
            
            
            
        else:
            # print("Student not found")
            messagebox.showerror("Error", "Student not found")

        cursor.close()
        conn.close()          
            

        

        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
    