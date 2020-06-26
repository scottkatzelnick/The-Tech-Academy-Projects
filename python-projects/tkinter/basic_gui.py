# The Tech Academy - Software Developer BootCamp
#
# Python: 3.8.3
#
# Author: Scott Katzelnick
#
# Purpose:
#
#         This is a basic script to learn how to use the
#         tkinter module. It will create a basic geometry
#         and represent the essential commands, classes,
#         objects, and submodules that are required to
#         create a baic GUI.


# Import tkinter and all(*) of it's modules
import tkinter
from tkinter import *


# Child Class referencing tkinter to build GUI windows(Frame)
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry("{}x{}".format(700, 400))
        self.master.title("Learning tkinter!")
        self.master.config(bg="lightgray")

        self.varfname = StringVar()
        self.varlname = StringVar()

        self.lblfname = Label(
            self.master,
            text="First Name: ",
            font=("Helvetica", 16),
            fg="black",
            bg="lightgray",
        )
        self.lblfname.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.lbllname = Label(
            self.master,
            text="Last Name: ",
            font=("Helvetica", 16),
            fg="black",
            bg="lightgray",
        )
        self.lbllname.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        self.lbldisplay = Label(
            self.master, text="", font=("Helvetica", 16), fg="black", bg="lightgray",
        )
        self.lbldisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        self.txtfname = Entry(
            self.master,
            text=self.varfname,
            font=("Helvetica", 16),
            fg="black",
            bg="white",
        )
        self.txtfname.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        self.txtlname = Entry(
            self.master,
            text=self.varlname,
            font=("Helvetica", 16),
            fg="black",
            bg="white",
        )
        self.txtlname.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        self.btnsubmit = Button(
            self.master, text="Submit", width=10, height=2, command=self.submit
        )
        self.btnsubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        self.btncancel = Button(
            self.master, text="Cancel", width=10, height=2, command=self.cancel
        )
        self.btncancel.grid(row=2, column=1, padx=(0, 100), pady=(30, 0), sticky=NE)

    def submit(self):
        fn = self.varfname.get()
        ln = self.varlname.get()
        self.lbldisplay.config(text="Hello {} {}!".format(fn, ln))

    def cancel(self):
        self.master.destroy()


# __main__ module run block
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
