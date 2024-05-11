import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"Image\College.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open(r"Image\img2.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=500, y=0, width=500, height=130)

        #third image
        img2 = Image.open(r"Image\college2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1000, y=0, width=500, height=130)

        # background image
        img3 = Image.open(r"Image\bg.jpg")
        img3 = img3.resize((1530, 560), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=560)


        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE", font=("times new roman",40,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1400,height=45)

        #Student button
        img4 = Image.open(r"Image\b1.jpg")
        img4 = img4.resize((180, 180), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=150,y=100,width=180,height=180)

        b2 = Button(bg_img, command=self.student_details,text="Student details", cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=150, y=240, width=180, height=40)

        # Detect face
        img5 = Image.open(r"Image\facedetct.jpeg")
        img5 = img5.resize((180, 180), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,command=self.face_data ,image=self.photoimg5, cursor="hand2")
        b1.place(x=440, y=100, width=180, height=180)
        b2 = Button(bg_img,command=self.face_data ,text="Face Detect", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=440, y=240, width=180, height=40)

        # Attendence face
        img6 = Image.open(r"Image\attendence.jpg")
        img6 = img6.resize((180, 180), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, command=self.attendance_data,image=self.photoimg6, cursor="hand2")
        b1.place(x=730, y=100, width=180, height=180)
        b2 = Button(bg_img, command=self.attendance_data,text="Attendence", cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=730, y=240, width=180, height=40)

        # Help desk
        img7 = Image.open(r"Image\help.png")
        img7 = img7.resize((180, 180), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img,command=self.help_info, image=self.photoimg7, cursor="hand2")
        b1.place(x=1020, y=100, width=180, height=180)
        b2 = Button(bg_img,command=self.help_info, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=1020, y=240, width=180, height=40)

        # Train face button
        img8 = Image.open(r"Image\trainface.jpg")
        img8 = img8.resize((180, 180), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=150, y=340, width=180, height=180)
        b2 = Button(bg_img, text="Train Data",command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=150, y=480, width=180, height=40)

        #Photos button
        img9 = Image.open(r"Image\photos.jpeg")
        img9 = img9.resize((180, 180), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=440, y=340, width=180, height=180)
        b2 = Button(bg_img,command=self.open_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=440, y=480, width=180, height=40)

        #Developer button
        img10 = Image.open(r"Image\Developer.jpg")
        img10 = img10.resize((180, 180), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img,command=self.developer_info, image=self.photoimg10, cursor="hand2")
        b1.place(x=730, y=340, width=180, height=180)
        b2 = Button(bg_img,command=self.developer_info, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=730, y=480, width=180, height=40)

        #Exit button
        img11 = Image.open(r"Image\exit.jpg")
        img11 = img11.resize((180, 180), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img,command=self.iExit, image=self.photoimg11, cursor="hand2")
        b1.place(x=1020, y=340, width=180, height=180)
        b2 = Button(bg_img,command=self.iExit ,text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="white")
        b2.place(x=1020, y=480, width=180, height=40)

    #FUNCTION BUTTON
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def open_img(self):
        os.startfile("Data")

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_info(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit from this window.",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()      