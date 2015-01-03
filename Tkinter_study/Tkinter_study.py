__author__ = 'Administrator'

from tkinter import *
from datetime import *
import urllib

from urllib.parse import *


def abc():
    aa = urllib.parse.unquote(ourl.get())
    text.delete(0.0, END)
    text.insert(INSERT, aa)


def cba():
    aa = urllib.parse.quote(ourl.get())
    text.delete(0.0, END)
    text.insert(INSERT, aa)


def selectAll(char):
    text.tag_add("sel", "1.0", "end")
    return 'break'

root = Tk()
root.title(datetime.now())
root.resizable(False, False)
ourl = StringVar()


originalURL = Label(root, text='Before:', fg='red', bg='blue').grid(row=0, sticky=W)
afterURL = Label(root, text='After:', fg='red', bg='blue').grid(row=1, sticky=W)

oURL = Entry(root, width=60, textvariable=ourl)
oURL.grid(row=0, column=1, sticky=W)
oURL.focus_set()

text = Text(root, width=60, height=5)
text.grid(row=1, column=1)
text.bind("<Control-Key-a>", selectAll)

mButton = Button(root, text='Decode', command=abc).grid(row=3, column=3)
nButton = Button(root, text='Encode', command=cba).grid(row=3, column=0)

root.mainloop()