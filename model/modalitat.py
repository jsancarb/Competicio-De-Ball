from principal.component import *
from principal.gestorErrors import *


class Modalitat(Component):
    """Modalitat"""

    def __init__(self, _codi, _nom):
        self._codi = _codi
        self._nom = _nom
        self._components = {"jutges": [], "parelles": []}
        self._num_inscripcio = 0
        self._proxim_num_inscripcio = 1

    def get_codi(self):
        return self._codi

    def set_codi(self, _codi):
        self._codi = _codi

    def get_nom(self):
        return self._nom

    def set_nom(self, _nom):
        self._nom = _nom

    def get_components(self):
        return self._components

    def set_components(self, _components):
        self._components = _components

    @staticmethod
    def add_modalitat():
        codi = input("Codi de la modalitat: ")
        nom = input("Nom de la modalitat: ")
        return Modalitat(codi, nom)

    def update_component(self):
        print("Codi de la modalitat: " + self._codi)
        self._codi = input("Entra el nou codi: ")
        print("Nom de la modalitat: ")
        self._nom = input("Entra el nou nom: ")

    def add_parella(self, parella):
        self._num_inscripcio = self._proxim_num_inscripcio
        parella.set_num_inscripcio(self._num_inscripcio)
        self._proxim_num_inscripcio += 1
        self._components["parelles"].append(parella)

    def add_jutge(self, jutge):
        if len(self._components["jutges"]) < 3:
            self._components["jutges"].append(jutge)
            print(str(len(self._components["jutges"])) + " jutges assignats")
        elif len(self._components["jutges"]) > 7:
            raise GestorErrors(GestorErrors.MAX_JUTGES)
        else:
            self._components["jutges"].append(jutge)

    def show_component(self):
        print("Les dades de la modalitat amb codi: " + self._codi)
        print("Nom: " + self._nom)
        if len(self._components["parelles"]) == 0:
            print("No hi ha parelle inscrita.")
        else:
            for parella in self._components["parelles"]:
                parella.show_parelladeball()
        if len(self._components["jutges"]) == 0:
            print("No hi ha cap jutge assignat.")
        else:
            for jutge in self._components["jutges"]:
                jutge.show_component()
