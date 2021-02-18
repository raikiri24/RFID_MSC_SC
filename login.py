from tkinter import*
from PIL import ImageTk, Image


root = Tk()
#cfd1ce
#para sa pag clicked ng login button
def clicked(): 
    clicked_label = Label(root).pack()

#para sa entry box (placeholder)
def click(event):
    user.config(state=NORMAL)
    user.delete(0, END)
def click1(event):
    passw.config(state=NORMAL)
    passw.delete(0, END)

#logo image

image = Image.open("msc.jpg")
image = image.resize((200, 200), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
logo = Label(image = my_img)
logo.pack(pady = 20)



# textbox for user and password
user = Entry(root, width = 30)
user.insert(0, "Username")
user.config(state = DISABLED)
user.bind("<Button-1>", click)
user.pack(pady=10)

passw = Entry(root, width = 30)
passw.insert(0, "Password" )
passw.config(state = DISABLED)
passw.bind("<Button-1>", click1)
passw.pack(pady = 10)

#login button
login = Button(root, text = "login", bg = "green",command =clicked, width = 10)
login.pack()




root.mainloop()