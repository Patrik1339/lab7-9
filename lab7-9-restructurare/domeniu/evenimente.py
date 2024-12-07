class Evenimente(object):
    def __init__(self, id_eveniment, data, timp, descriere):
        """
        Constructor pentru obiecte din clasa Evenimente
        :param id: int
        :param data: string
        :param timp: int
        :param descriere: string
        """
        self.__id_eveniment = id_eveniment
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def __eq__(self, other):
        if not isinstance(other, Evenimente):
            return False
        return (self.get_id_eveniment() == other.get_id_eveniment() and
                self.get_data() == other.get_data() and
                self.get_timp() == other.get_timp() and
                self.get_descriere() == other.get_descriere())

    def __hash__(self):
        return hash(self.__id_eveniment)

    def __repr__(self):
        return f"Evenimente(id={self.get_id_eveniment()}, Data='{self.get_data()}', Timp='{self.get_timp()}, Descriere='{self.get_descriere()}')"

    def get_id_eveniment(self):
        """
        Metoda care returneaza idul evenimentului
        :return: id_eveniment
        """
        return self.__id_eveniment

    def get_data(self):
        """
        Metoda care returneaza data evenimentului
        :return: data
        """
        return self.__data

    def get_timp(self):
        """
        Metoda care returneaza timpul cand are loc evenimentul
        :return: timp
        """
        return self.__timp

    def get_descriere(self):
        """
        Metoda care returneaza descrierea evenimentului
        :return: descriere
        """
        return self.__descriere

    def set_data(self, data):
        """
        Metoda care seteaza data evenimentului
        :param data: string
        :return: Nimic
        """
        self.__data = data

    def set_timp(self, timp):
        """
        Metoda care seteaza timpul evenimentului
        :param timp: int
        :return: Nimic
        """
        self.__timp = timp

    def set_descriere(self, descriere):
        """
        Metoda care seteaza descrierea evenimentului
        :param descriere: string
        :return: Nimic
        """
        self.__descriere = descriere