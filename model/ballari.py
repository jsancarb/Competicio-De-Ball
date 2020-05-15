from model.integrant import *


class Ballari(Integrant):
    """Ballari"""

    def __init__(self, _nom, _dni, _sexe):
        super().__init__(_nom, _dni)
        self._sexe = _sexe
        self._modalitat = None
        self._emparellat = False

    def set_sexe(self, _sexe):
        self._sexe = _sexe

    def get_sexe(self):
        return self._sexe

    def set_modalitat(self, _modalitat):
        self._modalitat = _modalitat

    def get_modalitat(self):
        return self._modalitat

    def set_emparellat(self, emparellat):
        self._emparellat = emparellat

    def is_emparellat(self):
        return self._emparellat

    @staticmethod
    def add_ballari():
        dni = input("NIF del ballarí o ballarina: ")
        nom = input("Nom del ballarí o ballarina: ")
        sexe = input("Sexe del ballarí o ballarina: Dona (D) - Home (H): ")
        return Ballari(nom, dni, sexe)

    def update_component(self):
        super().update_component()
        if self._sexe == "H":
            print("És un ballari")
        else:
            print("És una ballarina")
        self._sexe = input(
            "Entra el sexe del ballarí o ballarina: Dona (D) - Home (H):")
        if self._emparellat:
            print("Té parella")
        else:
            print("No te parella")
        emparellat = input("Està emparellat o emparellada?: Si (1) - No (0): ")
        if emparellat == 0:
            self.set_emparellat(False)
        else:
            self.set_emparellat(True)

    def show_component(self):
        super().show_component()
        if self._sexe == "H":
            print("És un ballari")
        else:
            print("És una ballarina")
        if self._emparellat:
            print("Té parella")
        else:
            print("No te parella")
        if self._modalitat is None:
            modalitat = ""
        else:
            modalitat = self._modalitat
        print("El codi de la seva modalitat és: " + modalitat)
