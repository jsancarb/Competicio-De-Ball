from tkinter import *


class JutgeForm(object):
    """Formulari per gestionar Jutges"""

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._dni = StringVar()
        self._nom = StringVar()
        self._window = Toplevel()
        title = "title"
        if 'title' in self._kwargs:
            title = self._kwargs["title"]
        self._window.title(title)
        self._window.geometry('300x200')
        frame = Frame(self._window)
        frame.pack(side="top", fill="x")
        Label(frame, text="DNI").pack(side="top", fill="x")
        if 'dni' in self._kwargs:
            self._dni.set(self._kwargs['dni'])
        Entry(frame, textvariable=self._dni).pack(side="top", fill="x")
        Label(frame, text="Nom").pack(side="top", fill="x")
        if 'nom' in self._kwargs:
            self._nom.set(self._kwargs['nom'])
        Entry(frame, textvariable=self._nom).pack(side="top", fill="x")
        Button(frame, text="Desar", command=lambda: self.enviar()).pack(side="top", fill="x")
        Button(frame, text="Sortir", command=lambda: self._window.destroy()).pack(side="top", fill="x")

    def enviar(self):
        self._kwargs['command'](self._dni.get(), self._nom.get())
        self._window.destroy()
