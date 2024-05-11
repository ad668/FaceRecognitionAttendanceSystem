from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_recognition
from attendance import Attendance


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="Help Desk", font=("times new roman", 30, "bold"),
                            bg="white", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=50)

        img_top = Image.open(r"Image\help.jpg")
        img_top = img_top.resize((1530, 650))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=51, width=1530, height=650)

        title_label = Label(f_lb1, text="Email: abc123@gmail.com", font=("times new roman", 30, "bold"),
                            bg="white", fg="blue")
        title_label.place(x=450, y=250)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()