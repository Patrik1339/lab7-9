class Persoane(object):
    def __init__(self, id_persoana, nume, adresa):
        """
        Constructor pentru obiecte din clasa persoane
        :param id_persoana: int
        :param nume: string
        :param adresa: string
        """
        self.__id_persoana = id_persoana
        self.__nume = nume
        self.__adresa = adresa

    def __eq__(self, other):
        if not isinstance(other, Persoane):
            return False
        return (self.get_id_persoana() == other.get_id_persoana() and
                self.get_nume() == other.get_nume() and
                self.get_adresa() == other.get_adresa())

    def __repr__(self):
        return f"Persoane(id={self.get_id_persoana()}, nume='{self.get_nume()}', adresa='{self.get_adresa()}')"

    def get_id_persoana(self):
        """
        Metoda care returneaza idul persoanei
        :return: id_persoana
        """
        return self.__id_persoana

    def get_nume(self):
        """
        Metoda care returneaza numele persoanei
        :return: nume
        """
        return self.__nume

    def get_adresa(self):
        """
        Metoda care returneaza adresa persoanei
        :return: adresa
        """
        return self.__adresa

    def set_nume(self, nume):
        """
        Metoda care seteaza numele persoanei
        :param nume: string
        :return: Nimic
        """
        self.__nume = nume

    def set_adresa(self, adresa):
        """
        Metoda care seteaza adresa persoanei
        :param adresa: string
        :return: Nimic
        """
        self.__adresa = adresa