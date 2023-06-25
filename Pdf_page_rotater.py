import PyPDF2
import pyttsx3
import tkinter
from tkinter import filedialog
import os
root = tkinter.Tk()
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
num = int(input("Enter the degree which you want to rotate: "))
PageNo = int(input("Enter the page no: "))
pdf_in = open(b, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum == PageNo:
        page.rotateClockwise(num)
    pdf_writer.addPage(page)
with open('Rotated.pdf', 'wb') as new_pdf:
    pdf_writer.write(new_pdf)
s = os.path.abspath("Rotated.pdf")
pdf_in.close()
print(os.path.abspath("Rotated.pdf"))
# with open('path.txt', 'w') as f:
#     a = f.write(s)
# with open('path.txt', 'r') as f:
#     a = f.read()
# os.system(f'open {s}')