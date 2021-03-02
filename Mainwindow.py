from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
from classes.Employee import Employee

# If database not found, create one then delete the 'con' object
try:
    from classes.Connection import Connection
    con = Connection()
except:  
    con.create_database('msc_database')
finally:
    del con

# If table 'employees' not found, create one then delete the 'con' object
try:
    from classes.Connection import Connection
    con = Connection()
    con.create_employee_table('employees')
except Exception:
    pass
finally:
    del con


root=Tk()


class MainWindow:
    #para widget ng mainform
    def __init__(self, root, *args, **kwargs):

        self.root = root
        self.root.title("RFID SYSTEM")
        self.root.geometry("1200x700+200+70")
        self.root.configure(bg="#006600")
        self.root.resizable(False, False)

        #para sa background image
        self.image = ImageTk.PhotoImage(file="images/msc.jpg")
        self.label = Label(self.root, image=self.image)
        self.label.place(x=0, y=0)
       
        #Function for Main button. para mapunta sa front ung Frame
        def clicked_home():
            self.frame_home.lift()
                 
        ###Para sa Employee Frame#####       
        def clicked_emp():
            self.frame_emp.lift()
            #Mga label sa pag insert ng Data
            self.head_label = Label(self.frame_emp, text="Register Employee Information",
            font=("Andalus", 24, 'bold'), fg="white", bg="#339900", borderwidth=10)
            self.head_label.place(x=0, y=20, width=880)
            
            self.fname_label = Label(self.frame_emp, text="First Name", font=("Andalus", 12, 'bold'), 
            fg="black")
            self.fname_label.place(x=20, y=100)
            
            self.mname_label = Label(self.frame_emp, text="Middle Name", font=("Andalus", 12, 'bold'), 
            fg="black")
            self.mname_label.place(x=20, y=185)
           
            self.lname_label = Label(self.frame_emp, text="Last Name", font=("Andalus", 12, 'bold'),
            fg="black")     
            self.lname_label.place(x=20, y=270)

            self.gender_label = Label(self.frame_emp, text="Gender", font=("Andalus", 12, 'bold'),
            fg="black")
            self.gender_label.place(x=20, y=350)

            self.age_label = Label(self.frame_emp, text="Age", font=("Andalus", 12, 'bold'),
            fg="black")     
            self.age_label.place(x=20, y=430)

            self.address_label = Label(self.frame_emp, text="Address", font=("Andalus", 12, 'bold'),
            fg="black")     
            self.address_label.place(x=20, y=510)

            #label sa right side ng employee frame
            self.department_label = Label(self.frame_emp, text="Department", font=("Andalus", 12, 'bold'),
            fg="black")     
            self.department_label.place(x=350, y=95)

            self.position_label = Label(self.frame_emp, text="Position", font=("Andalus", 12, 'bold'),
            fg="black")
            self.position_label.place(x=350, y=181)

            self.rfid_label = Label(self.frame_emp, text="RFID UID", font=("Andalus", 12, 'bold'),
            fg="black")
            self.rfid_label.place(x=350, y=265)

            self.email_label = Label(self.frame_emp, text="Email Address", font=("Andalus", 12, 'bold'),
            fg="black")
            self.email_label.place(x=350, y=350)

            self.contact_label = Label(self.frame_emp, text="Contact Number", font=("Andalus", 12, 'bold'),
            fg="black")
            self.contact_label.place(x=350, y=435)

            self.picbox_label = Label(self.frame_emp, text="", bg="darkgreen")
            self.picbox_label.place(x=680, y=125, width=130, height=130)

            self.image_path_label = Label(self.frame_emp, text="Image Path")
            self.image_path_label.place(x=680, y=260)
            self.image_path_label.place_forget()
           
            #Mga Entry box para sa pag insert
            self.fname_entry = Entry(self.frame_emp, font=("calibri",14), borderwidth=5)
            self.fname_entry.place(x=20, y=135, width=250)

            self.mname_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.mname_entry.place(x=20, y=220, width=250)

            self.lname_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.lname_entry.place(x=20, y=305, width=250)

            self.age_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.age_entry.place(x=20, y=465, width=250)

            self.address_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.address_entry.place(x=20, y=550, width=250)

            #entry box for employee registration right side
            self.email_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.email_entry.place(x=350, y=382, width=250)

            self.contact_number_entry = Entry(self.frame_emp, font=("calibri", 14), borderwidth=5)
            self.contact_number_entry.place(x=350, y=463, width=250)

            #combo box for department options
            options_dep = [
                "",
                "SICS",
                "SED",
                "SENG"
            ]
            self.department_var = StringVar()
            self.dep_cbox = ttk.Combobox(self.frame_emp, textvariable=self.department_var, value=options_dep)
            self.dep_cbox.current(0)
            self.dep_cbox.place(x=350, y=131, width=250, height=31)
            
            #combo box for positions options
            options_position = [
                "",
                "Support Staff",
                "College Lecturer",
                "Instructor I"
            ]
            self.position_var = StringVar()
            self.position_cbox = ttk.Combobox(self.frame_emp, textvariable=self.position_var, value=options_position)
            self.position_cbox.current(0)
            self.position_cbox.place(x=350, y=216, width=250, height=31)

            self.rfid_text = Entry(self.frame_emp)
            self.rfid_text.place(x=350, y=302, width=250, height=31)

            #combo box for department options
            options_gender = [
                "",
                "Male",
                "Female"
            ]
            self.gender_var = StringVar()
            self.gender_cbox = ttk.Combobox(self.frame_emp, textvariable=self.gender_var, value=options_gender)
            self.gender_cbox.current(0)
            self.gender_cbox.place(x=20, y=385, width=250, height=31)

            # REGISTER button for the employee registration
            self.btn_register = Button(self.frame_emp, text="Register", borderwidth=3, relief=GROOVE,
            activebackground="#0B0F08", activeforeground="white", fg="white", bg="green", 
            font=("arial", 15, 'bold'), command=self.register_employee)
            self.btn_register.place(x=20, y=610, width=250, height=50)

            # BROWSE button
            self.browse_btn = Button(self.frame_emp, text='Browse', command=self.open_image)
            self.browse_btn.place(x=680, y=302)

        # Department Tab
        def clicked_dep():
            self.frame_dep.lift()
        
        # Position Tab
        def clicked_pos():
            self.frame_pos.lift()
           
        #Container for Main button example: Home,Employee etc.
        self.canvas = Canvas(self.root)
        self.canvas.place(x=10, y=10, width=300, height=680)
        #ito ung sa image na png
        
        self.image1 = ImageTk.PhotoImage(file="images/msclogo1.png")
        self.label1 = Label(self.canvas, image=self.image1, borderwidth=10)
        self.label1.place(x=75, y=5)

        #Home button
        self.Home = Button(self.canvas, text="HOME", borderwidth=5, relief=GROOVE, activebackground="#0B0F08",
        activeforeground="white", fg="white", bg="green", font=("arial", 15, 'bold'), command=clicked_home)
        self.Home.place(x=10, y=150, width=280, height=60)
               
        #employee button
        self.employee = Button(self.canvas, text="EMPLOYEE", borderwidth=5, relief=GROOVE, 
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'), command=clicked_emp)
        self.employee.place(x=10, y=210, width=280, height=60)
         
        #department button
        self.department = Button(self.canvas, text="DEPARTMENT", borderwidth=5, relief=GROOVE,
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'), command=clicked_dep)
        self.department.place(x=10, y=270, width=280, height=60)

        #post button
        self.post = Button(self.canvas, text="POSITION", borderwidth=5, relief=GROOVE,
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'), command=clicked_pos)
        self.post.place(x=10, y=330, width=280, height=60)

        #settings button
        self.settings = Button(self.canvas, text="SETTINGS", borderwidth=5, relief=GROOVE,
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'))
        self.settings.place(x=10, y=390, width=280, height=60)

        #employee button    
        self.event = Button(self.canvas, text="EVENT", borderwidth=5, relief=GROOVE,
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'))
        self.event.place(x=10, y=450, width=280, height=60)

        #employee button
        self.employee = Button(self.canvas, text="STUDENT", borderwidth=5, relief=GROOVE,
        activebackground="#0B0F08", activeforeground="white", fg="white", bg="green",
        font=("arial", 15, 'bold'))
        self.employee.place(x=10, y=510, width=280, height=60)
       
        #####Frame para sa Main Button#####
        #frame for position info
        self.frame_pos = Frame(self.root, borderwidth=10, bg="red")
        self.frame_pos.place(x=320, y=10, width=870, height=680)
        #frame for department info
        self.frame_dep = Frame(self.root, borderwidth=10, bg="yellow")
        self.frame_dep.place(x=320, y=10, width=870, height=680)
        #frame for employee info
        self.frame_emp = Frame(self.root)
        self.frame_emp.place(x=320, y=10, width=870, height=680)
        #frame for home info
        self.frame_home = Frame(self.root)
        self.frame_home.place(x=320, y=10, width=870, height=680)

    # REGISTERING Employee
    def register_employee(self):
        self.check_if_empty()

        employee = Employee()
        employee.uid = self.rfid_text.get()
        employee.first_name = self.fname_entry.get()
        employee.middle_name = self.mname_entry.get()
        employee.last_name = self.lname_entry.get()
        employee.age = self.age_entry.get()
        employee.gender = self.gender_var.get()
        employee.address = self.address_entry.get()
        employee.email = self.email_entry.get()
        employee.employee_image = self.image_path_label.cget('text')
        employee.contact_number = self.contact_number_entry.get()
        employee.insert_employee_record()
        
        self.clear_text()

    # File Dialog for browsing image
    def open_image(self):
        self.file_name = filedialog.askopenfilename(initialdir = "/", title="Select a Photo",
        filetype=(("jpeg","*.jpg"),("png","*.png")))
        self.image_path_label.configure(text = self.file_name)
        self.image = ImageTk.PhotoImage(Image.open(self.file_name))
        self.picbox_label = ttk.Label(self.frame_emp, image=self.image)
        self.picbox_label.place(x=680, y=125, width=130, height=130)
        # Debugging purpose
        # print(self.image_path_label.cget('text'))

    def check_if_empty(self):
        if self.fname_entry.get() == '' or self.mname_entry.get() == '' or self.lname_entry.get() == '' \
            or self.age_entry.get() == '' or self.email_entry.get() == '' or self.address_entry.get() == '' \
            or self.contact_number_entry.get() == '' or self.gender_var.get() == '' \
            or self.position_var.get() == '' or self.department_var.get() == '' \
            or self.image_path_label.cget('text') == '' or self.rfid_text.get() == '':
            messagebox.showwarning("Empty field(s)", "Please fill out all the form.")

    def clear_text(self):
        self.fname_entry.delete(0, 'end')
        self.mname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.contact_number_entry.delete(0, 'end')
        self.image_path_label.configure(text="")
        self.gender_cbox.current(0)
        self.dep_cbox.current(0)
        self.position_cbox.current(0)
        self.rfid_text.delete(0, 'end')



main=MainWindow(root)
root.mainloop()