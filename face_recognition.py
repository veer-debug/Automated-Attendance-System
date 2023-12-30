from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from time import strftime
import numpy as np
import cv2
import os


# LBPS




class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recoginition System")
        
        title_ibl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_ibl.place(x=-3,y=0,width=1530,height=45)
        
        
        
        # =====================================
        
        img_top=Image.open(r"Images\16_home.jpg")
        img_top=img_top.resize((1000,732))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=525,y=50,width=1000,height=732)
        # ========
            
        img_top1=Image.open(r"Images\17_home.webp")
        img_top1=img_top1.resize((790,732))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl1=Label(self.root,image=self.photoimg_top1)
        f_lbl1.place(x=5,y=50,width=620,height=732)
        
        b1_5=Button(self.root,text="FACE  DECTOR ",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="green")
        b1_5.place(x=960,y=650,width=500,height=80)
        
        b1_5=Button(self.root,text="FACE  DECTOR ",command=self.face_recog,cursor="hand2",font=("times new roman",23,"bold"),bg="red",fg="black")
        b1_5.place(x=179,y=585,height=50)
        
        
        # img_top2=Image.open(r"Images\17_home.png")
        # img_top2=img_top2.resize((790,732))
        # self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        
        # f_lbl2=Label(self.root,image=self.photoimg_top2)
        # f_lbl2.place(x=50,y=50,width=630,height=732)
        
#    ===================================Attendance=========================
    def mark_attendance(self,i,r,n,d):
        now=datetime.now()
        d1=now.strftime("%d/%m/%Y")
    
# Replace these with your own database credentials
        host = "localhost"
        user = "root"
        password = "9954"
        database = "student"
        

# Your variable for the table name
        # s=StringVar(r)
        table_name ='R_'+str(r)

# Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    # Create a cursor object to interact with the database
        cursor = conn.cursor()

    # Define the table creation SQL query with a dynamic table name
        table_creation_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Roll VARCHAR(45),
            Name VARCHAR(45),
            Department VARCHAR(45),
            Date VARCHAR(45)
        );
        """
        
        
# Execute the table creation query
        cursor.execute(table_creation_query)
        
        data=f"select Date from {table_name}"
        cursor.execute(data);
        date1=cursor.fetchone()
        date2=np.array(date1)
        
        if d1 not in date2:
            insert_query = f"INSERT INTO {table_name} ( Roll, Name, Department, Date) VALUES ( %s, %s, %s, %s)"

            cursor.execute(insert_query, ( r, n, d, d1))

        conn.commit()
        cursor.close()
        conn.close()

        
        
        
        
        
    # =======================fACE RECOGNISATION=======================
    
    def face_recog(self):
        def drw_boundry(img,classifier,scaleFactor,minNeighur,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighur)
            
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="9954",database=" Face_recog")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from students where ID="+str(id))
                n=my_cursor.fetchone()
                # i=str(i)
                n= "+".join(n)
                
                my_cursor.execute("select Roll_No from students where ID="+str(id))
                r=my_cursor.fetchone()
                # r=str(r)

                r= "+".join(r)
                
                my_cursor.execute("select Department from students where ID="+str(id))
                d=my_cursor.fetchone()
                # d=str(d)

                d= "+".join(d)
                
                my_cursor.execute("select ID from students where ID="+str(id))
                i=my_cursor.fetchone()
                # d=str(d)

                # i= "+".join(i)
                i= id
                # si=si+1
                
                
                
                
                if confidence >60:
                    cv2.putText(img,f"Roll   :{r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f"Name :{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Dep   :{d}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"ID     :{i}",(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord.append((x, y, w, h))
            return coord
        def recognize(img,clf,faceCascade):
            coord=drw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcom",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
            
            
 
 
 
 
 
 
 
 
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
    
    