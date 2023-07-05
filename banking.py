import os
import tkinter as tk
from tkinter import ttk
from tkinter import ttk 
# from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
# from PIL import ImageTk, Image

#Main Screen 
master = tk.Tk()
connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='test123', database='py_lg_rg_db')
c = connection.cursor()
master.title('Wallet Payment Service')

#Functions
def finish_reg():
    print("In finish reg")
    fullname = fullname_entry_rg.get().strip() # remove white space
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    confirm_password = confirmpass_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender_entry_rg.get()

    print
    if len(fullname) > 0 and  len(username) > 0 and len(password) > 0 and len(phone) > 0:
        if check_username(username) == False: 
            if password == confirm_password:
                vals = (fullname, username, password, phone, gdr, "sample")
                insert_query = "INSERT INTO `users`(`fullname`, `username`, `password`, `phone`, `gender`, `image_path`) VALUES (%s,%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Register','your account has been created successfully')
            else:
                messagebox.showwarning('Password','incorrect password confirmation')
        else:
            messagebox.showwarning('Duplicate Username','This Username Already Exists, try another one')
    else:
        messagebox.showwarning('Empty Fields','make sure to enter all the information')


def register():
    register_screen = tk.Toplevel(master)
    register_screen.title('Register')

    #Labels
    # tk.Label(register_screen, text="Please enter below details to register", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
    # tk.Label(register_screen, text="Name", font=('Calibri',14)).grid(row=1,sticky=tk.W)
    # tk.Label(register_screen, text="Age", font=('Calibri',14)).grid(row=2,sticky=tk.W)
    # tk.Label(register_screen, text="Gender", font=('Calibri',14)).grid(row=3,sticky=tk.W)
    # tk.Label(register_screen, text="Password", font=('Calibri',14)).grid(row=4,sticky=tk.W)

    global fullname_entry_rg
    global username_entry_rg
    global password_entry_rg
    global confirmpass_entry_rg
    global phone_entry_rg
    global gender_entry_rg
    # global register_button

    fullname_label_rg = tk.Label(register_screen, text='Fullname:', font=('Verdana',14)).grid(row=0,sticky=tk.W)
    username_label_rg = tk.Label(register_screen, text='Username:', font=('Verdana',14)).grid(row=1,sticky=tk.W)
    password_label_rg = tk.Label(register_screen, text='Password:', font=('Verdana',14)).grid(row=2,sticky=tk.W)
    confirmpass_label_rg = tk.Label(register_screen, text='Re-Password:', font=('Verdana',14)).grid(row=3,sticky=tk.W)
    phone_label_rg = tk.Label(register_screen, text='Phone:', font=('Verdana',14)).grid(row=4,sticky=tk.W)
    gender_label_rg = tk.Label(register_screen, text='Gender:', font=('Verdana',14)).grid(row=5,sticky=tk.W)

    fullname_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22).grid(row=0,column=1)
    username_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22).grid(row=1,column=1)
    password_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22, show='*').grid(row=2,column=1)
    confirmpass_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22, show='*').grid(row=3,column=1)
    phone_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22).grid(row=4,column=1)
    gender_entry_rg = tk.Entry(register_screen, font=('Verdana',14), width=22).grid(row=5,column=1)
    
    register_button = tk.Button(register_screen,text="Register", font=('Verdana',16), bg='#2980b9',fg='#fff', padx=25, pady=10, width=25).grid(row=6,column=1)
    go_login_label = tk.Label(register_screen, text=">> already have an account? sign in" , font=('Verdana',10), fg='red').grid(row=7,column=1)

    register_button['command'] = finish_reg
   
    # tk.Label(master, text="Name", font=('Calibri',14)).grid(row=1,sticky=tk.W)
def login():
   print("This is a login page") 

#Labels
tk.Label(master, text="Custom Banking Beta", font=('Verdana',16)).grid(row=0,sticky=tk.N,pady=10)
tk.Label(master, text="The most secure App", font=('Verdana',16)).grid(row=1,sticky=tk.N,pady=10)

#Buttons
tk.Button(master, text="Register", font=('Calibri',12),width=20,command=register).grid(row=3,sticky=tk.N)
tk.Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=tk.N,pady=15)


# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM `users` WHERE `username` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False


master.mainloop()