from controller.controlador_data import ControladorData
from model.competicio import Competicio
from persistencia.gestor_persistencia import GestorPersistencia
from principal.gestorErrors import GestorErrors
from view.competicio_form import CompeticioForm
from view.menu import Menu
from tkinter.messagebox import *
from view.pregunta import Pregunta
from view.selector import Selector
from view.table import Table


class ControladorCompeticio(object):
    """Controla el menu competició"""

    def __init__(self):
        """Constructor del marc"""
        menu_list = ["0. Sortir",
                     "1. Alta Competició",
                     "2. Seleccionar Competició",
                     "3. Modificar Competició",
                     "4. LListar Competicions",
                     "5. Carregar Competicio",
                     "6. Desar Competicio"]
        menu_competicio = Menu(menu_list, lambda num: self.selecciona_opcio(num))
        self._frame = menu_competicio.get_frame()

    def selecciona_opcio(self, opcio):
        """Selector d'opcions del menu"""
        if opcio == 0:
            ControladorData.switch_frame(0)
        if opcio == 1:
            if ControladorData.get_pos_competicio() < ControladorData.MAXCOMPETICIONS:
                CompeticioForm(
                    title="Alta competicio",
                    command=lambda anyo, poblacio: self.desar_competicio(anyo, poblacio))
            else:
                showwarning("Alerta", "Número màxim de competicións assolit")
        if opcio == 2:
            if len(ControladorData.get_competicions()) == 0:
                showwarning("Alerta", "Primer s'ha de donar d'alta una competicio")
            else:
                comp_list = []
                for i in range(len(ControladorData.get_competicions())):
                    comp_list.append(str(i + 1))
                Selector("Seleciona Competicio", comp_list, lambda num: self.select_competicio(num))
        if opcio == 3:
            if ControladorData.get_comp_actual() is None:
                showwarning("Alerta", "Primer s'ha de selecionar una competicio")
            else:
                CompeticioForm(
                    title="Modificar competicio",
                    command=lambda anyo, poblacio: self.update_competicio(anyo, poblacio),
                    edicio=ControladorData.get_comp_actual().get_edicio(),
                    any=ControladorData.get_comp_actual().get_any(),
                    poblacio=ControladorData.get_comp_actual().get_poblacio())
        if opcio == 4:
            if len(ControladorData.get_competicions()) == 0:
                showwarning("Alerta", "Primer s'ha de donar d'alta una competicio")
            else:
                Table("Competicions", ControladorData.get_table_competicions())
        if opcio == 5:
            Selector("Seleciona mètode de persistencia",
                     ControladorData.METODES_PERSISTENCIA,
                     lambda num: self.carregar_persistencia(num))
        if opcio == 6:
            if ControladorData.get_comp_actual() is None:
                showwarning("Alerta", "Primer s'ha de selecionar una competicio")
            else:
                Selector("Seleciona mètode de persistencia",
                         ControladorData.METODES_PERSISTENCIA,
                         lambda num: self.desar_persistencia(num))

    def get_frame(self):
        return self._frame

    @staticmethod
    def desar_competicio(anyo, poblacio):
        competicio = Competicio(anyo, poblacio)
        ControladorData.get_competicions().append(competicio)
        ControladorData.add_pos_competicio()
        showinfo("Info", "Competició desada")

    @staticmethod
    def select_competicio(num):
        ControladorData.set_competicio_actual(ControladorData.get_competicions()[int(num) - 1])
        showinfo("Info", "Competició amb número d'edicio: "
                 + str(ControladorData.get_comp_actual().get_edicio()) + " selecionada")

    @staticmethod
    def update_competicio(anyo, pobalcio):
        ControladorData.get_comp_actual().set_any(anyo)
        ControladorData.get_comp_actual().set_poblacio(pobalcio)
        showinfo("Info", "Competició actualizada")

    def carregar_persistencia(self, tipus, edicio=None):
        if edicio is None:
            Pregunta("Edicio",
                     "Quina és la edició de la competicio que vols carregar?",
                     lambda edicio_carregar: self.carregar_persistencia(tipus, edicio_carregar))
            return
        try:
            gestor = GestorPersistencia()
            if tipus == "XML":
                gestor.carregar_competicio("XML", edicio + ".xml")
            elif tipus == "Serial":
                gestor.carregar_competicio("Serial", edicio + ".dat")
            elif tipus == "SQLite":
                gestor.carregar_competicio("SQLite", edicio)
            pos = self.comprovar_competicio(gestor.get_gestor().get_competicio())
            if pos == -1:
                ControladorData.get_competicions().append(gestor.get_gestor().get_competicio())
                showinfo("Correcte", "Competicio carregada")
            else:
                ask = askyesno("Sobrescriure", "La competicio ja existeix, la vol sobrescriure?")
                if ask == YES:
                    ControladorData.get_competicions().insert(pos, gestor.get_gestor().get_competicio())
                    showinfo("Correcte", "Competicio carregada")
        except GestorErrors as e:
            showerror("Error", e.message())

    @staticmethod
    def desar_persistencia(tipus):
        gestor = GestorPersistencia()
        try:
            if tipus == "XML":
                gestor.desar_competicio("XML", str(ControladorData.get_comp_actual().get_edicio()) + ".xml",
                                        ControladorData.get_comp_actual())
            elif tipus == "Serial":
                gestor.desar_competicio("Serial", str(ControladorData.get_comp_actual().get_edicio()) + ".dat",
                                        ControladorData.get_comp_actual())
            elif tipus == "SQLite":
                gestor.desar_competicio("SQLite", str(ControladorData.get_comp_actual().get_edicio()),
                                        ControladorData.get_comp_actual())
            showinfo("Correcte", "Competició desada")
        except GestorErrors as e:
            showerror("Error", e.message())

    @staticmethod
    def comprovar_competicio(competicio):
        for i in range(len(ControladorData.get_competicions())):
            if ControladorData.get_competicions()[i].get_edicio() == competicio.get_edicio():
                return i
        return -1
