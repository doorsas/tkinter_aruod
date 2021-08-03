from tkinter import *
import tkinter as tk
from tkinter import ttk



class App(Tk):
    def __init__(self):
        self.window = Tk()
        self.window.title ("BMI")

        self.label = Label(self.window, text="Enter your wight (kg) ").pack()
        self.kg= StringVar()
        Entry(self.window, textvariable=self.kg).pack()


        self.label = Label (self.window, text="Enter your hight (m)").pack ()
        self.m= StringVar ()
        Entry (self.window, textvariable=self.m).pack ()

        self.label = Label (self.window, text="Enter your Gender ").pack ()
        self.g= StringVar ()


        usertype = tk.StringVar()
        self.combo = ttk.Combobox(self.window,state='readonly',values=
        ['male','Female','child']).pack()
        self.gender = StringVar()

        self.age = StringVar ()
        self.label = Label (self.window, text="Enter your age ").pack ()
        self.spin=Spinbox(self.window, from_=0, to=100).pack ()


        self.buttontext = StringVar()
        Button(self.window, textvariable=self.buttontext,
        command=self.calculate).pack()
        self.buttontext.set("Calculate")


        self.bmi_num = StringVar()
        Label(self.window, textvariable=self.bmi_num).pack()

        self.bmi_text = StringVar()
        Label(self.window, textvariable=self.bmi_text).pack()


        self.window.mainloop()

    def calculate(self):

        weight=(self.kg.get())
        weight=float(weight)
        hight=(self.m.get())
        hight=float(hight)
        Gender=(self.g.get())
        age=(self.age.get())
        bmi=float((weight)/float(hight**2))
        self.bmi_num.set("Your BMI is %.2f" % bmi)
        if self.g.get()=="Man":
            if bmi < 18.5:
                self.bmi_text.set ("You are underweight")
            if 18.5 <= bmi < 25:
                self.bmi_text.set ("You are normal")
            if 25 <= bmi < 30:
                self.bmi_text.set ("You are overweight")
            if 30 <= bmi > 30:
                self.bmi_text.set ("You are obese")



App()