from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "esc2.db")



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        #BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="Images/icon.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #==========================================TITLE================================================
        lbl_title=Label(self.root,text="Employee Payroll System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=80)
        
        #FRAME
        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        #ICON
        img1=Image.open(r"Images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        #GET STARTED
        get_start=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_start.place(x=75,y=100)
        
        #LABEL
        username_lbl=Label(frame,text="Username:",font=("arial",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password:",font=("arial",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("arial",15,"bold"),show = "*")
        self.txtpass.place(x=40,y=250,width=270)
        
        # USERNAME ICON
        img2=Image.open(r"Images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
        
        #PASSWORD ICON
        img3=Image.open(r"Images\lock-512.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        
        #Login Button
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #Register Button
        registerbtn=Button(frame,command=self.register_window,text="Sign-Up",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=0,y=350,width=160)
        
        #Forgot Password
        forgotpassbtn=Button(frame,command=self.forgot_pass,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=0,y=380,width=160)
        
    #REGISTER WINDOW
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
    #LOGIN
    def login(self):
        if  self.txtuser.get()=="":
            messagebox.showerror("Error","Enter Username")
        elif self.txtpass.get()=="":
            messagebox.showerror("Error","Enter Password")
        elif self.txtuser.get()=="root" and self.txtpass.get()=="root":
            messagebox.showinfo("Success","Login Successfully")
            self.root.destroy()
            import EPS
        else:
            conn = sqlite3.connect(DB_PATH)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where USERNAME=? and PASSWORD=?",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                        ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.root.destroy()
                import EPS
            conn.commit()
            conn.close()
            
    #Reset Password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Please Select Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please Enter your Security Question",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter Your new Password",parent=self.root2)
        else:
            conn=sqlite3.connect(DB_PATH)
            my_cursor=conn.cursor()
            query1=("select * from register where USERNAME=? and SECURITY_Q=? and SECURITY_A=?")
            value1=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","PLEASE ENTER CORRECT ANSWER",parent=self.root2)
            else:
                query2=("update register set PASSWORD=? where USERNAME=?")
                value2=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query2,value2)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS","NEW PASSWORD SET",parent=self.root2)
                self.root2.destroy()
            
            
    #Forgot Password        
    def forgot_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter Email Address")
        else:
            conn=sqlite3.connect(DB_PATH)
            my_cursor=conn.cursor()
            query=("select * from register where USERNAME=?")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("ERROR","Please Enter Valid email address")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("FORGOT PASSWORD")
                self.root2.geometry("340x450+610+170")
                
                #LABEL
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                #SECURITY QUESTION
                security_Q=Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Colour","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                #SECURITY ANSWER
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security_A = ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)

                
                #PASSWORD
                newpass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                newpass.place(x=50,y=220)

                #self.var_txt_newpass=StringVar()
                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                #Button
                btn=Button(self.root2,command=self.reset_pass,text="RESET",font=("times new roman",15),fg="white",bg="green")
                btn.place(x=130,y=320)
                
                
                

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        
        #Variables
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #=======================================BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file=r"Images\hackers2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #LEFT IMAGE
        self.bg1=ImageTk.PhotoImage(file=r"Images\thought-good-morning-messages-LoveSove.jpg")
        left_bg1=Label(self.root,image=self.bg1)
        left_bg1.place(x=50,y=100,width=470,height=550)
        
        #FRAME
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl =Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #==============================================LABEL AND ENTRIES
        
        #---------------ROW1
        
        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        lname_entry.place(x=370,y=130,width=250)
        
        
        #---------------ROW2
        
        contact = Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text="Username:",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #------------------ROW4
        
        security_Q=Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Favourite Colour","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)
        
        
        #--------------------ROW4
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15),show="*")
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show="*")
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #========================================Check Button
        
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I agree to the terms & conditions.",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        
        #=================================================Buttons
        
        #Register
        img=Image.open(r"Images\register.jpg")
        img=img.resize((200,55),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=430,width=200)
        
        
        #Login
        img1=Image.open(r"Images\loginpng.png")
        img1=img1.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=380,y=430,width=200)
        
        
    #===================================Function
    
    def register_data(self):
        if self.var_fname.get()=="":
            messagebox.showerror("Error","Enter your First Name",parent=self.root)
            
        elif self.var_lname.get()=="":
            messagebox.showerror("Error","Enter your Last Name",parent=self.root)
            
        elif self.var_contact.get()=="":
            messagebox.showerror("Error","Enter your Contact No.",parent=self.root)
        
        elif self.var_email.get()=="":
            messagebox.showerror("Error","Enter your Username",parent=self.root)
        
        elif self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","Choose your Security Question",parent=self.root)
        
        elif self.var_securityA.get()=="":
            messagebox.showerror("Error","Enter your Security Answer",parent=self.root)
        
        elif self.var_pass.get()=="":
            messagebox.showerror("Error","Enter your New Password",parent=self.root)
        
        elif self.var_confpass.get()=="":
            messagebox.showerror("Error","Re-Enter your New Password",parent=self.root)
        
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password does not match",parent=self.root)
        
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree to our Terms and Conditions",parent=self.root)
        
        else:

            conn = sqlite3.connect(DB_PATH)
            my_cursor=conn.cursor()
            query="select * from register where USERNAME=?"
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already in use",parent=self.root)

            else:
                my_cursor.execute("insert into register values(?,?,?,?,?,?,?)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        ))

                messagebox.showinfo("Success", "Successfully Signed-Up", parent=self.root)
                self.var_fname.set(" "),
                self.var_lname.set(""),
                self.var_contact.set(""),
                self.var_email.set(""),
                self.var_securityQ.set("Select"),
                self.var_securityA.set(""),
                self.var_pass.set(""),
                self.var_confpass.set(""),
                self.var_check.set("offvalue=0")
            conn.commit()
            conn.close()


def return_login(self):


    self.root.destroy()

if __name__ == '__main__':
    main()