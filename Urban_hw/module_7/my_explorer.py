import tkinter
from tkinter import filedialog
import os


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Select",
                                          filetypes=(('текстовый файл', '.txt'),
                                                     (('Все файлы', '*'))))

    text['text'] = text['text'] + filename


window = tkinter.Tk()
window.title('my_explorer')
window.geometry('500x350')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, width=75, height=3,
                     text='File: ', background='silver', foreground='blue')
text.grid(column=1, row=1, pady=20)
button_select = tkinter.Button(window, width=10, height=1,
                               text='Select file', foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=10)
window.mainloop()