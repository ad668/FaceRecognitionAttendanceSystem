from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_recognition
from attendance import Attendance


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"),
                            bg="white", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=50)

        img_top = Image.open(r"Image\Dev.jpg")
        img_top = img_top.resize((1530, 650))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=51, width=1530, height=650)

        main_frame = Frame(f_lb1, bd=2, bg="white")
        main_frame.place(x=850, y=0, width=500, height=560)

        img_top1 = Image.open(r"Image\DEVAD1.jpg")
        img_top1 = img_top1.resize((200, 200))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lb2 = Label(main_frame, image=self.photoimg_top1)
        f_lb2.place(x=300, y=0, width=200, height=200)


        #Developer Info

        Dev_info = Label(main_frame, text="Hello I am Aditya", font=("times new roman", 16, "bold"),
                            bg="white",fg="blue")
        Dev_info.place(x=30, y=55)

        Dev_info1 = Label(main_frame, text="I am Software Developer", font=("times new roman", 16, "bold"),
                         bg="white",fg="blue")
        Dev_info1.place(x=30, y=87)


        #Image
        img3 = Image.open(r"Image\imag1.jpg")
        img3 = img3.resize((495, 350))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lb2 = Label(main_frame, image=self.photoimg3)
        f_lb2.place(x=0, y=205, width=495, height=350)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()