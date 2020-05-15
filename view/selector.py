from tkinter import *


class Selector(object):
    """Selector adaptable amb butons"""

    def __init__(self, title, select_list, func):
        self._func = func
        self._window = Toplevel()
        self._window.title(title)
        self._window.minsize(width=250, height=100)
        frame = Frame(self._window)
        frame.pack(expand="yes", padx="40")
        for i in range(len(select_list)):
            Button(frame,
                   text=select_list[i],
                   command=lambda i=i: self.enviar(select_list[i])
                   ).pack(side="left", fill="x")
        self._window.mainloop()

    def enviar(self, element):
        self._func(element)
        self._window.destroy()




