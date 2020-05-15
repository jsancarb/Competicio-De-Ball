from model.competicio import *
from persistencia.gestor_persistencia import GestorPersistencia
from model.competicio import Competicio
from os import system, name


class Application(object):
    """Classe per controlar la aplicació per consola"""
    competicio_actual: Competicio = None
    competicions = []
    posicio_competicions = 0

    FITXER = "competicio"

    def main(self):
        while True:
            self.clear()
            print("Selecciona una opció:\n")
            print("0. Sortir")
            print("1. Gestió de competicions")
            print("2. Gestió de modalitats")
            print("3. Gestió de ballarins o ballarines")
            print("4. Gestió de jutges")
            opcio = input()
            if opcio == "0":
                exit()
            elif opcio == "1":
                self.menu_competicions()
            elif opcio == "2":
                if self.competicio_actual is not None:
                    self.menu_components(3)
                else:
                    print("\nPrimer s'ha de seleccionar la competició al menú Gestió de competicions\n")
                    input("\nPresiona intro per continuar.....")
            elif opcio == "3":
                if self.competicio_actual is not None:
                    self.menu_components(1)
                else:
                    print("\nPrimer s'ha de seleccionar la competició al menú Gestió de competicions\n")
                    input("\nPresiona intro per continuar.....")
            elif opcio == "4":
                if self.competicio_actual is not None:
                    self.menu_components(2)
                else:
                    print("\nPrimer s'ha de seleccionar la competició al menú Gestió de competicions\n")
                    input("\nPresiona intro per continuar.....")
            else:
                print("\nS'ha de seleccionar una opció correcta del menú.\n")
                input("\nPresiona intro per continuar.....")
    def menu_competicions(self):
        while True:
            self.clear()
            print("Selecciona una opció:\n")
            print("0. Sortir")
            print("1. Crear nova competició")
            print("2. Seleccionar competició")
            print("3. Modificar competició")
            print("4. Llista de competicions")
            print("5. Carregar competició")
            print("6. Desar competició")
            opcio = input()
            if opcio == "0":
                return
            elif opcio == "1":
                self.competicions.append(Competicio.add_competicio())
                self.posicio_competicions += 1
            elif opcio == "2":
                index_sel = self.select_competicio()
                if index_sel >= 0:
                    self.competicio_actual = self.competicions[index_sel]
                else:
                    print("\nNo existeix aquesta competicio\n")
                    input("\nPresiona intro per continuar.....")
            elif opcio == "3":
                index_sel = self.select_competicio()
                if index_sel >= 0:
                    self.competicions[index_sel].update_component()
                else:
                    print("\nNo existeix aquesta competicio\n")
                    input("\nPresiona intro per continuar.....")
            elif opcio == "4":
                for competicio in self.competicions:
                    competicio.show_component()
                input("\nPresiona intro per continuar.....")
            elif opcio == "5":
                gestor = GestorPersistencia()
                tipus = input("\nQuin mètode vols utilitzar 1.-XML 2.-Serial:")
                if tipus == "1":
                    gestor.carregar_competicio("XML", self.FITXER + ".xml")
                elif tipus == "2":
                    gestor.carregar_competicio("Serial", self.FITXER + ".dat")
                else:
                    print("\nOpció no vàlida")
                self.competicions.append(gestor.get_gestor().get_competicio())
            elif opcio == "6":
                if self.competicio_actual is not None:
                    gestor = GestorPersistencia()
                    tipus = input("\nQuin mètode vols utilitzar 1.-XML 2.-Serial:")
                    if tipus == "1":
                        gestor.desar_competicio("XML", self.FITXER + ".xml", self.competicio_actual)
                    elif tipus == "2":
                        gestor.desar_competicio("Serial", self.FITXER + ".dat", self.competicio_actual)
                    else:
                        print("\nOpció no vàlida")
                        input("\nPresiona intro per continuar.....")
                else:
                    print("\nPrimer s'ha de seleccionar la competició al menú Gestió de competicions\n")
                    input("\nPresiona intro per continuar.....")
            else:
                print("\nS'ha de seleccionar una opció correcta del menú.")
                input("\nPresiona intro per continuar.....")

    def menu_components(self, tipus):
        while True:
            self.clear()
            print("Selecciona una opció:\n")
            print("0. Sortir")
            print("1. Alta")
            print("2. Modificar")
            print("3. Llistar")
            if tipus == 3:
                print("4. Assignar jutge")
                print("5. Assignar parella de ball")
                print("6. Assignar puntuació a les parelles de ball")
            opcio = input()
            if opcio == "0":
                return
            elif opcio == "1":
                if tipus == 1:
                    self.competicio_actual.add_ballari()
                if tipus == 2:
                    self.competicio_actual.add_jutge()
                if tipus == 3:
                    self.competicio_actual.add_modalitat()
            elif opcio == "2":
                index_sel = self.competicio_actual.select_component(tipus)
                if index_sel >= 0:
                    self.competicio_actual.get_components()[
                        index_sel].update_component()
                else:
                    print("\nNo existeix aquest component")
                    input("\nPresiona intro per continuar.....")
            elif opcio == "3":
                for component in self.competicio_actual.get_components():
                    if isinstance(component, Ballari) and tipus == 1:
                        component.show_component()
                    if isinstance(component, Jutge) and tipus == 2:
                        component.show_component()
                    if isinstance(component, Modalitat) and tipus == 3:
                        component.show_component()
                input("\nPresiona intro per continuar.....")
            elif opcio == "4":
                self.competicio_actual.add_jutge_modalitat()
            elif opcio == "5":
                self.competicio_actual.add_parella_modalitat()
            elif opcio == "6":
                self.competicio_actual.add_puntuacio_parella()
            else:
                print("\nS'ha de seleccionar una opció correcta del menú.")
                input("\nPresiona intro per continuar.....")

    def select_competicio(self):
        edicio = input("\nEdició de la competició?:")
        for i in range(len(self.competicions)):
            if str(self.competicions[i].get_edicio()) == edicio:
                return i
        return -1

    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
