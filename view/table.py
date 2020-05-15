from tkinter import *
from tkinter.ttk import *


class Table(object):
    """Taula grafica adaptable"""

    def __init__(self, title="", table=None):
        if table is None:
            table = []
        window = Toplevel()
        window.title(title)
        frame = Frame(window)
        frame.pack(side="top", fill="x")
        # show headings elimina la primera columna
        if len(table) > 0:
            tree = Treeview(frame, columns=table[0], show='headings')
            tree.pack(side="top", fill="x")
            for i in range(len(table[0])):
                # ancho N per centrar contigut
                tree.column(table[0][i], ancho=N)
                tree.heading(table[0][i], text=table[0][i])
            for i in range(1, len(table)):
                tree.insert("", END, values=table[i])
