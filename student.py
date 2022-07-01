from ast import Try
from logging import root
from msilib.schema import SelfReg
from multiprocessing import connection
from sre_parse import State
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




    



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        
        # ================== variables ============= #
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        
         #firstImage

        img = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\facialrecognition.png")
        img = img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
         
         #SecondImage
        img1 = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\stdLogin.png")
        img1 = img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500,y=1,width=500,height=130)

         #thirdImage
        img2 = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\attendance1.png")
        img2 = img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

         #bg image
        img3 = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\BestFacialRecognition.jpg")
        img3 = img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=140,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Calibri",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=15,y=55,width=1500,height=600)
         
        # left label frame 
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("calibri",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #Current course Information

        current_course_frame =LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("calibri",12,"bold"))
        current_course_frame.place(x=17,y=135,width=720,height=150)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman ",12,"bold"))
        dep_combo["values"]=("Select Department","CSE","IT","EC","EX","ME","CIV",) 
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1 ,padx=2,pady=10)
         
        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman ",12,"bold"))
        course_combo["values"]=("Select Course","B.E","B.TECH","M.TECH","MCA","BCA","PH") 
        course_combo.current(0)
        course_combo.grid(row=0,column=3 ,padx=2,pady=10)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman ",12,"bold"))
        year_combo["values"]=("Select Year","1","2","3","4") 
        year_combo.current(0)
        year_combo.grid(row=1,column=1 ,padx=2,pady=10,sticky=W)

        # Semester

        year_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman ",12,"bold"))
        year_combo["values"]=("Select Sem","1","2","3","4","5","6","7","8") 
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student information

        class_Student_frame =LabelFrame(main_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("calibri",12,"bold"))
        class_Student_frame.place(x=17,y=250,width=720,height=300)
        
        #student ID
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        # Student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class Division

        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       #class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold")
       #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman ",12,"bold"),state="readonly",width=16)
        div_combo["values"]=("A","B","C") 
        div_combo.current(0)
        div_combo.grid(row=1,column=1 ,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_Student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
         
        Gender_no_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #Gender_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        #Gender_no_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman ",12,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Male","Female","Other") 
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1 ,padx=10,pady=5,sticky=W)

        
       #DOB

        dob_no_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_no_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_no_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

      # EMAIL:

        em_no_label=Label(class_Student_frame,text="E-Mail:",font=("times new roman",12,"bold"),bg="white")
        em_no_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        em_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        em_no_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

      # Phone No

        ph_no_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        ph_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        ph_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        ph_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


      # Address

        AD_no_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        AD_no_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        AD_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        AD_no_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
      # HOD NAME 
        hod_no_label=Label(class_Student_frame,text="HOD Name:",font=("times new roman",12,"bold"),bg="white")
        hod_no_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        hod_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        hod_no_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


     # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text = "Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=2)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text= "No Photo Sample", value = "No")
        radiobtn2.grid(row=6,column=1)

     # buttons frame

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame, text="Save",command=self.add_data,width=17, font=("times new roman",13,"bold"),bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text="Update",width=17,command =self.update_data,font=("times new roman",13,"bold"),bg="blue", fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame, text="Delete",width=17,command=self.delete_data, font=("times new roman",13,"bold"),bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("times new roman",13,"bold"),bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)
  
        #2nd Button Frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample",width=35, font=("times new roman",13,"bold"),bg="blue", fg="white")
        take_photo_btn.grid(row=1,column=0)
        
        update_photo_btn=Button(btn_frame1, text="Update Photo Sample",width=35, font=("times new roman",13,"bold"),bg="blue", fg="white")
        update_photo_btn.grid(row=1,column=1)
        
     # RIGHT LABEL FRAME SECTION STARTS HERE ..........................................................   

        # Right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("calibri",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)


        img_right = Image.open(r"C:\Users\asus\OneDrive\Desktop\FRS\college_images\student.jpg")
        img_right = img_right.resize((720,130), Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # ================ Search System =========== #

        Search_frame =LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("calibri",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

       
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_frame,font=("times new roman ",12,"bold"),width=15)
        search_combo["values"]=("Select Year","1","2","3","4") 
        search_combo.current(0)
        search_combo.grid(row=0,column=1 ,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame, text="Search",width=12, font=("times new roman",12,"bold"),bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame, text="Show All",width=12, font=("times new roman",12,"bold"),bg="blue", fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        #=============table frame ========================#
        table_frame =Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")

        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Hod Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
       


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)

        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=115)
     
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ============= function declaration ========== #
    def add_data(self):
        if self.var_dep.get()=="Select department" or  self.var_name.get()=="" or self.var_id.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                              self.var_dep.get(),
                                                                                              self.var_course.get(),
                                                                                              self.var_year.get(),
                                                                                              self.var_sem.get(),
                                                                                              self.var_id.get(),
                                                                                              self.var_name.get(),
                                                                                              self.var_div.get(),
                                                                                              self.var_roll.get(),
                                                                                              self.var_gender.get(),
                                                                                              self.var_dob.get(),
                                                                                              self.var_email.get(),
                                                                                              self.var_phone.get(),
                                                                                              self.var_address.get(),
                                                                                              self.var_teacher.get(),
                                                                                              self.var_radio1.get()

                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close
                messagebox.showinfo("Success", "Student details has been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

   # ===================== fetch data ======================#
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
             conn.close()

        
   # ================== get cursor =======================#
    def get_cursor(self,event=" "):
         cursor_focus=self.student_table.focus()
         content = self.student_table.item(cursor_focus)
         data=content["values"]

         self.var_dep.set(data[0]),
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_sem.set(data[3]),
         self.var_id.set(data[4]),
         self.var_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_roll.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_dob.set(data[9]),
         self.var_email.set(data[10]),
         self.var_phone.set(data[11]),
         self.var_address.set(data[12]),
         self.var_teacher.set(data[13]),
         self.var_radio1.set(data[14])

    
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select department" or  self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                Upadate=messagebox.askquestion("Update","Do you want to update student details",parent=self.root)
               # conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
                if len(Upadate)>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                
                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_sem.get(),
                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                 self.var_div.get(),
                                                                                                                                                                 self.var_roll.get(),
                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                 self.var_teacher.get(),
                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                 self.var_id.get()
                               )) 
                else:
                     if not Upadate:
                         return 
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()         
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required ",parent=self.root)  
        else:
             try:
                 delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student ", parent=self.root)
                 if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                 else:
                     if not delete:
                        return   
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
             except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set(" ")
        self.var_address.set(" ")
        self.var_teacher.set(" ")
        self.var_radio1.set("")
        
    def            generate_dataset(self):
        if self.var_dep.get()=="Select department" or  self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Redhat1$",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_id.get()==id+1   
                                                                                                                                                                                )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ====== Load predefined data on face frontals from opencv ==== #

                face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compiled!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
 
           


















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()