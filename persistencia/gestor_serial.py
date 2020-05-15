import pickle
from model.ballari import Ballari
from model.competicio import Competicio
from model.jutge import Jutge
from model.modalitat import Modalitat
from persistencia.proveedor_persistencia import ProveedorPersistencia
from principal.gestorErrors import GestorErrors


class GestorSerial(ProveedorPersistencia):
    """Persistencia serial amb pickle"""

    _competicio: Competicio

    def set_competicio(self, competicio):
        self._competicio = competicio

    def get_competicio(self) -> Competicio:
        return self._competicio

    def desar_competicio(self, nom_fitxer: str, competicio: Competicio):
        try:
            with open(nom_fitxer, "wb") as file:
                pickle.dump(competicio, file, pickle.HIGHEST_PROTOCOL)
                for comp in competicio.get_components():
                    pickle.dump(comp, file, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            raise GestorErrors(GestorErrors.DESAR_ES, getattr(e, 'message', repr(e)))
        finally:
            file.close()

    def carregar_comapeticio(self, nom_fitxer: str):
        file = None
        try:
            file = open(nom_fitxer, "rb")
            self._competicio = pickle.load(file)
            while True:
                comp = pickle.load(file)
                if isinstance(comp, Ballari):
                    self._competicio.add_ballari(comp)
                if isinstance(comp, Jutge):
                    self._competicio.add_jutge(comp)
                if isinstance(comp, Modalitat):
                    self._competicio.add_modalitat(comp)
        except Exception as e:
            raise GestorErrors(GestorErrors.CARREGA_ES, getattr(e, 'message', repr(e)))
        finally:
            if file is not None:
                file.close()
