from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x690+0+0")
        self.root.title("Attendance Details")

        #Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        # first image
        img = Image.open(r"Image\sm1.jpeg")
        img = img.resize((750, 180))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=750, height=180)

        # second image
        img1 = Image.open(r"Image\sm2.jpg")
        img1 = img1.resize((750, 180))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=750, y=0, width=750, height=180)

        title_label = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"),
                            bg="white", fg="darkgreen")
        title_label.place(x=0, y=180, width=1530, height=50)

        #main Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=240, width=1340, height=450)

        #left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Student Attendance Details ",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=0, width=650, height=440)

        #LEft image
        img_left = Image.open(r"Image\student_details.png")
        img_left = img_left.resize((640, 100))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lb1 = Label(Left_frame, image=self.photoimg_left)
        f_lb1.place(x=3, y=0, width=640, height=100)

        left_inside_frame = Frame(Left_frame,relief=RIDGE ,bd=2, bg="white")
        left_inside_frame.place(x=5, y=110, width=635, height=260)

        #Labels and Entries
        #attendance ID
        attendanceID_label = Label(left_inside_frame, text='StudentID:', bg="white", font=("times new roman", 11, "bold"))
        attendanceID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        attendanceID_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,
                                    font=("times new roman", 13, "bold"))
        attendanceID_Entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Name
        Name_label = Label(left_inside_frame, text='Name:', bg="white",
                                   font=("times new roman", 11, "bold"))
        Name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        Name_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,
                                       font=("times new roman", 13, "bold"))
        Name_Entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #Date
        date_label = Label(left_inside_frame, text='Date:', bg="white",
                                   font=("times new roman", 11, "bold"))
        date_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        date_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                                       font=("times new roman", 13, "bold"))
        date_Entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Department
        Department_label = Label(left_inside_frame, text='Department:', bg="white",
                                   font=("times new roman", 11, "bold"))
        Department_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        Department_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,
                                       font=("times new roman", 13, "bold"))
        Department_Entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #Time
        time_label = Label(left_inside_frame, text='Time:', bg="white",
                                   font=("times new roman", 11, "bold"))
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        time_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,
                                       font=("times new roman", 13, "bold"))
        time_Entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #attendance
        attendance_label = Label(left_inside_frame, text='Attendance:', bg="white", font=("times new roman", 12, "bold"))
        attendance_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        attendance_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,  font=("times new roman", 12, "bold"),
                                    width=20, state="readonly")
        attendance_combo['values'] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)


        #Roll Number
        roll_label = Label(left_inside_frame, text='Roll Number:', bg="white",
                           font=("times new roman", 11, "bold"))
        roll_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        roll_Entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,
                               font=("times new roman", 13, "bold"))
        roll_Entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=4, y=210, width=620, height=35)

        import_btn = Button(btn_frame, text="Import csv", command=self.imoportcsv, width=15, height=1, cursor="hand2",
                          font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)
        export_btn = Button(btn_frame, command=self.exportcsv,text="Export csv", width=15, height=1, cursor="hand2",
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)
        update_btn = Button(btn_frame,text="Update", width=15, height=1, cursor="hand2",
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, command=self.reset_data,text="Reset", width=15, height=1, cursor="hand2",
                           font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Student Attendance Details ",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=0, width=650, height=440)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=635, height=405)

        #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch data
    def facedata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #Import CSV
    def imoportcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.facedata(mydata)

    #Export CSV
    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error","No Data is found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is exported "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # Update
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[2])
        self.var_atten_roll.set(rows[1])
        self.var_atten_dep.set(rows[3])
        self.var_atten_date.set(rows[5])
        self.var_atten_time.set(rows[4])
        self.var_atten_attendance.set(rows[6])

    #reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")





if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
