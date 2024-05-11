from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"),
                            bg="white", fg="green")
        title_label.place(x=0, y=0, width=1530, height=50)

        img_top = Image.open(r"Image\face2.png")
        img_top = img_top.resize((765, 600))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=51, width=765, height=600)

        img_bottom = Image.open(r"Image\face.jpeg")
        img_bottom = img_bottom.resize((765, 600))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=650, y=51, width=765, height=600)

        b2 = Button(f_lb2,command=self.Face_Recognition, text="Face Recognition", cursor="hand2",font=("times new roman", 18, "bold"), bg="darkgreen",fg="white")
        b2.place(x=290, y=530, width=180, height=30)


# Mark Attendance------------------
    def Mark_attendence(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1}, Present")

        #Face Recognition--------

    def Face_Recognition(self):
        def draw_boundry(img,classifier,scaleFactor,minimumNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minimumNeighbour)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="",
                                               database="face_recognition_system")
                my_cursur = conn.cursor()
                my_cursur.execute("select Name from student where Student_ID="+str(id))
                n =my_cursur.fetchone()
                n ="+".join(n)

                my_cursur.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursur.fetchone()
                r = "+".join(r)

                my_cursur.execute("select Dep from student where Student_ID=" + str(id))
                d = my_cursur.fetchone()
                d = "+".join(d)

                my_cursur.execute("select Student_ID from student where Student_ID=" + str(id))
                i = my_cursur.fetchone()
                i = "+".join(i)


                if confidence>75:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"StudentID:{i}", (x, y - 3), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.Mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,y ]
            return coord
        def recognize(img,clf,faceCascade):
            coord =draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap=cv2.VideoCapture(0)
        while True:
            ret, img=videocap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        videocap.release()
        cv2.destroyAllWindows()






if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
