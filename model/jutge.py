from model.integrant import *


class Jutge(Integrant):
    """Jutge"""

    def __init__(self, nom, dni):
        super().__init__(nom, dni)

    @staticmethod
    def add_jutge():
        dni = input("Dni del o de la jutge: ")
        nom = input("Nom del o de la jutge: ")
        return Jutge(nom, dni)
