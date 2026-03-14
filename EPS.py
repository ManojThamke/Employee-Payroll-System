from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import tkinter as tk 
from tkinter import messagebox,ttk
from tkinter import font
import sqlite3
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "esc2.db")
import time
import os
import tempfile 
class EmployeeSystem():
    def __init__(self,root): 
        self.root=root
        self.root.title("Employee Payroll System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="NG SERVICES",font=("times new roman",30,"bold"),fg="cyan",bg="red",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("times new roman",16),fg="black",bg="yellow").place(x=1100,y=10,height=30)
        

#===================================================================Employee Info===================================================================================


        options2=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        options3=[
            "2021",
            "2022",
            "2023",
            "2024",
            "2025",
            "2026",
            "2027",
            "2028",
            "2029",
            "2030",
            "2031",
            "2032",
        ]

        self.var_code=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_Designation=StringVar()
        self.var_Contact=StringVar()
        self.var_Email=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()

        self.var_gender.set("Select Gender")
        option= ["Male","Female","other"]
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="light gray")
        Frame1.place(x=10,y=70,width=750,height=610)
        title2=Label(Frame1,text="Employee Details",font=("Elephant",20),fg="black",bg="white",padx=10).place(x=0,y=0,relwidth=1)
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=60)
        txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_code,fg="black",bg="light yellow").place(x=220,y=65,width=200)
        btn_code=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),fg="black",bg="light gray",activebackground="cyan").place(x=440,y=65,height=30)
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=110)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,fg="black",bg="light yellow").place(x=220,y=115, width=200)
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=160)
        txt_gender=OptionMenu(Frame1,self.var_gender,* option).place(x=220,y=165)
        lbl_DOB=Label(Frame1,text="D.O.B",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=360)
        lbl_DOB1 = Label(Frame1, text="(YYYY-MM-DD)", font=("times new roman", 10), fg="black", bg="light gray").place(x=430,y=368)
        txt_DOB=Entry(Frame1,textvariable=self.var_DOB,fg="black", bg="light yellow").place(x=220,y=365, width=200, height=27)
        lbl_DOJ=Label(Frame1,text="D.O.J",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=410)
        lbl_DOB1 = Label(Frame1, text="(YYYY-MM-DD)", font=("times new roman", 10), fg="black", bg="light gray").place(x=430, y=420)
        txt_DOJ=Entry (Frame1,textvariable=self.var_DOJ,fg="black",bg="light yellow").place(x=220,y=415, width=200, height=27)
        lbl_Designation=Label(Frame1,text="Designation",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=210)
        txt_Designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_Designation,fg="black",bg="light yellow").place(x=220,y=215, width=200)
        lbl_Contact=Label(Frame1,text="Contact",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=260)
        txt_Contact=Entry(Frame1,font=("times new roman",15),textvariable=self.var_Contact,fg="black",bg="light yellow").place(x=220,y=265, width=200)
        lbl_Email=Label(Frame1,text="Email",font=("times new roman",20),fg="black",bg="light gray").place(x=10,y=310)
        txt_Email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_Email,fg="black",bg="light yellow").place(x=220,y=315, width=200)

#==================================================================Salary Info====================================================================
        
        
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_present=StringVar()
        self.var_absent=StringVar()
        self.var_Medical=StringVar()
        self.var_Incentive=StringVar()
        self.var_netsalary=StringVar()
        self.var_month.set("Month")
        self.var_year.set("Year")

        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="light gray")
        Frame2.place(x=770,y=70,width=580,height=300)
        title2=Label(Frame2,text="Salary Details",font=("Elephant",20),fg="black",bg="white",padx=10).place(x=0,y=0,relwidth=1)
        lbl_month=Label(Frame2,text="Month",font=("times new roman",17),fg="black",bg="light gray").place(x=10,y=60)
        txt_month=OptionMenu(Frame2,self.var_month,* options2).place(x=95,y=61,width=100)
        lbl_year=Label(Frame2,text="Year",font=("times new roman",17),fg="black",bg="light gray").place(x=215,y=60)
        txt_year=OptionMenu(Frame2,self.var_year,* options3).place(x=285,y=61,width=100)
        lbl_salary=Label(Frame2,text="Salary",font=("times new roman",17),fg="black",bg="light gray").place(x=400,y=60)
        txt_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_salary,fg="black",bg="light yellow").place(x=470,y=61,width=100)
        lbl_present=Label(Frame2,text="Working days",font=("times new roman",17),fg="black",bg="light gray").place(x=10,y=120)
        txt_present=Entry(Frame2,font=("times new roman",15),textvariable=self.var_present,fg="black",bg="light yellow").place(x=170,y=120,width=100)
        lbl_absent=Label(Frame2,text="Absent",font=("times new roman",17),fg="black",bg="light gray").place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,fg="black",bg="light yellow").place(x=390,y=120,width=100)
        lbl_Medical=Label(Frame2,text="Medical",font=("times new roman",16),fg="black",bg="light gray").place(x=10,y=175)
        txt_Medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Medical,fg="black",bg="light yellow").place(x=95,y=171,width=100)
        lbl_Incentive=Label(Frame2,text="Incentive",font=("times new roman",16),fg="black",bg="light gray").place(x=220,y=171)
        txt_Incentive=Entry(Frame2,font=("times new roman",15),textvariable=self.var_Incentive,fg="black",bg="light yellow").place(x=330,y=171,width=100)
        lbl_netsalary=Label(Frame2,text="Net.Sal",font=("times new roman",16),fg="black",bg="light gray").place(x=10,y=220)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_netsalary,fg="black",bg="light yellow").place(x=95,y=215,width=100)
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",16),fg="black",bg="light gray",activebackground="cyan").place(x=50,y=260,height=28)
        btn_save=Button(Frame2,text="Save",command=self.save,font=("times new roman",16),fg="black",bg="light gray",activebackground="cyan").place(x=180,y=260,height=28)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",16),fg="black",bg="light gray",activebackground="cyan").place(x=270,y=260,height=28)
        btn_update=Button(Frame2,text="Update",command=self.update,font=("times new roman",16),fg="black",bg="light gray",activebackground="cyan").place(x=365,y=260,height=28)
        btn_Delete=Button(Frame2,text="Delete",command=self.delete,font=("times new roman",16),fg="black",bg="light gray",activebackground="cyan").place(x=470,y=260,height=28)
#========================================================================Salary Frame===========================================================================
        
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=600,y=380,width=750,height=300)
        
#========================================================================QR Frame==============================================================
        
        
        
        qr_frame=Frame(Frame3,bg="light green",bd=10,relief=RIDGE)
        qr_frame.place(x=2,y=2,width=250,height=300)
        title_qr=Label(qr_frame,text="QR CODE",font=("times new roman",20),fg="black",bg="light gray",padx=10).place(x=0,y=0,relwidth=1)
        btn_generate=Button(qr_frame,command=self.generate,text="Generate QR",font=("times new roman",12),fg="black",bg='light gray', activebackground='cyan').place(x=150,y=260)
        self.qr_code=Label(qr_frame,text="No QR\nAvailable",font=("new times roman",20),fg="black",bg="light gray",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=55,width=180,height=180)
       
        
#==================================================================Salary Receipt===============================================================
        
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=251,y=2,width=495,height=300)
        title_sal=Label(sal_frame,text="Salary Receipt",font=("Elephant",18),fg="black",bg="light gray",padx=10).place(x=0,y=0,relwidth=1)
        sal_frame2=Frame(sal_frame,bg='white',bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=235)
        self.sample=f'''\tNG SERVICES
        ------------------------------------------------
Employee ID\t\t:  
Employee name\t\t:
Salary of \t\t: Mon-YYYY 
---------------------------------------------------------
Total days\t\t     : DD
Total present\t\t    : DD
Total absent\t\t     : DD
Medical\t\t     : Rs.---
Incentive\t\t     :Rs.----
Net Salary\t\t     :Rs.----
---------------------------------------------------------- 
This is computer generated slip,not
required any signature
 '''
      
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        self.txt_salary_receipt=Text(sal_frame2,font=("times new roman",13),bg="light yellow",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)
        btn_print=Button(sal_frame,text="Print",command=self.print,font=("times new roman",16),fg="black",bg='light gray', activebackground='cyan').place(x=200,y=267,height=30)
        
        self.checkConnection()
        
#===================================================================Search=====================================================================
    
    def search(self):
        try:
            con=sqlite3.connect(DB_PATH)
            cur=con.cursor()
            cur.execute("SELECT * FROM emp_salary2 WHERE e_code='%s' "%self.var_code.get())
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Employee Code",parent=self.root)
 
            else:

             
                self.var_code.set(row[0])
                self.var_name.set(row[1])
                self.var_gender.set(row[2])
                self.var_Designation.set(row[3])
                self.var_Contact.set(row[4])
                self.var_Email.set(row[5])
                self.var_DOB.set(row[6])
                self.var_DOJ.set(row[7])
                self.var_month.set(row[8])
                self.var_year.set(row[9])
                self.var_salary.set(row[10])
                self.var_present.set(row[11])
                self.var_absent.set(row[12])
                self.var_Medical.set(row[13])
                self.var_Incentive.set(row[14])
                self.var_netsalary.set(row[15])
                file_=open("salary_receipt"+str(row[16]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                con.commit()
                con.close()
                for i in file_:
                     self.txt_salary_receipt.insert(END,i)
                file_.close()
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
    
    
#======================================================================Save====================================================================
    
    def save(self):
        if self.var_code.get()=="":
            messagebox.showerror("Error","Employee information is required")
            return
     
         
        
        try:
            con=sqlite3.connect(DB_PATH) 
            cur=con.cursor()
            cur.execute("SELECT * FROM emp_salary2 WHERE e_code='%s' "%self.var_code.get())
            rows=cur.fetchone()
            #print(row) 
            if rows!=None:
                 messagebox.showerror("Error","This Employee ID has already been taken",parent=self.root)
            else:
               cur.execute("insert into emp_salary2 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                   
               
                   self.var_code.get(),
                   self.var_name.get(),
                   self.var_gender.get(),
                   self.var_Designation.get(),
                   self.var_Contact.get(),
                   self.var_Email.get(),
                   self.var_DOB.get(),
                   self.var_DOJ.get(),
                   self.var_month.get(),
                   self.var_year.get(),
                   self.var_salary.get(),
                   self.var_present.get(),
                   self.var_absent.get(),
                   self.var_Medical.get(),
                   self.var_Incentive.get(),
                   self.var_netsalary.get(),
                   self.var_code.get()+".txt"
               )
               )       
               con.commit()
               con.close()
               file_=open("salary_receipt"+str(self.var_code.get())+".txt",'w+')
               file_.write(self.txt_salary_receipt.get('1.0',END))
               file_.close()
               messagebox.showinfo("Success","Record added successfully")    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
#=============================================================Calculate=========================================================================
    
    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_absent.get()==''  or  self.var_present.get()=='' or self.var_Incentive.get()=='' or self.var_Medical.get()=='':
            messagebox.showerror("Error","All fields are required")

        else:
            per_day=int(self.var_salary.get())/int(self.var_present.get())
            work_day=int(self.var_present.get())-float(self.var_absent.get())
            sal=per_day*work_day
            incentive=float(self.var_Incentive.get())
            medical=float(self.var_Medical.get())

            net_sal=(sal+incentive)-medical
            self.var_netsalary.set(str(round(net_sal,2)))
            
#=================================================Update the receipt=======================================================================
            
            new_sample=f'''\tNG SERVICES
        ------------------------------------------------
Employee ID\t\t: {self.var_code.get()}
Employee name\t\t: {self.var_name.get()}
Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
---------------------------------------------------------
Total days\t\t       : {(self.var_present.get())}  
Total present\t\t    : {str(int(self.var_present.get())-float(self.var_absent.get()))}
Total absent\t\t     : {self.var_absent.get()}
Medical\t\t           : Rs.{self.var_Medical.get()}  
Incentive\t\t        : Rs.{self.var_Incentive.get()}
Net Salary\t\t       : Rs.{self.var_netsalary.get()}
---------------------------------------------------------- 
This is computer generated slip,not
required any signature
 '''
             
            self.txt_salary_receipt.delete(1.0,END) 
            self.txt_salary_receipt.insert(END,new_sample)
            
#=================================================Update the receipt=======================================================================
            
            new_sample=f'''\tNG SERVICES
        ------------------------------------------------
Employee ID\t\t: {self.var_code.get()}
Employee name\t\t: {self.var_name.get()}
Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
---------------------------------------------------------
Total days\t\t       : {(self.var_present.get())}  
Total present\t\t    : {str(int(self.var_present.get())-float(self.var_absent.get()))}
Total absent\t\t     : {self.var_absent.get()}
Medical\t\t          : Rs.{self.var_Medical.get()}  
Incentive\t\t        : Rs.{self.var_Incentive.get()}
Net Salary\t\t       : Rs.{self.var_netsalary.get()}
---------------------------------------------------------- 
This is computer generated slip,not
required any signature
 '''
             
            self.txt_salary_receipt.delete(1.0,END) 
            self.txt_salary_receipt.insert(END,new_sample)        
            
#======================================================================Clear=======================================================================       
    
    def clear(self):
                
            self.var_code.set('')
            self.var_name.set('')
            self.var_gender.set('Select Gender')
            self.var_Designation.set('')
            self.var_Contact.set('')
            self.var_Email.set('')
            self.var_DOB.set('')
            self.var_DOJ.set('')
            self.var_month.set('Month')
            self.var_year.set('Year')
            self.var_salary.set('')
            self.var_present.set('')
            self.var_absent.set('')
            self.var_Medical.set('')
            self.var_Incentive.set('')
            self.var_netsalary.set('')
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,self.sample)
 #=====================================================================CheckConnection===========================================================    
             
    def checkConnection(self):
        try:
           con=sqlite3.connect("esc2.db")
           cur=con.cursor()
           cur.execute("SELECT * FROM emp_salary2")
           rows=cur.fetchall()
           #print(rows)
           
          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")       
               
#================================================Print==========================================================================================           
    def print(self):
          file_=tempfile.mktemp(".txt") 
          open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))      
          os.startfile(file_,'print')    
            
    #===============================================Update======================================================================================
    
    def update(self):
         
        if self.var_code.get()=='':
            messagebox.showwarning("Error","Employee information are required")
        else: 
           try:
            con=sqlite3.connect(DB_PATH)
            cur=con.cursor()
            cur.execute("SELECT * FROM emp_salary2 WHERE e_code='%s' "%self.var_code.get())
            row=cur.fetchone()
            #print(row) 
            if row==None:
                 messagebox.showerror("Error","This Employee ID is invalid",parent=self.root)
            else:
               cur.execute("UPDATE `emp_salary2` SET  `e_name`=?,`e_gender`=?,`Designation`=?,`Contact`=?,`Email`=?,`D.O.B`=?,`D.O.J`=?,`Month`=?,`Year`=?,`Salary`=?,`Working days`=?,`Absent`=?,`Medical`=?,`Incentive`=?,`net salary`=?,`salary_receipt`=? WHERE `e_code`=?",

               
                  ( 
               
                   self.var_name.get(),
                   self.var_gender.get(),
                   self.var_Designation.get(),
                   self.var_Contact.get(),
                   self.var_Email.get(),
                   self.var_DOB.get(),
                   self.var_DOJ.get(),
                   self.var_month.get(),
                   self.var_year.get(),
                   self.var_salary.get(),
                   self.var_present.get(),
                   self.var_absent.get(),
                   self.var_Medical.get(),
                   self.var_Incentive.get(),
                   self.var_netsalary.get(),
                   self.var_code.get()+".txt",
                   self.var_code.get()
                  )   
               
               )       
               con.commit()
               con.close()
               file_=open("salary_receipt"+str(self.var_code.get())+".txt",'w')
               file_.write(self.txt_salary_receipt.get('1.0',END))
               file_.close()
               messagebox.showinfo("Success","Record updated successfully")    
           except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
           
                              
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_absent.get()=='' or self.var_present.get()=='':
                messagebox.showerror("Error","All fields are required")
        else:
           per_day=int(self.var_salary.get())/int(self.var_present.get())
           work_day=int(self.var_present.get())-float(self.var_absent.get())
           sal=per_day*work_day
           incentive=float(self.var_Incentive.get())
           medical=float(self.var_Medical.get())
           net_sal=(sal+incentive)-medical
           self.var_netsalary.set(str(round(net_sal,2)))

            #===================================Update the receipt========================================================================================
           new_sample=f'''\tNG SERVICES
        ------------------------------------------------
Employee ID\t\t: {self.var_code.get()}
Employee name\t\t: {self.var_name.get()}
Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
---------------------------------------------------------
Total days\t\t       : {(self.var_present.get())}  
Total present\t\t    : {str(int(self.var_present.get())-float(self.var_absent.get()))}
Total absent\t\t     : {self.var_absent.get()}
Medical\t\t          : Rs.{self.var_Medical.get()}  
Incentive\t\t        : Rs.{self.var_Incentive.get()}
Net Salary\t\t       : Rs.{self.var_netsalary.get()}
---------------------------------------------------------- 
This is computer generated slip,not
required any signature
 '''
           self.txt_salary_receipt.delete(1.0,END) 
           self.txt_salary_receipt.insert(END,new_sample) 
  
 #==============================================Employee Frame=================================================================================
    
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll System")
        self.root2.geometry("1350x700+0+0")
        self.root2.config(bg="white")
        title=Label(self.root2,text="Employee Details",font=("times new roman",20,"bold"),fg="white",bg="blue",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()
        scroll_y=Scrollbar(self.root2,orient=VERTICAL)
        scroll_x=Scrollbar(self.root2,orient=HORIZONTAL)
        scroll_x.pack(fill=X,side=BOTTOM)
        scroll_y.pack(fill=Y,side=RIGHT)
        
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_code', 'e_name', 'e_gender', 'Designation','Contact','Email','D.O.B','D.O.J','Month', 'Year', 'Salary', 'Working days', 'Absent', 'Medical', 'Incentive','net salary','salary_receipt'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        self.employee_tree.heading('e_code',text='EID')
        self.employee_tree.heading('e_name',text='NAME')
        self.employee_tree.heading('e_gender',text='GENDER')
        self.employee_tree.heading('Designation',text='DESIGNATION')
        self.employee_tree.heading('Contact',text='CONTACT')
        self.employee_tree.heading('Email',text='EMAIL')
        self.employee_tree.heading('D.O.J',text='D.O.J')
        self.employee_tree.heading('D.O.B',text='D.O.B')
        self.employee_tree.heading('Month',text='MONTH')
        self.employee_tree.heading('Year',text='YEAR')
        self.employee_tree.heading('Salary',text='SALARY')
        self.employee_tree.heading('Working days',text='WORKING DAYS')
        self.employee_tree.heading('Absent',text='ABSENT')
        self.employee_tree.heading('Medical',text='Medical')
        self.employee_tree.heading('Incentive',text='Incentive')
        self.employee_tree.heading('net salary',text='Net SALARY')
        self.employee_tree.heading('salary_receipt',text='SALARY_RECEIPT')
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('e_code',width=8)
        self.employee_tree.column('e_name',width=100)
        self.employee_tree.column('e_gender',width=30)
        self.employee_tree.column('Designation',width=50)
        self.employee_tree.column('Contact',width=50)
        self.employee_tree.column('Email',width=50)
        self.employee_tree.column('D.O.B',width=50)
        self.employee_tree.column('D.O.J',width=50)
        self.employee_tree.column('Month',width=40)
        self.employee_tree.column('Year',width=10)
        self.employee_tree.column('Salary',width=50)
        self.employee_tree.column('Working days',width=80)
        self.employee_tree.column('Absent',width=10)
        self.employee_tree.column('Medical',width=10)
        self.employee_tree.column('Incentive',width=10)
        self.employee_tree.column('net salary',width=50)
        self.employee_tree.column('salary_receipt',width=88)
        scroll_x.config(command=self.employee_tree.xview)
        scroll_y.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()
    
#=====================================Show Employee's Details===================================================================================  
 
    def show(self):
            try:
             con=sqlite3.connect(DB_PATH)
             cur=con.cursor()
             cur.execute("SELECT * FROM emp_salary2")
             rows=cur.fetchall()
           #print(rows)
             self.employee_tree.delete(*self.employee_tree.get_children())
             for row in rows:
                 self.employee_tree.insert('',END,values=row)
             con.close()
          
            except Exception as ex:
             messagebox.showerror("Error",f"Error due to: {str(ex)}")
             
 #=========================================================Delete================================================================================       
        
    def delete(self):
        if self.var_code.get()=="":
            messagebox.showerror("Error","Employee information is required")
        else:
          try:
            con=sqlite3.connect(DB_PATH)
            cur=con.cursor()
            cur.execute("SELECT * FROM emp_salary2 WHERE e_code='%s' "%self.var_code.get())
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Employee Code",parent=self.root)
 
            else:
                op=messagebox.askyesnocancel("Confirm","Do you really want to delete?")
                if op==True:
                 cur.execute("DELETE FROM emp_salary2 WHERE e_code='%s' "%self.var_code.get())
                 con.commit()
                 con.close()
          except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")    
            
#=============================================QR Generator================================================================            

    def generate(self):
        if self.var_code.get()=='' or self.var_name.get()=='' or self.var_gender.get()==''or self.var_Designation.get()==''or self.var_Contact.get()==''or self.var_Email.get()==''or self.var_DOB.get()=='' or self.var_DOJ.get()=='':
                messagebox.showerror("Error","All fields are required")
        else:
            qr_data=(f"Employee ID: {self.var_code.get()}\nEmployee name: {self.var_name.get()}\nEmployee Gender: {self.var_gender.get()}\nEmployee Designation : {self.var_Designation.get()}\nEmployee Contact: {self.var_Contact.get()}\nEmployee Email: {self.var_Email.get()}\nEmployee DOJ: {self.var_DOB.get()}\nEmployee DOB: {self.var_DOJ.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            self.image=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.image)
     
     
     
     
     
     
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()


