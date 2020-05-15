from model.competicio import Competicio
from model.jutge import Jutge
from persistencia.proveedor_persistencia import ProveedorPersistencia
import sqlite3
from principal.gestorErrors import GestorErrors


class GestorSQLite(ProveedorPersistencia):
    """Persistencia SQL amb SQLite"""

    _competicio: Competicio
    _con = None
    _cursor = None
    EDICIO_COMPETICIO = "SELECT * FROM COMPETICIONS WHERE EDICIO = ?"
    INSERT_COMPETICIO = "INSERT INTO COMPETICIONS VALUES(?,?,?)"
    UPDATE_COMPETICIO = "UPDATE COMPETICIONS SET ANYO = ?, POBLACIO=? WHERE EDICIO = ?"
    DELETE_JUTGE = "DELETE FROM JUTGES WHERE EDICIOCOMPETICIO = ?"
    INSERT_JUTGE = "INSERT INTO JUTGES VALUES (?, ?, ?)"
    SEL_JUTGE = "SELECT * FROM JUTGES WHERE EDICIOCOMPETICIO = ?"

    def sql_connection(self):
        try:
            self._con = sqlite3.connect('competicions.db')
            self._cursor = self._con.cursor()
        except sqlite3.Error as e:
            raise GestorErrors(9, getattr(e, 'message', repr(e)))

    def create_tables(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS COMPETICIONS("
                             "EDICIO INTEGER NOT NULL,"
                             "ANYO INTEGER NOT NULL, "
                             "POBLACIO VARCHAR(120) NOT NULL, "
                             "PRIMARY KEY (EDICIO))")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS JUTGES("
                             "NIF VARCHAR(9) NOT NULL,"
                             "NOM VARCHAR(120) NOT NULL,"
                             "EDICIOCOMPETICIO INTEGER NOT NULL,"
                             "PRIMARY KEY (NIF),"
                             "FOREIGN KEY (EDICIOCOMPETICIO) REFERENCES COMPETICIONS (EDICIO))")

    def close_con(self):
        self._con.close()

    def set_competicio(self, competicio):
        self._competicio = competicio

    def get_competicio(self) -> Competicio:
        return self._competicio

    def desar_competicio(self, nom_fitxer: str, competicio: Competicio):
        try:
            self.sql_connection()
            self.create_tables()
            self._cursor.execute(self.EDICIO_COMPETICIO, [int(nom_fitxer)])
            rows = self._cursor.fetchall()
            data = []
            if len(rows) == 0:
                data.clear()
                data.append(int(nom_fitxer))
                data.append(competicio.get_any())
                data.append(competicio.get_poblacio())
                self._cursor.execute(self.INSERT_COMPETICIO, data)
                self.insert_jutge(competicio, data, nom_fitxer)
            else:
                data.clear()
                data.append(competicio.get_any())
                data.append(competicio.get_poblacio())
                data.append(int(nom_fitxer))
                self._cursor.execute(self.UPDATE_COMPETICIO, data)
                self._cursor.execute(self.DELETE_JUTGE, [int(nom_fitxer)])
                self.insert_jutge(competicio, data, nom_fitxer)
            self._con.commit()
        except sqlite3.OperationalError as e:
            raise GestorErrors(9, getattr(e, 'message', repr(e)))
        finally:
            self._con.close()

    def insert_jutge(self, competicio, data, nom_fitxer):
        for component in competicio.get_components():
            if isinstance(component, Jutge):
                data.clear()
                data.append(component.get_dni())
                data.append(component.get_nom())
                data.append(int(nom_fitxer))
                self._cursor.execute(self.INSERT_JUTGE, data)

    def carregar_comapeticio(self, nom_fitxer: str):
        try:
            self.sql_connection()
            self._cursor.execute(self.EDICIO_COMPETICIO, [int(nom_fitxer)])
            rows = self._cursor.fetchall()
            self._competicio = Competicio(str(rows[0][1]), rows[0][2], rows[0][0])
            self._cursor.execute(self.SEL_JUTGE, [int(nom_fitxer)])
            rows = self._cursor.fetchall()
            for row in rows:
                jutge = Jutge(row[1], row[0])
                jutge.show_component()
                self._competicio.add_jutge(jutge)
        except sqlite3.OperationalError as e:
            raise GestorErrors(9, getattr(e, 'message', repr(e)))
        finally:
            self._con.close()
