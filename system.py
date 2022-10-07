import sqlite3
from tkinter import *
from PIL import ImageTk,Image
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")

        self.bg=ImageTk.PhotoImage(file="2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root,bg="#bbd0ff")
        Frame_login.place(x=70,y=80,height=400,width=500)

root=Tk()
obj=Login(root)
root.title("form to input data")
root.geometry('1199x600+100+50')
e1 = StringVar()
e2 = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()


def insert_database():
    name1 = e1.get()
    email1 = e2.get()
    gender = var.get()
    country = c.get()
    programming = var1.get()
    conn = sqlite3.connect("form.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,gender TEXT,Country TEXT,Programming TEXT)")
        cursor.execute("INSERT INTO student(Fullname,Email,gender,Country,Programming) values(?,?,?,?,?)",
                       (name1, email1, gender, country, programming))
    conn.commit()


def delete_database():
    name1 = e1.get()
    email1 = e2.get()
    gender = var.get()
    country = c.get()
    programming = var1.get()

    conn = sqlite3.connect("form.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('delete from student where Fullname=? and Email=? and gender=? and Country=? and Programming=?',
                       (name1, email1, gender, country, programming))
    conn.commit()



Label(root, text="regestration form", width=20, fg='red', font=("bold", 20)).place(x=160, y=100)
Label(root, text="fullname", width=20, font=("bold", 10)).place(x=130, y=170)
Entry(root, textvar=e1).place(x=350, y=170)
Label(root, text="email", width=20, font=("bold", 10)).place(x=130, y=230)
Entry(root, textvar=e2).place(x=350, y=220)
c
Label(root, text="gender", width=20, font=("bold", 10)).place(x=130, y=280)
Radiobutton(root, text="male", padx=3, variable=var, value=1).place(x=450, y=280)
Radiobutton(root, text="famle", padx=15, variable=var, value=2).place(x=350, y=280)
Label(root, text="country", width=20, font=("bold", 10)).place(x=130, y=330)
list1 = ["canda", "india", "UK", "yemen"]
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=18)
c.set("select the county")
droplist.place(x=350, y=330)
Label(root, text="programming", width=20, font=("bold", 10)).place(x=130, y=380)
var1 = IntVar()
Checkbutton(root, text="java", variable=var1).place(x=350, y=380)
Checkbutton(root, text="python", variable=var1).place(x=400, y=380)
Button(root, text="insert", width=20, bg='brown', fg="white", command=insert_database).place(x=150, y=430)
Button(root, text="delete", width=20, bg='brown', fg="white", command=delete_database).place(x=350, y=430)
root.mainloop()



root.mainloop()