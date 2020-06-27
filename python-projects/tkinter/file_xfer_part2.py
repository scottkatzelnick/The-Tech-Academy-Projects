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
# FILE TRANSFER ASSIGNMENT PART TWO
# But now your company's users create or edit a collection of text files throughout the day. These text files represent
# data about customer orders.
#
# Once per day, any files that are new, or that were edited within the previous 24 hours, must be sent to the home
# office. To facilitate this, these new or updated files need to be copied to a specific 'destination' folder on a
# computer so that a special file transfer program can grab them and transfer them to the home office.
#
# The process of figuring out which files are new or recently edited (and copying them to the 'destination' folder), is
# currently being done manually. This is very expensive in terms of manpower.
#
# 1. Create two folders: one to hold the files that get created or modified throughout the day, and another to receive
# the folders that your script determines should be copied over daily.
#
# 2. To aid in your development efforts, you should create .txt files to add to the first folder, using Notepad or a
# similar program. You should also copy some older text files in there if you'd like. You should use files that you can
# edit so that you can control whether or not they are meant to be detected as 'modified in the last 24 hours' by your
# program.
#
# 3. Create a script that will automate this task.

# Import the required modules
import os
import time
import shutil

# Indicate source and destination directories and initialize them into variables
source = '/Users/Scott/Documents/the-tech-academy/python-projects/tkinter/daily/'
destination = "/Users/Scott/Documents/Projects/The Tech Academy/python projects/learn_python/Archive/"


# Create a method to get current time in milliseconds (Unix Time)
def current_milli_time():
    x = int(round(time.time() * 1000))
    return x


# Create a list of all files and join them into their full paths.
# Then pick out the files either created or modified within the
# past 24 hrs. (86,400 s) to be moved to the destination directory.
def move_recent():
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


# Run specified method
if __name__ == "__main__":
    move_recent()
