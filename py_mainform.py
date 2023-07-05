# main form
import tkinter as tk
from tkinter import *
from tkinter import ttk

w = 1200
h = 650

class mainform:
    def __init__(self, master):
        # self.master = master
        # # ----------- CENTER FORM ------------- #
        # ws = self.master.winfo_screenwidth()
        # hs = self.master.winfo_screenheight()
        # x = (ws-w)/2
        # y = (hs-h)/2
        # self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # # ----------- MENU ------------- #

        # self.frame = tk.Frame(self.master)
        # self.menubar = Menu(self.frame)
        # self.products = Menu(self.menubar)
        # self.products.add_command(label="Add")
        # self.products.add_command(label="Edit")
        # self.products.add_command(label="Remove")

        # self.menubar.add_cascade(menu=self.products, label="Product")

        # self.categories = Menu(self.menubar)
        # self.categories.add_command(label="Add")
        # self.categories.add_command(label="Edit")
        # self.categories.add_command(label="Remove")

        # self.menubar.add_cascade(menu=self.categories, label="Category")

        # self.frame.pack()

        # # ------------------------------ #

        # self.master.config(menu=self.menubar, bg="#ecf0f1")
        # self.lbl = tk.Label(self.master, text='Main Form', font=('verdana',50, 'bold'), fg='#2A2C2B',bg="#ecf0f1")
        # self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)
        r = tk.Tk()
        # master = Tk()
        # Label(r, text='First Name').grid(row=0)
        # Label(r, text='Last Name').grid(row=1)
        # e1 = Entry(r)
        # e2 = Entry(r)
        # e1.grid(row=0, column=1)
        # e2.grid(row=1, column=1)
        # mainloop()

        p1 = Page1(self)


        button = tk.Button(r, text='Stop', width=25, command=p1.show)
        button.pack()
        button = tk.Button(r, text='Stop1', width=25, command=r.destroy)
        button.pack()
        button = tk.Button(r, text='Stop2', width=25, command=r.destroy)
        button.pack()
        # r.mainloop()
class Page(tk.Frame):
    def __init__(self, master):
        self.master = master
    def show(self):
        self.lift()
class Page1(Page):
   def __init__(self, master):
       self.master = master
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
