from tkinter import *


class Pregunta(object):
    """Dialeg per preguntar"""

    def __init__(self, title, ask, func):
        self._func = func
        self._window = Toplevel()
        self._window.title(title)
        self._resposta = StringVar()
        img = PhotoImage(file="question.png")
        frame = Frame(self._window)
        frame.pack(pady=50, padx=20)
        image_label = Label(frame, image=img)
        image_label.grid(column=0, row=0, rowspan=2, padx=20)
        Label(frame, text=ask).grid(column=1, row=0, columnspan=3)
        Entry(frame, textvariable=self._resposta).grid(column=1, row=2)
        Button(frame, text="Enviar", command=lambda: self.enviar()).grid(column=2, row=2)
        Button(frame, text="Cancelar", command=lambda: self._window.destroy()).grid(column=3, row=2)
        image_label.image = img

    def enviar(self):
        self._func(self._resposta.get())
        self._window.destroy()
