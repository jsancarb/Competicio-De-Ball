from tkinter import *
from tkinter.messagebox import showwarning
from controller.controlador_competicio import ControladorCompeticio
from controller.controlador_jutges import ControladorJutges
from controller.controlador_data import ControladorData
from view.menu import Menu


class ControladorPrincipal(object):
    """Controla el menu principal"""

    _frames = []

    def __init__(self):

        # Instanciem la finestra general
        self._window = Tk()
        self._window.resizable(0, 0)
        # Instaciem el frame dels menus i el possem dintre del list de frames
        menu_list = ["0. Sortir", "1. Menú Competicions", "2. Menú Jutges"]
        menu_principal = Menu(menu_list, lambda num: self.selecciona_opcio(num))
        control_competicio = ControladorCompeticio()
        control_jutges = ControladorJutges()
        self._frames.append(menu_principal.get_frame())
        self._frames.append(control_competicio.get_frame())
        self._frames.append(control_jutges.get_frame())
        # Funcio lambda per tornar al menú principal
        ControladorData.set_switch_frame(lambda num: self.switch_frame(num))
        # Establim el frame del menu principal
        self.main_frame()
        self._window.mainloop()

    def selecciona_opcio(self, opcio):
        if opcio == 0:
            exit()
        elif opcio == 1:
            # Establim el menu de competicions i canviem el titol
            self._window.title("Menu Competicio")
            self.switch_frame(1)
        elif opcio == 2:
            # Establim el menu de jutges i canviem el titol
            if ControladorData.get_comp_actual() is None:
                showwarning("Alerta", "Primer s'ha de selecionar una competicio")
            else:
                self._window.title("Menu Jutges")
                self.switch_frame(2)

    @staticmethod
    def switch_frame(num):
        """Funcio per alternar els frames"""
        ControladorPrincipal._frames[num].tkraise()

    def main_frame(self):
        self.switch_frame(0)
        self._window.title("Menu Principal")
