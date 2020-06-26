# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Formatter: Black v19.10b0
#
# Author: Scott Katzelnick
#
# Purpose:
#
# FILE TRANSFER ASSIGNMENT PART THREE
# Users are now asking for a user interface to make using the script easier and more versatile.
#
# Desired features of the UI:
#
# Allow the user to browse and choose a specific folder that will contain the files to be checked daily.
#
# Allow the user to browse and choose a specific folder that will receive the copied files.
#
# Allow the user to manually initiate the 'file check' process that is performed by the script.
#
# You have been asked to create this UI.
#
# Once you have completed this assignment, upload your code to Github

# Import required modules
from datetime import time
from tkinter import *
import tkinter as tk
import os
import shutil
from tkinter import filedialog
import file_xfer_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.maxsize(700, 500)
        self.master.minsize(700, 500)
        file_xfer_func.center_window(self, 700, 400)
        self.master.title("Directory Auto-Sync®")
        self.master.config(bg="#333")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_xfer_func.close_app(self))
        arg = self.master

        self.get_lbl = tk.Label(
            self.master,
            font=("Helvetica", 16),
            fg="#fff",
            bg="#333",
            text="Choose Source Directory",
        )
        self.get_lbl.grid(row=0, column=0, padx=(190, 0), pady=(50, 0))

        def select_dir():
            dir_path = filedialog.askdirectory()
            x = dir_path + "/"
            self.lst_dir.insert(END, x)

        self.lst_dir = tk.Entry(self.master, width=40, textvariable=file_xfer_func.b)
        self.lst_dir.grid(row=1, column=0, padx=(180, 0), pady=(5, 0))

        self.relay_btn = tk.Button(
            self.master,
            highlightbackground="#333",
            text="Submit",
            command=file_xfer_func.relay_source(),
        )
        self.relay_btn.grid(row=2, column=0, padx=(290, 0), pady=(10, 0))

        self.get_btn = tk.Button(
            self.master, highlightbackground="#333", text="Browse", command=select_dir
        )
        self.get_btn.grid(row=2, column=0, padx=(90, 0), pady=(10, 0))

        self.give_lbl = tk.Label(
            self.master,
            font=("Helvetica", 16),
            fg="#fff",
            bg="#333",
            text="Choose Destination Directory",
        )
        self.give_lbl.grid(row=3, column=0, padx=(190, 0), pady=(40, 0))

        def dest_dir():
            dir_path = filedialog.askdirectory()
            x = dir_path + "/"
            self.lst_dir_give.insert(END, x)

        self.lst_dir_give = tk.Entry(
            self.master, width=40, textvariable=file_xfer_func.e
        )
        self.lst_dir_give.grid(row=4, column=0, padx=(180, 0), pady=(5, 0))

        self.relay_btn_give = tk.Button(
            self.master,
            highlightbackground="#333",
            text="Submit",
            command=file_xfer_func.relay_dest(),
        )
        self.relay_btn_give.grid(row=5, column=0, padx=(290, 0), pady=(10, 0))

        self.give_btn = tk.Button(
            self.master, highlightbackground="#333", text="Browse", command=dest_dir
        )
        self.give_btn.grid(row=5, column=0, padx=(90, 0), pady=(10, 0))

        source = ""
        destination = ""
        self.move_btn = tk.Button(
            self.master,
            highlightbackground="#333",
            text="Move Files",
            command=file_xfer_func.move_files(),
        )
        self.move_btn.grid(row=6, column=0, padx=(200, 0), pady=(40, 0))


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
