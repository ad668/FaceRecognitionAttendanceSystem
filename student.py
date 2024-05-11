from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        #Variable
        self.var_Dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()

        #first image
        img=Image.open(r"D:\Face Recognition Project\Image\sm1.jpeg")
        img=img.resize((500,100))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=100)

        #second image
        img1 = Image.open(r"D:\Face Recognition Project\Image\sm2.jpg")
        img1 = img1.resize((500, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=500, y=0, width=500, height=100)

        #third image
        img2 = Image.open(r"D:\Face Recognition Project\Image\sm3.jpeg")
        img2 = img2.resize((500, 100))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1000, y=0, width=500, height=100)

        # background image
        img3 = Image.open(r"D:\Face Recognition Project\Image\bg.jpg")
        img3 = img3.resize((1530, 590))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1530, height=590)

        title_label = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"),
                            bg="white", fg="darkgreen")
        title_label.place(x=0, y=0, width=1530, height=50)


        #mainframe
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1345,height=560)

        #Left level frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Details ",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=650,height=525)

        img_left = Image.open(r"D:\Face Recognition Project\Image\student_details.png")
        img_left = img_left.resize((640, 100))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lb1 = Label(Left_frame, image=self.photoimg_left)
        f_lb1.place(x=3, y=0, width=640, height=100)

        #current Course
        Current_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text=" Current Course Information ",
                                font=("times new roman", 12, "bold"))
        Current_frame.place(x=4, y=105, width=630, height=110)

        dep_label=Label(Current_frame,text='Department',bg="white",font=("times new roman", 12, "bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combo=ttk.Combobox(Current_frame,textvariable=self.var_Dep,font=("times new roman", 12, "bold"),width=17,state="readonly")
        dep_combo['values']=("Select Department","Computer","IT","BAF","BMS","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label = Label(Current_frame, text='Course', bg="white", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, pady=10,sticky=W)

        course_combo = ttk.Combobox(Current_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo['values'] = ("Select Course", "BSC", "BE", "B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        # Year
        year_label = Label(Current_frame, text='Year', bg="white", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(Current_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo['values'] = ("Select Year", "2020-21", "2021-22", "2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(Current_frame, text='Semester', bg="white", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        semester_combo = ttk.Combobox(Current_frame,textvariable=self.var_sem, font=("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo['values'] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3","Sem-4","Sem-5","Sem-6")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # Class Student Information
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text=" Class Student Information ",
                                   font=("times new roman", 12, "bold"))
        student_frame.place(x=4, y=215, width=640, height=285)

        #Student ID
        studentID_label = Label(student_frame, text='StudentID:', bg="white", font=("times new roman", 11, "bold"))
        studentID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        studentID_Entry=ttk.Entry(student_frame,textvariable=self.var_id,width=18,font=("times new roman", 13, "bold"))
        studentID_Entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # Student Name
        studentName_label = Label(student_frame, text='Student Name:', bg="white", font=("times new roman", 11, "bold"))
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        studentName_Entry = ttk.Entry(student_frame,textvariable=self.var_name, width=18, font=("times new roman", 13, "bold"))
        studentName_Entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(student_frame, text='Class Division:', bg="white", font=("times new roman", 11, "bold"))
        class_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(student_frame, textvariable=self.var_div, font=("times new roman", 11, "bold"),
                                    width=18, state="readonly")
        class_div_combo['values'] = ("Select Division", "A", "B", "C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(student_frame, text='Roll No:', bg="white", font=("times new roman", 11, "bold"))
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        roll_no_Entry = ttk.Entry(student_frame,textvariable=self.var_roll ,width=18, font=("times new roman", 13, "bold"))
        roll_no_Entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_label = Label(student_frame, text='Gender:', bg="white", font=("times new roman", 11, "bold"))
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_frame,textvariable=self.var_gender ,font=("times new roman", 11, "bold"), width=18, state="readonly")
        gender_combo['values'] = ("Select Gender", "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # DOB
        dob_label = Label(student_frame, text='DOB:', bg="white", font=("times new roman", 11, "bold"))
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        dob_Entry = ttk.Entry(student_frame,textvariable=self.var_DOB ,width=18, font=("times new roman", 13, "bold"))
        dob_Entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(student_frame, text='Email:', bg="white", font=("times new roman", 11, "bold"))
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        email_Entry = ttk.Entry(student_frame,textvariable=self.var_email ,width=18, font=("times new roman", 13, "bold"))
        email_Entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone
        phone_label = Label(student_frame, text='Mobile No:', bg="white", font=("times new roman", 11, "bold"))
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        phone_Entry = ttk.Entry(student_frame,textvariable=self.var_phone ,width=18, font=("times new roman", 13, "bold"))
        phone_Entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        address_label = Label(student_frame, text='Address:', bg="white", font=("times new roman", 11, "bold"))
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        address_Entry = ttk.Entry(student_frame,textvariable=self.var_address,width=18, font=("times new roman", 13, "bold"))
        address_Entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name
        teacher_name_label = Label(student_frame, text='Teacher Name:', bg="white", font=("times new roman", 11, "bold"))
        teacher_name_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        teacher_name_Entry = ttk.Entry(student_frame,textvariable=self.var_teacher ,width=18, font=("times new roman", 13, "bold"))
        teacher_name_Entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # Radio button

        radiobtn1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5, pady=10, sticky=W)


        radiobtn2 = ttk.Radiobutton(student_frame,variable=self.var_radio1 ,text="No photo sample", value="No")
        radiobtn2.grid(row=5, column=1, padx=5, pady=10, sticky=W)

        #button Frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=210,width=630,height=50)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=6,height=2,cursor="hand2",font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=6,height=2,cursor="hand2", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=6,height=2,cursor="hand2", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, text="Reset",command=self.Reset_data,width=6, height=2,cursor="hand2",font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        take_photo_sample_btn = Button(btn_frame,command=self.generate_dataset ,text="Take a Photo Sample", width=17, height=2,cursor="hand2",font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        take_photo_sample_btn.grid(row=0, column=4)
        update_photo_sample_btn = Button(btn_frame, text="Update Photo Sample", width=16,height=2,cursor="hand2",
                                       font=("times new roman", 13, "bold"), bg="blue",
                                       fg="white")
        update_photo_sample_btn.grid(row=0, column=5)

        # Right level frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text=" Student Details ",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=0, width=650, height=525)

        #image
        img_right = Image.open(r"D:\Face Recognition Project\Image\right_img.jpg")
        img_right = img_right.resize((640, 100))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lb1 = Label(Right_frame, image=self.photoimg_right)
        f_lb1.place(x=3, y=0, width=640, height=100)

        #--------Search System----------
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text=" Search System ",
                                   font=("times new roman", 12, "bold"))
        search_frame.place(x=4, y=100, width=640, height=70)

        search_label = Label(search_frame, text='Search By:', bg="red",fg="white",
                                   font=("times new roman", 11, "bold"))
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=10, state="readonly")
        search_combo['values'] = ("Select","Roll_No","Phone_no" )
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_Entry = ttk.Entry(search_frame, width=18, font=("times new roman", 13, "bold"))
        search_Entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=11,cursor="hand2",
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=4)
        showAll_btn = Button(search_frame, text="Show All", width=11, cursor="hand2",
                           font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4,padx=4)


        #----------------table Frame-------------------
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=4, y=175, width=640, height=310)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","course","year","sem","id","name","div","roll","gender","DOB","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function

    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition_system")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_Dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been addeed successful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #   fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition_system")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #-----------------getCursur

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # Update
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if upadate > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="face_recognition_system")
                    my_cursur = conn.cursor()
                    my_cursur.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s",(
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #------delete------
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete Page","Do you want to delete this student",parent=self.root)
                if delete >0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="",
                                                   database="face_recognition_system")
                    my_cursur = conn.cursor()
                    sqlquery="delete from student where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursur.execute(sqlquery,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student data",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset
    def Reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_DOB.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #------Take a photot sample
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="face_recognition_system")
                my_cursur = conn.cursor()
                my_cursur.execute("select * from student")
                myresult=my_cursur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursur.execute(
                    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_ID=%s",
                    (
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.Reset_data()
                conn.close()

                #----Load predefined data from frontal from opencv
                face_classifier=cv2.CascadeClassifier("D:\Face Recognition Project\haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3,  minimum naighbour=5
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
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed.........",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()