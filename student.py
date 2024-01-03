from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import datetime
from time import strftime




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recoginition System")
        # self.root=Tk()
        self.root.title("Student")
        self.root.iconbitmap(r'C:\Users\theve\OneDrive\Desktop\Project_1\Automated-Attendance-System\Images\logo.ico')
        
        # =======================VRIABLES===================
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        # self.var_radio2=StringVar()
        # --------------------------------------------------------------------------------------------------
        img1=Image.open("Images/13_home.webp")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=5,y=0,width=500,height=130)
        
        
        img2=Image.open(r"Images\01_home.png")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=500,height=130)
        
        
        img3=Image.open(r"Images\12_home.webp")
        img3=img3.resize((500,130))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1015,y=0,width=500,height=130)
        #-----------------------------------background image----------------------------------------------------------------
        img4=Image.open(r"Images\back_home.png")
        img4=img4.resize((1900,1070))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bgimage=Label(self.root,image=self.photoimg4)
        bgimage.place(x=5,y=130,width=1510,height=650)

        title_ibl=Label(bgimage,text="STUDENT MANAGAMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=-3,y=0,width=1530,height=45)
        # time
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_ibl,font=('times new roman',18,'bold'),background='white',foreground='green')
        lbl.place(x=1300,y=(-15),width=200,height=70)
        time()
        
        
        
        main_frame=Frame(bgimage,bd=2)
        main_frame.place(x=0,y=50,width=1505,height=590)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=700,height=540)
        
        
        img_left=Image.open(r"Images\15_home.webp")
        img_left=img_left.resize((700,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=680,height=130)
        
        # Current cource
        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=680,height=90)
        # Department
        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=2,pady=2,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo['values']=("Select Department","Computer","Diploma","Civil","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        # Course
        course_lable=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=2,pady=2,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo['values']=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=2,sticky=W)
        
        # Year
        
        Year_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_lable.grid(row=1,column=0,padx=2,pady=2,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        Year_combo['values']=("Select Year","2020","2021","2022","2023","2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        
        # Semester
        semester_lable=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_lable.grid(row=1,column=2,padx=2,pady=2,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)
        
        # Class information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=225,width=680,height=285)
        
        # Student ID
        studentId_lable=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentId_lable.grid(row=0,column=0,padx=10,pady=2,sticky=W)
        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=2,sticky=W)
        
        # Student Name
        studentName_lable=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_lable.grid(row=0,column=2,padx=10,pady=2,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=2,sticky=W)
        
        # Class Dividsion
        class_div_lable=Label(class_student_frame,text="Division",font=("times new roman",12,"bold"),bg="white")
        class_div_lable.grid(row=1,column=0,padx=10,pady=2,sticky=W)
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo['values']=("A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=2,sticky=W)
        
        
        # Roll Number
        roll_num_lable=Label(class_student_frame,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        roll_num_lable.grid(row=1,column=2,padx=10,pady=2,sticky=W)
        roll_num_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_num_entry.grid(row=1,column=3,padx=10,pady=2,sticky=W)
        
        # Gender
        gender_lable=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_lable.grid(row=2,column=0,padx=10,pady=2,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=2,sticky=W)
        
        # Date of Birth
        dob_lable=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_lable.grid(row=2,column=2,padx=10,pady=2,sticky=W)
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)
        
        
        # Email
        email_lable=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_lable.grid(row=3,column=0,padx=10,pady=2,sticky=W)
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)
        
        # Phone Number
        phone_lable=Label(class_student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        phone_lable.grid(row=3,column=2,padx=10,pady=2,sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)
        
        # Address
        address_lable=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_lable.grid(row=4,column=0,padx=10,pady=2,sticky=W)
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)
        
        # Teacher name
        teacher_lable=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_lable.grid(row=4,column=2,padx=10,pady=2,sticky=W)
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)
        
        
        
        # Radio buttons

        radiobtn1=Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        
        # button_frame
        btn_frame=Frame(class_student_frame,bd=1,relief=RAISED,bg="white")
        btn_frame.place(x=0,y=170,width=678,height=80)
        
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)
        
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="brown",fg="white")
        del_btn.grid(row=0,column=2,padx=5)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        reset_btn.grid(row=0,column=3)
        
        # Next Frame
        btn1_frame=Frame(class_student_frame,bd=1,relief=RAISED,bg="white")
        btn1_frame.place(x=0,y=220,width=678,height=80)
        
        
        take_photo_btn=Button(btn1_frame,text="Take photo sample",command=self.generate_dataset,width=35,font=("times new roman",12,"bold"),bg="red",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=5)
        
        update_photo_btn=Button(btn1_frame,text="Update photo sample",width=35,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=10)
        
        
        
        
        
        
        
        
        
        
        
        # ====================right frame==========================
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=700,height=540)
        
        
        
        
        img_right=Image.open(r"Images\14.jpg")
        img_right=img_right.resize((700,150))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=680,height=130)
        
        
        # ==========================Serch========================
        
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=130,width=680,height=70)
        
        
        search_lable=Label(search_frame,text="Search By.",font=("times new roman",15,"bold"),bg="white")
        search_lable.grid(row=0,column=0,padx=2,pady=2,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo['values']=("Select ","Roll No.","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)
        
        
        
        
        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="brown",fg="white")
        search_btn.grid(row=0,column=3)
        
        showAll_btn=Button(search_frame,text="ShowAll",width=15,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)
        
        
        # ===============Table frame======================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=205,width=680,height=300)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Gender","Department","Year","Semester","Course","Division","DOB","Email","Phone","Address","Teacher","Photos"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Roll_No",text="Roll")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photos",text="Photos")
        self.student_table["show"]="headings"
        
        self.student_table.column("ID",width=50)
        self.student_table.column("Roll_No",width=50)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=50)
        self.student_table.column("Department",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=50)
        self.student_table.column("Course",width=100)
        self.student_table.column("Division",width=50)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=200)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photos",width=50)
        self.student_table["show"]="headings"
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    # ================================Function Decleration======================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # ==============================fetch datta==============================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # =======================Get =====================================
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_std_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_gender.set(data[3]),
        self.var_dep.set(data[4]),
        self.var_year.set(data[5]),
        self.var_semester.set(data[6]),
        self.var_course.set(data[7]),
        self.var_div.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # Update data
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to this student setails",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update students set Roll_No=%s,Name=%s,Gender=%s,Department=%s,Year=%s,Semester=%s,Course=%s,Division=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                    
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_course.get(),
                    self.var_div.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    
                    
                        
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # ===============Deleat Function================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be reqired",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
                    my_cursor=conn.cursor()
                    sql="delete from students where ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ==============================Reset ==============================
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_gender.set("Male"),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select year"),
        self.var_semester.set("Select semester"),
        self.var_course.set("Select course"),
        self.var_div.set("Select division"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    # =======================Photo smples=========================
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from students")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id=1+id
                my_cursor.execute("update students set Roll_No=%s,Name=%s,Gender=%s,Department=%s,Year=%s,Semester=%s,Course=%s,Division=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                    
                self.var_roll.get(),
                self.var_name.get(),
                self.var_gender.get(),
                self.var_dep.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_course.get(),
                self.var_div.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_std_id.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ================Load predifiend=================
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minum nebhbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set Completed !!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                    
                
                
                
                    
       
        
        
  
        







if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
    
        