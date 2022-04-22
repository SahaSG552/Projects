import tabula
import tkinter as tk

# from tkinter import filedialog   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

file_path = askopenfilename(
    initialdir="/", title="Select a file", filetypes=[("PDF", "*.pdf")]
)

# file_path = askopenfilename()[:-4] # show an "Open" dialog box and return the path to the selected file

if file_path:
    # file_path = input("Путь к файлу"), input("Имя файла")
    # file_path = ("\\").join(file_path)
    df = tabula.read_pdf(file_path, pages="all")
    df[0].to_excel(file_path.rstrip(".pdf") + ".xlsx")
    print(file_path)
