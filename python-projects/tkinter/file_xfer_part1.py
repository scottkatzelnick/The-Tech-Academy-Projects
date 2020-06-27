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
# FILE TRANSFER ASSIGNMENT PART ONE
# NOTE: This is a three-part assignment. Ensure to save all your code files for this assignment because you will be
# uploading them to GitHub for review by an Instructor.
#
# Your employer wants a program to move all their text files (with a .txt file extension) from one folder to another
# with the click of a button. On your desktop you will have two new folders, one called Folder A and another called
# Folder B. You will need to move text files from Folder A to Folder B.


# Import necessary modules
import shutil
import os

# Set file path for source
source = "/Users/Scott/Documents/the-tech-academy/python-projects/basic-python/a"

# Set the destination path & create list of all files in source to be moved to destination
destination = "/Users/Scott/Documents/the-tech-academy/python-projects/basic-python/b"
files = os.listdir(source)
for i in files:
    fpath = str(source + '/')
    shutil.move(fpath + i, destination)
