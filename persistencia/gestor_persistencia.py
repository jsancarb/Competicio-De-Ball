from persistencia.gestor_SQLite import GestorSQLite
from persistencia.gestor_XML import GestorXML
from persistencia.gestor_serial import GestorSerial
from persistencia.proveedor_persistencia import ProveedorPersistencia


class GestorPersistencia(object):
    """Control del mètode de persistencia"""

    _gestor: ProveedorPersistencia

    def get_gestor(self):
        return self._gestor

    def desar_competicio(self, tipus, nom_fitxer, competicio):
        if tipus == "XML":
            self._gestor = GestorXML()
        elif tipus == "Serial":
            self._gestor = GestorSerial()
        elif tipus == "SQLite":
            self._gestor = GestorSQLite()
        self._gestor.desar_competicio(nom_fitxer, competicio)

    def carregar_competicio(self, tipus, nom_fitxer):
        if tipus == "XML":
            self._gestor = GestorXML()
        elif tipus == "Serial":
            self._gestor = GestorSerial()
        elif tipus == "SQLite":
            self._gestor = GestorSQLite()
        self._gestor.carregar_comapeticio(nom_fitxer)
