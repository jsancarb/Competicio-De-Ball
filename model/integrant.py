from principal.component import *


class Integrant(Component):
    """Integrant"""

    def __init__(self, nom, dni):
        self._nom = nom
        self._dni = dni

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    def update_component(self):
        print("NIF de l'integrant: " + self._dni)
        self._dni = input("Entra el nou dni:")
        print("Nom de l'intregrant: " + self._nom)
        self._nom = input("Entra el nou nom: ")

    def show_component(self):
        print("Les dades de l'integrant amb nif " + self._dni + " són: ")
        print("Nom: " + self._nom)
