from controller.controlador_data import ControladorData
from model.jutge import Jutge
from principal.gestorErrors import GestorErrors
from view.jutge_form import JutgeForm
from view.menu import Menu
from tkinter.messagebox import showinfo, showerror
from view.selector import Selector
from view.table import Table


class ControladorJutges(object):
    """Ccontrola el menu de Jutges"""

    def __init__(self):
        menu_list = ["0. Sortir",
                     "1. Alta Jutge",
                     "2. Modificar Jutge",
                     "3. Llista Jutges"]
        menu_competicio = Menu(menu_list, lambda num: self.selecciona_opcio(num))
        self._frame = menu_competicio.get_frame()

    def selecciona_opcio(self, opcio):
        if opcio == 0:
            ControladorData.switch_frame(0)
        if opcio == 1:
            JutgeForm(
                title="Alta Jutge",
                command=lambda dni, nom: self.desar_jutge(dni, nom))
        if opcio == 2:
            jutges_list = []
            for component in ControladorData.get_comp_actual().get_components():
                if isinstance(component, Jutge):
                    jutges_list.append(component.get_dni())
            Selector("Selecciona un Jutge", jutges_list, lambda dni: self.update_jutge(dni))
        if opcio == 3:
            Table("LLista de Jutges", ControladorData.get_table_jutges())

    def get_frame(self):
        return self._frame

    @staticmethod
    def desar_jutge(dni, nom):
        try:
            jutge = Jutge(nom, dni)
            if ControladorData.get_comp_actual().select_component(2, dni) == -1:
                ControladorData.get_comp_actual().get_components().append(jutge)
                showinfo("Jutges", "Jutge afegit correctament")
            else:
                showerror("Jutges", "Aquest jutge ja existeix")
        except GestorErrors as e:
            showerror("Error", e.message())

    def update_jutge(self, dni, nom=None):
        pos = ControladorData.get_comp_actual().select_component(2, dni)
        if nom is None:
            JutgeForm(title="Editar Jutge", dni=ControladorData.get_comp_actual().get_components()[pos].get_dni(),
                      nom=ControladorData.get_comp_actual().get_components()[pos].get_nom(),
                      command=lambda nou_nom, nou_dni: self.update_jutge(nou_nom, nou_dni))
            return
        ControladorData.get_comp_actual().get_components()[pos].set_dni(dni)
        ControladorData.get_comp_actual().get_components()[pos].set_nom(nom)
        showinfo("Jutges", "Jutge actualizat correctament")
