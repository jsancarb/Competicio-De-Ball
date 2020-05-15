from model.ballari import Ballari
from model.modalitat import Modalitat
from model.parelladeball import ParellaDeBall
from model.jutge import Jutge
from principal.component import Component
from principal.gestorErrors import GestorErrors


class Competicio(Component):
    """Competicio"""
    _propera_edicio = 1
    _components = []

    def __init__(self, anyo, poblacio, edicio=None):
        self._poblacio = poblacio
        self._any = anyo
        if edicio is None:
            self._edicio = self._propera_edicio
            self._propera_edicio += 1
        else:
            self._edicio = edicio

    def set_poblacio(self, poblacio):
        self._poblacio = poblacio

    def get_poblacio(self):
        return self._poblacio

    def set_edicio(self, edicio):
        self._edicio = edicio

    def get_edicio(self):
        return self._edicio

    def set_any(self, anyo):
        self._any = anyo

    def get_any(self):
        return self._any

    def set_components(self, components):
        self._components = components

    def get_components(self):
        return self._components

    @staticmethod
    def add_competicio():
        anyo = input("Any de la competició: ")
        poblacio = input("Població on es realitza la competició: ")
        return Competicio(anyo, poblacio)

    def update_component(self):
        print("Any de la competició: " + self._any)
        self._any = input("Any de la competició: ")
        print("Població on es realitza la competició: " + self._poblacio)
        self._poblacio = input("Entra la nova població: ")

    def show_component(self):
        print("Les dades de la competició edició: " + str(self._edicio))
        print("Any: " + self._any)
        print("Població " + self._poblacio)

    def select_component(self, tipus, identificacio=None):
        if identificacio is None:
            if tipus == 1:
                identificacio = input("Nif del ballari o ballarina?: ")
            elif tipus == 2:
                identificacio = input("Nif del o de la jutge?: ")
            elif tipus == 3:
                identificacio = input("Codi de la modalitat?: ")
        for i in range(len(self._components)):
            if isinstance(self._components[i], Ballari) and tipus == 1:
                if self._components[i].get_dni() is identificacio:
                    return i
            if isinstance(self._components[i], Jutge) and tipus == 2:
                if self._components[i].get_dni() is identificacio:
                    return i
            if isinstance(self._components[i], Modalitat) and tipus == 3:
                if self._components[i].get_codi() is identificacio:
                    return i
        return -1

    def add_ballari(self, ballari=None):
        if ballari is None:
            ballari = Ballari.add_ballari()
        if self.select_component(1, ballari.get_dni()) == -1:
            if ballari.get_modalitat() is None:
                self.add_codi_modalitat_ballari(ballari)
            self._components.append(ballari)
        else:
            self._components.append(ballari)
            print("\nEl ballarí o ballarina ja existeix")
            input("\nPresiona intro per continuar.....")

    def add_jutge(self, jutge=None):
        if jutge is None:
            jutge = Jutge.add_jutge()
        if self.select_component(2, jutge.get_dni()) == -1:
            self._components.append(jutge)
        else:
            self._components.append(jutge)
            print("\nEl jutge ja existeix")
            input("\nPresiona intro per continuar.....")

    def add_modalitat(self, modalitat=None):
        if modalitat is None:
            modalitat = Modalitat.add_modalitat()
        if self.select_component(3, modalitat.get_codi()) == -1:
            self._components.append(modalitat)
        else:
            self._components.append(modalitat)
            print("\nLa modalitat ja existeix")
            input("\nPresiona intro per continuar.....")

    def add_jutge_modalitat(self):
        pos_modalitat = self.select_component(3)
        if pos_modalitat >= 0:
            pos_jutge = self.select_component(2)
            if pos_jutge >= 0:
                self._components[pos_modalitat].add_jutge(self._components[pos_jutge])
            else:
                raise GestorErrors(GestorErrors.NO_EXIST_JUTGE)
        else:
            raise GestorErrors(GestorErrors.NO_EXIST_MODALITAT)

    def add_codi_modalitat_ballari(self, ballari):
        pos = self.select_component(3)
        if pos >= 0:
            ballari.set_modalitat(self._components[pos].get_codi())
        else:
            raise GestorErrors(GestorErrors.NO_EXIST_MODALITAT)

    def add_parella_modalitat(self):
        nou_ballari = None
        nova_ballarina = None
        parella_creada = False
        pos = self.select_component(3)
        if pos >= 0:
            for i in range(len(self._components)):
                if isinstance(self._components[i], Ballari):
                    mateixa_modalitat = self._components[i].get_modalitat() == self._components[pos].get_codi()
                    if mateixa_modalitat and not self._components[i].is_emparellat():
                        if self._components[i].get_sexe() == "H":
                            nou_ballari = self._components[i]
                        else:
                            nova_ballarina = self._components[i]
                        if nou_ballari is not None and nova_ballarina is not None:
                            nou_ballari.set_emparellat(True)
                            nova_ballarina.set_emparellat(True)
                            self._components[pos].add_parella(ParellaDeBall(nou_ballari, nova_ballarina))
                            parella_creada = True
            if not parella_creada:
                raise GestorErrors(GestorErrors.NO_PARELLA_BALL)
        else:
            raise GestorErrors(GestorErrors.NO_EXIST_MODALITAT)

    def add_puntuacio_parella(self):
        pos = self.select_component(3)
        if pos >= 0:
            if self._components[pos] is not None:
                for i in range(len(self._components[pos].get_components()["parelles"])):
                    print("Parella amb número d'inscripció " + str(
                        self._components[pos].get_components()["parelles"][i].get_num_inscripcio()))
                    self._components[pos].get_components()["parelles"][i].set_puntuacio(
                        input("Puntuacio de la parella: "))
            else:
                raise GestorErrors(GestorErrors.MODALITAT_SENSE_PARELLES)
        else:
            raise GestorErrors(GestorErrors.NO_EXIST_MODALITAT)
