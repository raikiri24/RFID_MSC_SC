from tkinter import *
from PIL import ImageTk, Image


class LoginWindow:
    #para widget ng login
    def __init__(self):

        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("1200x700+200+70")
        self.root.resizable(False,False)

        #para sa background image
        self.image=ImageTk.PhotoImage(file="msc.jpg")
        self.label=Label(self.root,image=self.image)
        self.label.pack()
        
        #canvas
        self.canvas = Canvas(self.root,borderwidth=10)
        self.canvas.place(x=390,y=170,width=400,height=400)
      
        #ito ung sa image na png
        self.image1=ImageTk.PhotoImage(file="msclogo1.png")
        self.label1=Label(self.root,image=self.image1,borderwidth=10)
        self.label1.place(x=527,y=170)

        #label and entry box for user and password
        self.userlabel=Label(self.canvas,text="USER_ID",font=("Andalus",14,'bold'),fg="green")
        self.userlabel.place(x=80,y=150)

        self.userentry=Entry(self.canvas,font=("calibri",14),borderwidth=5)
        self.userentry.place(x=80,y=190,width=250)

        self.passlabel=Label(self.canvas,text="PASSWORD",font=("Andalus",14,'bold'),fg="green")
        self.passlabel.place(x=80,y=250)
    
        self.passentry=Entry(self.canvas,show="*",font=("calibri",14),borderwidth=5)
        self.passentry.place(x=80,y=290,width=250)

        # Show Password Check box
        self.check_var = IntVar()  # Variable for Checkbutton's value 1/0
        self.check_pass = Checkbutton(self.canvas, text="Show Password", command=self.show_password, \
            variable=self.check_var, onvalue=1, offvalue=0)
        self.check_pass.place(x=10,y=340,width=250)

        #login button
        self.loginbutton = Button(self.root, text="LOGIN",borderwidth=5,relief=GROOVE, \
            activebackground="#0B0F08",activeforeground="white",fg="white",bg="green", \
            font=("arial",15,'bold'))
        self.loginbutton.place(x=473,y=550,width=250)

        self.root.mainloop()

    # Show Password function
    def show_password(self):
        if self.check_var.get() == 1:  # If checked
            self.passentry.configure(show="")
        else:
            self.passentry.configure(show="*")



app = LoginWindow()