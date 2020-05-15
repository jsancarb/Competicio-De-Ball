from model.competicio import Competicio


class ProveedorPersistencia(object):
    """Interface dels gestors de persistencia"""

    def set_competicio(self, competicio):
        pass

    def get_competicio(self) -> Competicio:
        pass

    def desar_competicio(self, nom_fitxer: str, competicio: Competicio): 
        pass

    def carregar_comapeticio(self, nom_fitxer: str):
        pass
