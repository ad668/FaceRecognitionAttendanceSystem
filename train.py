from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="TRAIN DATASET", font=("times new roman", 30, "bold"),
                            bg="white", fg="red")
        title_label.place(x=0, y=0, width=1530, height=50)

        img_top = Image.open(r"Image\train_face1.jpg")
        img_top = img_top.resize((1530, 225))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=51, width=1530, height=225)

        b2 = Button(self.root, text="TRAIN DATA",command=self.train_classifiers, cursor="hand2", font=("times new roman", 25, "bold"), bg="red",
                    fg="white")
        b2.place(x=0, y=275, width=1530, height=50)

        img_bottom = Image.open(r"Image\people.jpg")
        img_bottom = img_bottom.resize((1530, 370))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=320, width=1530, height=370)

    def train_classifiers(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 10

        ids = np.array(ids)

        # train classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()