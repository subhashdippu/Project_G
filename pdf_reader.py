import PyPDF2 # pip install 'PyPDF2<3.0'
import pyttsx3
import tkinter
from tkinter import filedialog
import os
root = tkinter.Tk()
import time
import math
import sys
import os
import subprocess
# import matplotlib.pyplot as plt
root.withdraw()  # use to hide tkinter window

def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(
        initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir
file_path_variable = search_for_file_path()
with open('movie_path.txt', 'w') as f:
    b = f.write(file_path_variable)
with open('movie_path.txt', 'r') as f:
    b = f.read()
book = open(b, 'rb')
os.system(f'open {b}')
pdfReader = PyPDF2.PdfFileReader(book) # This is going to read the book 
pages = pdfReader.numPages # This will find the no: of pages present in book
print(pages)
speaker = pyttsx3.init()
# speaker("Enter the page number which youy want to read")
num1 = int(input("Enter the page number which youy want to read "))
for num in range(num1, pages):
	# hour = int(proj1.takeCommand())
    page = pdfReader.getPage(num1) # This will read the page no: 8
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait() 
    speaker.runAndWait()