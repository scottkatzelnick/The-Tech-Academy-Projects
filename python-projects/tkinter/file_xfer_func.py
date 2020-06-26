import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
from datetime import time
from file_transfer_assignment import file_xfer_part3

b = StringVar()
e = StringVar()


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (700 / 2))
    y = int((screen_height / 2) - (500 / 2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


def close_app(self):
    if messagebox.askokcancel('Quit App', 'Do you want to quit this application?'):
        self.master.destroy()
        os._exit(0)


def relay_source():
    global source
    src = b.get()
    source = src


def relay_dest():
    global destination
    d = e.get()
    dest = d
    destination = dest


def current_milli_time():
    x = int(round(time.time() * 1000))
    return x


def move_files():
    files = os.listdir(source)
    print(files)
    for i in files:
        paths = os.path.join(source, i)
        file_birth = os.stat(paths).st_birthtime
        file_modify = os.stat(paths).st_mtime
        if (current_milli_time() / 1000) - file_birth < 86400 or (
                current_milli_time() / 1000
        ) - file_modify < 86400:
            shutil.copy2(paths, destination)
        else:
            print("\n{} already in directory".format(paths))
    return
