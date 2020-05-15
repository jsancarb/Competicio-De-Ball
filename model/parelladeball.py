class ParellaDeBall(object):
    """Parella de Ball"""

    def __init__(self, _ballari, _ballarina):
        self._num_inscripcio = 0
        self._ballari = _ballari
        self._ballarina = _ballarina
        self._puntuacio = 0

    def get_num_inscripcio(self):
        return self._num_inscripcio

    def set_num_inscripcio(self, _num_inscripcio):
        self._num_inscripcio = _num_inscripcio

    def get_ballari(self):
        return self._ballari

    def set_ballari(self, _ballari):
        self._ballari = _ballari

    def get_ballarina(self):
        return self._ballarina

    def set_ballarina(self, _ballarina):
        self._ballarina = _ballarina

    def set_puntuacio(self, _puntuacio):
        self._puntuacio = _puntuacio

    def get_puntuacio(self):
        return self._puntuacio

    def show_parelladeball(self):
        print("Les dades de la parella de ball amb número d'inscripció " +
              str(self._num_inscripcio))
        if self._ballari is None:
            print("Encara no hi ha ballarí assignat")
        else:
            self._ballari.show_component()
        if self._ballarina is None:
            print("Encara no hi ha ballarina assignada")
        else:
            self._ballarina.show_component()
        print("Puntuació " + str(self._puntuacio))
