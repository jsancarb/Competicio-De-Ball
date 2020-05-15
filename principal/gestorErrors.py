class GestorErrors(Exception):
    """Gestio d'errors"""

    NAN = 1
    MAX_JUTGES = 2
    NO_EXIST_JUTGE = 3
    NO_EXIST_MODALITAT = 4
    NO_PARELLA_BALL = 5
    MODALITAT_SENSE_PARELLES = 6
    MAX_COMPONENTS = 7
    CARREGA_ES = 8
    DESAR_ES = 9
    DB_CONECT = 10

    def __init__(self, num=0, message=None) -> None:
        errors = {
            1: "L'opció introduïda no és numèrica",
            2: "La modalitat ja té tots els o les jutges necessaris/es",
            3: "No existeix aquest o aquesta jutge",
            4: "No existeix aquesta modalitat",
            5: "No s'ha pogut crear una parella per aquesta modalitat",
            6: "Aquesta modalitat no té parelles",
            7: "Ja no hi caben més components",
            8: "No s'ha pogut carregar la competició a causa d'error d'entrada/sortida",
            9: "No s'ha pogut desar la competició a causa d'error d'entrada/sortida",
            10: "Error al conectar amb la base de dades"
        }
        self._message = "¡¡¡ERROR!!! " + errors.get(num, "Error desconegut") + "\n" + str(message)
        super().__init__(self._message)

    def message(self):
        return self._message
