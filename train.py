from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2
import os


# LBPS




class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recoginition System")
        self.root.title("Tranning")
        self.root.iconbitmap(r"Images\logo.ico")
        
        
        title_ibl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=-3,y=0,width=1530,height=45)
        
        img_top=Image.open(r"Images\13_home.webp")
        img_top=img_top.resize((1530,425))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=425)
              
        
        
        img_bottom=Image.open(r"Images\14.jpg")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bott=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bott)
        f_lbl.place(x=0,y=480,width=1530,height=500)
        
        # Button       
        b1_5=Button(self.root,text="TRAIN DATA ",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="pink",fg="black")
        b1_5.place(x=0,y=480,width=1530,height=90)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # Gray scale image
            imageNP=np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNP)
            ids.append(id)
            
            cv2.imshow("Traning",imageNP)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        # ========================Train the classifier==========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed")
        
            
        





if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()
    
    