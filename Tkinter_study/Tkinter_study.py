__author__ = 'Administrator'

from tkinter import *
from tkinter import ttk
import urllib

from urllib.parse import *


#
# def timez():
#     t = 1
#     while t != 0:
#         t = time.ctime()
#         root.title(str(t))
#         root.update()
#         time.sleep(1)

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
root.title('URL Code Transformation')
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

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

mButton = ttk.Button(root, text='Decode', command=abc, style='C.TButton').grid(row=3, column=3)
nButton = ttk.Button(root, text='Encode', command=cba, style='C.TButton').grid(row=4, column=3)

root.mainloop()