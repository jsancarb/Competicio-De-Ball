from tkinter import *


class Menu(object):
    """Menu adaptable segons parametres"""

    def __init__(self, buttons, func):
        self._frame = Frame()
        self._frame.grid(row=0, column=0, sticky='news')
        for i in range(len(buttons)):
            Button(self._frame,
                   text=buttons[i],
                   command=lambda i=i: func(i),
                   height=round(30 / len(buttons)),
                   width=100).pack(fill=BOTH, expand=YES)

    def get_frame(self):
        return self._frame
