from tkinter import *


class CompeticioForm(object):
    """Formulari per gestionar Competicions"""

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        edicio = StringVar()
        self._anyo = StringVar()
        self._poblacio = StringVar()
        self._window = Toplevel()
        self._window.title(self._kwargs['title'])
        self._window.geometry('300x200')
        frame = Frame(self._window)
        frame.pack(side="top", fill="x")
        Label(frame, text="Edicio").pack(side="top", fill="x")
        if 'edicio' in self._kwargs:
            edicio.set(self._kwargs['edicio'])
        Entry(frame, state='readonly', textvariable=edicio).pack(side="top", fill="x")
        Label(frame, text="Any").pack(side="top", fill="x")
        if 'any' in self._kwargs:
            self._anyo.set(self._kwargs['any'])
        Entry(frame, textvariable=self._anyo).pack(side="top", fill="x")
        Label(frame, text="Poblacio").pack(side="top", fill="x")
        if 'poblacio' in self._kwargs:
            self._poblacio.set(self._kwargs['poblacio'])
        Entry(frame, textvariable=self._poblacio).pack(side="top", fill="x")
        Button(frame, text="Desar", command=lambda: self.enviar()).pack(side="top", fill="x")
        Button(frame, text="Sortir", command=lambda: self._window.destroy()).pack(side="top", fill="x")

    def enviar(self):
        self._kwargs['command'](self._anyo.get(), self._poblacio.get())
        self._window.destroy()
