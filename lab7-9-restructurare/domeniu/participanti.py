class Participanti:
    def __init__(self, id_persoana, id_eveniment):
        self.__id_persoana = id_persoana
        self.__id_eveniment = id_eveniment

    def __eq__(self, other):
        if not isinstance(other, Participanti):
            return False
        return self.__id_persoana == other.__id_persoana and self.__id_eveniment == other.__id_eveniment

    def __repr__(self):
        return f"Evenimente(id_persoana={self.get_persoana()}, id_eveniment={self.get_eveniment()})"

    def get_persoana(self):
        return self.__id_persoana

    def get_eveniment(self):
        return self.__id_eveniment