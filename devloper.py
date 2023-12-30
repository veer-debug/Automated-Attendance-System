from tkinter import *
# from tkinter import tk
import webbrowser
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Devloper:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("DEVLOPER")
        
        title_ibl=Label(self.root,text="#  😊 DEVELOPER 😊 #",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        img4=Image.open(r"C:\Users\theve\OneDrive\Desktop\Folders\SE\final_project\Images\devloperbg.jpg")
        img4=img4.resize((1900,1070))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bgimage=Label(self.root,image=self.photoimg4)
        bgimage.place(x=5,y=45,width=1520,height=735)
        
        # title_ib3=Label(bgimage,text="Welcome ! We're a team dedicated to transforming ideas into digital reality.",font=("times new roman",20,"bold"),bg="pink",fg="black")
        # title_ib3.place(x=0,y=0,width=1530,height=80)
        
        
        
        # =========================Ranveer=====================================
        img_left2=Image.open(r"Images\ranveer.jpeg")
        img_left2=img_left2.resize((250,250))
        self.photoimg_left2=ImageTk.PhotoImage(img_left2)
        
        f_lb2=Label(bgimage,image=self.photoimg_left2)
        f_lb2.place(x=620,y=20,width=250,height=250)   
        
        
        R6=Label(bgimage,text="Renveer Kumar, a dedicated Python developer, brings a wealth of expertise to the realm of full-stack development.",font=(" ",15,"bold"),bg="white",fg="black")
        R6.place(x=220,y=370)
        R7=Label(bgimage,text="His  commitment  to  crafting  efficient  and  elegant  solutions is evident in  his  meticulous  approach  to coding. With a keen eye  for detail  and a passion ",font=(" ",15,"bold"),bg="white",fg="black")
        R7.place(x=20,y=402)
        R8=Label(bgimage,text="for  clean  code, Renveer transforms complex challenges into  streamlined  applications. Constantly   evolving alongside   Python's dynamic  ecosystem, he ",font=(" ",15,"bold"),bg="white",fg="black")
        R8.place(x=20,y=434)
        R8=Label(bgimage,text="remains at the  forefront  of innovation.  Renveer thrives in  collaborative environments, leveraging  his communication  skills to contribute to team success.",font=(" ",15,"bold"),bg="white",fg="black")
        R8.place(x=20,y=466)
        R8=Label(bgimage,text="Committed to continuous learning,he is dedicated to delivering cutting-edge solutions that exceed expectations and push the boundaries of what's possible.",font=(" ",15,"bold"),bg="white",fg="black")
        R8.place(x=20,y=498)


    # def open_instagram():
    #     # Replace 'https://www.instagram.com/your_username/' with the actual Instagram profile URL
    #     instagram_url = 'https://www.instagram.com/__ranveer0__/'
    #     webbrowser.open_new(instagram_url)

    # # Create the main window
    # root = Tk()
    # root.title("Instagram Link")

    # # Load Instagram logo image
    # instagram_logo_path = "path/to/instagram_logo.png"  # Replace with the path to your Instagram logo image
    # instagram_logo = PhotoImage(file=instagram_logo_path)

    # # Create a label to display the Instagram logo
    # logo_label = Label(root, image=instagram_logo)
    # logo_label.pack()

    # # Create a hyperlink label
    # link_label = Label(root, text="Follow me on Instagram!", font=("Helvetica", 12), fg="blue", cursor="hand2")
    # link_label.pack(pady=10)

    # # Bind the label to the function that opens the Instagram link
    # link_label.bind("<Button-1>", lambda e:open_instagram)

# Run the Tkinter event loop

        




if __name__=="__main__":
    root=Tk()
    obj=Devloper(root)
    root.mainloop()
    root.mainloop()
    