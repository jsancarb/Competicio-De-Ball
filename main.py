from controller.controlador_principal import ControladorPrincipal
from application import Application
import sys

"""Mètode per iniciar la aplicació gràfica"""


def run():
    if "-g" in sys.argv:
        ControladorPrincipal()
    elif "-c" in sys.argv:
        Application().main()
    else:
        print("\nGestio de competicions de ball"
              "\nPer iniciar mode el mode gràfic executa: main -g"
              "\nPer iniciar en mode consola executa: main -c\n")


if __name__ == '__main__':
    ControladorPrincipal()
    #run()
