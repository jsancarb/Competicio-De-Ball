from model.ballari import Ballari
from model.competicio import Competicio
from model.jutge import Jutge
from model.modalitat import Modalitat
from model.parelladeball import ParellaDeBall
from persistencia.proveedor_persistencia import ProveedorPersistencia
from xml.etree.ElementTree import *
from principal.gestorErrors import GestorErrors


class GestorXML(ProveedorPersistencia):
    """Persistencia XML amb ElementTree"""

    _competicio: Competicio

    def set_competicio(self, competicio):
        self._competicio = competicio

    def get_competicio(self) -> Competicio:
        return self._competicio

    def desar_competicio(self, nom_fitxer: str, competicio: Competicio):
        arrel = Element("competicio")
        arrel.set("any", competicio.get_any())
        arrel.set("edicio", str(competicio.get_edicio()))
        arrel.set("poblacio", competicio.get_poblacio())
        for comp in competicio.get_components():
            if isinstance(comp, Modalitat):
                fill = SubElement(arrel, "modalitat")
                fill.set("codi", str(comp.get_codi()))
                fill.set("nom", comp.get_nom())
                parelles = comp.get_components()["parelles"]
                jutges = comp.get_components()["jutges"]
                for par in parelles:
                    net = SubElement(fill, "parellaBall")
                    net.set("numInscripcio", str(par.get_num_inscripcio()))
                    net.set("puntuacio", str(par.get_puntuacio()))
                    ballari = par.get_ballari()
                    ballarina = par.get_ballarina()
                    renet = SubElement(net, "ballari")
                    renet.set("emparellat", "1" if ballari.is_emparellat() else "0")
                    renet.set("modalitat", str(ballari.get_modalitat()))
                    renet.set("nif", ballari.get_dni())
                    renet.set("nom", ballari.get_nom())
                    renet.set("sexe", ballari.get_sexe())
                    renet = SubElement(net, "ballarina")
                    renet.set("emparellat", "1" if ballarina.is_emparellat() else "0")
                    renet.set("modalitat", str(ballarina.get_modalitat()))
                    renet.set("nif", ballarina.get_dni())
                    renet.set("nom", ballarina.get_nom())
                    renet.set("sexe", ballarina.get_sexe())
                for jutge in jutges:
                    net = SubElement(fill, "jutge")
                    net.set("nif", jutge.get_dni())
                    net.set("nom", jutge.get_nom())
            if isinstance(comp, Jutge):
                fill = SubElement(arrel, "jutge")
                fill.set("nif", comp.get_dni())
                fill.set("nom", comp.get_nom())
            if isinstance(comp, Ballari):
                fill = SubElement(arrel, "ballari")
                fill.set("emparellat", "1" if comp.is_emparellat() else "0")
                fill.set("modalitat", str(comp.get_modalitat()))
                fill.set("nif", comp.get_dni())
                fill.set("nom", comp.get_nom())
                fill.set("sexe", comp.get_sexe())
        tree = ElementTree(arrel)
        try:
            tree.write(nom_fitxer, encoding="UTF-8", xml_declaration=True)
        except Exception as e:
            raise GestorErrors(GestorErrors.DESAR_ES, getattr(e, 'message', repr(e)))

    def carregar_comapeticio(self, nom_fitxer: str):
        try:
            tree = parse(nom_fitxer)
            arrel = tree.getroot()
            self._competicio = Competicio(arrel.attrib["any"], arrel.attrib["poblacio"], int(arrel.attrib["edicio"]))
            for fill in arrel:
                if fill.tag == "jutge":
                    jutge = Jutge(fill.attrib["nom"], fill.attrib["nif"])
                    self._competicio.add_jutge(jutge)
                if fill.tag == "ballari":
                    ballari = Ballari(fill.attrib["nom"], fill.attrib["nif"], fill.attrib["sexe"])
                    ballari.set_modalitat(fill.attrib["modalitat"])
                    ballari.set_emparellat(True if fill.attrib["emparellat"] == 1 else False)
                    self._competicio.add_ballari(ballari)
                if fill.tag == "modalitat":
                    modalitat = Modalitat(fill.attrib["codi"], fill.attrib["nom"])
                    for net in fill:
                        if net.tag == "jutge":
                            jutge = Jutge(net.attrib["nom"], net.attrib["nif"])
                            modalitat.get_components()["jutges"].append(jutge)
                        if net.tag == "parellaBall":
                            ballari = Ballari(net[0].attrib["nom"], net[0].attrib["nif"], net[0].attrib["sexe"])
                            ballarina = Ballari(net[1].attrib["nom"], net[1].attrib["nif"], net[1].attrib["sexe"])
                            ballari.set_emparellat(True)
                            ballarina.set_emparellat(True)
                            ballari.set_modalitat(net[0].attrib["modalitat"])
                            ballarina.set_modalitat(net[1].attrib["modalitat"])
                            parella = ParellaDeBall(ballari, ballarina)
                            parella.set_num_inscripcio(net.attrib["numInscripcio"])
                            parella.set_puntuacio(net.attrib["puntuacio"])
                            modalitat.add_parella(parella)
                    self._competicio.add_modalitat(modalitat)
        except IOError as e:
            raise GestorErrors(GestorErrors.CARREGA_ES, getattr(e, 'message', repr(e)))
