from model.jutge import Jutge


class ControladorData(object):
    """Controla les dades de la competició"""
    _competicions = []
    _pos_competicio = 0
    _comp_actual = None
    _switch_frame = None
    MAXCOMPETICIONS = 4
    METODES_PERSISTENCIA = ["XML", "Serial", "SQLite"]

    @staticmethod
    def get_competicions():
        return ControladorData._competicions

    @staticmethod
    def set_switch_frame(func):
        ControladorData._switch_frame = func

    @staticmethod
    def switch_frame(num):
        ControladorData._switch_frame(num)

    @staticmethod
    def set_competicio_actual(competicio):
        ControladorData._comp_actual = competicio

    @staticmethod
    def get_comp_actual():
        return ControladorData._comp_actual

    @staticmethod
    def add_pos_competicio():
        ControladorData._pos_competicio += 1

    @staticmethod
    def get_pos_competicio():
        return ControladorData._pos_competicio

    @staticmethod
    def get_table_competicions():
        tabla = []
        row = []
        tabla.append(["Edicio", "Any", "Poblacio"])
        for comp in ControladorData._competicions:
            row.append(comp.get_edicio())
            row.append(comp.get_any())
            row.append(comp.get_poblacio())
            tabla.append(row)
        return tabla

    @staticmethod
    def get_table_jutges():
        tabla = []
        row = []
        tabla.append(["DNI", "Nom"])
        for component in ControladorData._comp_actual.get_components():
            if isinstance(component, Jutge):
                row.append(component.get_dni())
                row.append(component.get_nom())
                tabla.append(row)
        return tabla
