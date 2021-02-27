from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

root=Tk()
 
       
class MainWindow:
    #para widget ng mainform
    def __init__(self,root,*args,**kwargs):
       
        self.root=root
        self.root.title("RFID SYSTEM")
        self.root.geometry("1200x700+200+70")
        self.root.configure(bg="#006600")
        self.root.resizable(False,False)

        #para sa background image
        self.image=ImageTk.PhotoImage(file="background_win.jpg")
        self.label=Label(self.root,image=self.image)
        self.label.place(x=0,y=0)
       
       

        
        #Function for Main button. para mapunta sa front ung Frame
        def clicked_home():
            self.frame_home.lift()
            
            
        ###Para sa Employee Frame#####       
        def clicked_emp():
            self.frame_emp.lift()
             #Mga label sa pag insert ng Data
            self.head_label=Label(self.frame_emp,text="Register Employee Information",
            font=("Andalus",24,'bold'),fg="white",bg="#339900",borderwidth=10)
            self.head_label.place(x=0,y=20,width=880)
            
            self.name_label=Label(self.frame_emp,text="First Name",font=("Andalus",12,'bold'),fg="black")
            self.name_label.place(x=20,y=100)
            
            self.mname_label=Label(self.frame_emp,text="Middle Name",font=("Andalus",12,'bold'),fg="black")
            self.mname_label.place(x=20,y=185)
           
            self.lname_label=Label(self.frame_emp,text="Last Name",font=("Andalus",12,'bold'),fg="black")     
            self.lname_label.place(x=20,y=270)

            self.gender_label=Label(self.frame_emp,text="Sex",font=("Andalus",12,'bold'),fg="black")
            self.gender_label.place(x=20,y=350)

            self.bdate_label=Label(self.frame_emp,text="Birth Date",font=("Andalus",12,'bold'),fg="black")     
            self.bdate_label.place(x=20,y=430)

            self.address_label=Label(self.frame_emp,text="Address",font=("Andalus",12,'bold'),fg="black")     
            self.address_label.place(x=20,y=510)

            #label sa right side ng employee frame
            self.department_label=Label(self.frame_emp,text="Department",font=("Andalus",12,'bold'),fg="black")     
            self.department_label.place(x=350,y=95)

            self.position_label=Label(self.frame_emp,text="Position",font=("Andalus",12,'bold'),fg="black")
            self.position_label.place(x=350,y=181)

            self.Salary_label=Label(self.frame_emp,text="Salary Grade",font=("Andalus",12,'bold'),fg="black")
            self.Salary_label.place(x=350,y=265)

            self.email_label=Label(self.frame_emp,text="Email Address",font=("Andalus",12,'bold'),fg="black")
            self.email_label.place(x=350,y=350)

            self.contact_label=Label(self.frame_emp,text="Contact Details",font=("Andalus",12,'bold'),fg="black")
            self.contact_label.place(x=350,y=435)

            self.picbox_label=Label(self.frame_emp,text="",bg="darkgreen")
            self.picbox_label.place(x=680,y=125, width=130,height=130)
           

             #Mga Entry box para sa pag insert
            self.name_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.name_entry.place(x=20,y=135,width=250)

            self.mname_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.mname_entry.place(x=20,y=220,width=250)

            self.lname_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.lname_entry.place(x=20,y=305,width=250)

            self.birthdate_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.birthdate_entry.place(x=20,y=465,width=250)

            self.address_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.address_entry.place(x=20,y=550,width=250)

            #entry box for employee registration right side
            self.email_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.email_entry.place(x=350,y=382,width=250)

            self.email_entry=Entry(self.frame_emp,font=("calibri",14),borderwidth=5)
            self.email_entry.place(x=350,y=463,width=250)

            #combo box for department options
            options_dep = [
                "",
                "SICS",
                "SED",
                "SENG"
            ]
            self.dep_cbox= ttk.Combobox(self.frame_emp,value=options_dep)
            self.dep_cbox.current(0)
            self.dep_cbox.place(x=350,y=131,width=250,height=31)
            
            #combo box for positions options
            options_position = [
                "",
                "Support Staff",
                "College Lecturer",
                "Instructor I"
            ]
            self.position_cbox= ttk.Combobox(self.frame_emp,value=options_position)
            self.position_cbox.current(0)
            self.position_cbox.place(x=350,y=216,width=250,height=31)

             #combo box for salary Grade
            options_salaryg = [
                "","1","2","3","4","5","6","7","8","9",
                "10","11","12","13","14","15","16","17","18"
            ]
            self.salaryg_cbox= ttk.Combobox(self.frame_emp,value=options_salaryg)
            self.salaryg_cbox.current(0)
            self.salaryg_cbox.place(x=350,y=302,width=250,height=31)

            #combo box for department options
            options_gender = [
                "","MALE",
                "FEMALE"
            ]
            self.gender_cbox= ttk.Combobox(self.frame_emp,value=options_gender)
            self.gender_cbox.current(0)
            self.gender_cbox.place(x=20,y=385,width=250,height=31)

            
            
            

            #Register button for the employee registration
            self.btn_save = Button(self.frame_emp, text="Register",borderwidth=3,relief=GROOVE,activebackground="#0B0F08",
            activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_emp)
            self.btn_save.place(x=20,y=610,width=250,height=50)


        def clicked_dep():
            self.frame_dep.lift()
        def clicked_pos():
            self.frame_pos.lift()
   
        
        #Container for Main button example: Home,Employee etc.
        self.canvas = Canvas(self.root)
        self.canvas.place(x=10,y=10,width=300,height=680)
        #ito ung sa image na png
        
        self.image1=ImageTk.PhotoImage(file="msclogo1.png")
        self.label1=Label(self.canvas,image=self.image1,borderwidth=10)
        self.label1.place(x=75,y=5)


        #Home button
        self.Home = Button(self.canvas, text="HOME",borderwidth=5,relief=GROOVE, activebackground="#0B0F08",
        activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_home)
        self.Home.place(x=10,y=150,width=280,height=60)
        
    
       
        #employee button
        self.employee = Button(self.canvas, text="EMPLOYEE",borderwidth=5,relief=GROOVE,activebackground="#0B0F08",
         activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'),command=clicked_emp)
        self.employee.place(x=10,y=210,width=280,height=60)
         

        #employee button
        self.department = Button(self.canvas, text="DEPARTMENT",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold')
        ,command=clicked_dep)
        self.department.place(x=10,y=270,width=280,height=60)

        #employee button
        self.post = Button(self.canvas, text="POSITION",borderwidth=5,relief=GROOVE, 
        activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold')
        ,command=clicked_pos)
        self.post.place(x=10,y=330,width=280,height=60)

          #employee button
        self.settings = Button(self.canvas, text="SETTINGS",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'))
        self.settings.place(x=10,y=390,width=280,height=60)

        #employee button    
        self.event = Button(self.canvas, text="EVENT",borderwidth=5,relief=GROOVE,
         activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'))
        self.event.place(x=10,y=450,width=280,height=60)

        #employee button
        self.employee = Button(self.canvas, text="STUDENT",borderwidth=5,relief=GROOVE, activebackground="#0B0F08",activeforeground="white",fg="white",bg="green",font=("arial",15,'bold'))
        self.employee.place(x=10,y=510,width=280,height=60)

       
        #####Frame para sa Main Button#####
        #frame for position info
        self.frame_pos = Frame(self.root,borderwidth=10,bg="red")
        self.frame_pos.place(x=320,y=10,width=870,height=680)
        #frame for department info
        self.frame_dep = Frame(self.root,borderwidth=10,bg="yellow")
        self.frame_dep.place(x=320,y=10,width=870,height=680)
        #frame for employee info
        self.frame_emp = Frame(self.root)
        self.frame_emp.place(x=320,y=10,width=870,height=680)
        #frame for home info
        self.frame_home = Frame(self.root)
        self.frame_home.place(x=320,y=10,width=870,height=680)

       
 

       
        

       


main=MainWindow(root)
root.mainloop()