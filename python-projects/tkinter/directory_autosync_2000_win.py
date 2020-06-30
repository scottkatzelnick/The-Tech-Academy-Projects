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
#   **********************************************************************************************
# **WHEN RUNNING THE PROGRAM I SETUP TWO FOLDERS, a AND b. MAKE a THE SOURCE and b THE DESTINATION**
#   **********************************************************************************************
# - These folders already have content with variable creation and modified dates to test the script.

# Imported modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
import time
import shutil
import os


# Parent class using imported Frame from tkinter to draw the program window
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Configuration of parent window
        self.master = master
        self.master.maxsize(700, 500)
        self.master.minsize(700, 500)
        self.master.title("Directory Auto-Sync 2000™")
        self.master.config(bg="#333")
        self.master.protocol("WM_DELETE_WINDOW", lambda: quit_message(self))

        # Source selector label
        self.src_lbl = Label(
            self.master,
            font=("SF Pro Text Regular", 16),
            fg="#fff",
            bg="#333",
            text="Choose Source Directory",
        )
        self.src_lbl.grid(row=0, column=0, padx=(83, 0), pady=(50, 0), sticky=NSEW)
        self.src_lbl.grid_rowconfigure(0, weight=1)

        # Source selector entry box
        spath = StringVar()
        self.src_entry = Entry(self.master, width=60, textvariable=spath)
        self.src_entry.grid(row=1, column=0, padx=(83, 0), pady=(5, 0), sticky=NSEW)
        self.src_entry.grid_rowconfigure(0, weight=3)

        # Source selector directory browser button
        self.src_btn = Button(
            self.master,
            text="Browse",
            highlightbackground="#333",
            command=lambda: src_select(self),
        )
        self.src_btn.grid(row=2, column=0, padx=(83, 0), pady=(10, 0), sticky=NSEW)
        self.src_btn.grid_rowconfigure(0, weight=1)

        # Destination selector label
        self.dest_lbl = Label(
            self.master,
            font=("SF Pro Text Regular", 16),
            fg="#fff",
            bg="#333",
            text="Choose Destination Directory",
        )
        self.dest_lbl.grid(row=3, column=0, padx=(83, 0), pady=(50, 0), sticky=NSEW)
        self.dest_lbl.grid_rowconfigure(0, weight=1)

        # Destination selector entry box
        dpath = StringVar()
        self.dest_entry = Entry(self.master, width=60, textvariable=dpath)
        self.dest_entry.grid(row=4, column=0, padx=(83, 0), pady=(5, 0), sticky=NSEW)
        self.dest_entry.grid_rowconfigure(0, weight=3)

        # Destination selector directory browser button
        self.dest_btn = Button(
            self.master,
            text="Browse",
            highlightbackground="#333",
            command=lambda: dest_select(self),
        )
        self.dest_btn.grid(row=5, column=0, padx=(83, 0), pady=(10, 0), sticky=NSEW)
        self.dest_btn.grid_rowconfigure(0, weight=1)

        # Manual Auto-Sync script button
        self.get_btn = Button(
            self.master,
            text="Move Files",
            highlightbackground="#333",
            command=lambda: get(),
        )

        # Gets current time in milliseconds for use in get() method
        def current_milli_time():
            x = int(round(time.time() * 1000))
            return x

        # Script that takes the paths from the GUI Entries and moves the appropriate files
        def get():
            source = spath.get()
            destination = dpath.get()
            files = os.listdir(source)
            for i in files:
                paths = os.path.join(source, i)
                dpaths = os.path.join(destination, i)
                file_exists = Path(dpaths)
                # file_birth = os.stat(paths).st_birthtime (Only used on mac/unix systems)
                file_modify = os.stat(paths).st_mtime
                if (current_milli_time() / 1000) - file_modify < 86400: # or (current_milli_time() / 1000) -
                    # file_birth < 86400 (Only used on mac/unix systems)
                    if i != '.DS_Store':
                        if file_exists.exists():
                            shutil.copy(paths, destination)
                            os.remove(i)
                            # print("{} was moved from\n{} to\n{} ".format(i, source, destination))
                        else:
                            shutil.move(paths, destination)
                            # print("{} was moved from\n{} to\n{} ".format(i, source, destination))
            dfiles = os.listdir(destination)
            final_dest = len(dfiles)
            messagebox.showinfo("Directory Auto-Sync 2000™", "{} files were moved successfully!".format(final_dest))

        # Placement for the Auto-Sync script button
        self.get_btn.grid(row=6, column=0, padx=(83, 0), pady=(30, 0), sticky=NSEW)
        self.get_btn.grid_rowconfigure(0, weight=1)


# Displays message to confirm closing the program
def quit_message(self):
    if messagebox.askokcancel(
        "Directory Auto-Sync 2000™",
        "Did you really want to quit Directory Auto-Sync 2000™?",
    ):
        self.master.destroy()
        os._exit(0)


# Centers main window on any screen
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (700 / 2))
    y = int((screen_height / 2) - (500 / 2))
    center_win = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return center_win


# Opens a file browser dialog so user can select directory for the source
def src_select(self):
    dir_path = filedialog.askdirectory()
    d = dir_path + "/"
    self.src_entry.insert(END, d)
    return


# Opens a file browser dialog so user can select directory for the destination
def dest_select(self):
    dir_path = filedialog.askdirectory()
    d = dir_path + "/"
    self.dest_entry.insert(END, d)
    return


# Runs main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    center_window(app, 700, 500)
    app.mainloop()
