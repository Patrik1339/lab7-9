from domeniu.persoane import Persoane
from erori.repository_error import RepositoryError


class ServicePersoane:
    def __init__(self, validator_persoane, repository_persoane, repository_participanti):
        self.__validator_persoane = validator_persoane
        self.__repository_persoane = repository_persoane
        self.__repository_participanti = repository_participanti

    def adauga_persoana(self, id_persoana, nume, adresa):
        """
        Adauga o persoana
        :param id_persoana: int
        :param nume: string
        :param adresa: string
        :return: Nimic
        """
        try:
            if self.__repository_persoane.get_all() is not None:
                if id_persoana in self.__repository_persoane.get_all():
                    raise RepositoryError("Persoana existenta!")
            persoana = Persoane(id_persoana, nume, adresa)
            erori = self.__validator_persoane.valideaza_persoana(persoana)
            if len(erori) > 0:
                raise RepositoryError(erori)
            self.__repository_persoane.adauga_persoana(persoana)
            return "Persoana a fost adaugata cu succes!"
        except RepositoryError as re:
            return str(re)

    def get_persoane(self):
        """
        Afiseaza persoanele
        :return: lista de persoane
        """
        if self.__repository_persoane.get_all() is None:
            return []
        return self.__repository_persoane.get_all()

    def sterge_persoana(self, id_persoana):
        """
        Sterge persoana cu idul id_persoana din lista de persoane
        :param id_persoana: int
        :return: Mesaj de succes sau eroare
        """
        try:
            persoane = self.__repository_persoane.get_all()
            if not persoane:
                raise RepositoryError("Persoana inexistenta!")
            if id_persoana not in persoane:
                raise RepositoryError("Persoana inexistenta!")
            persoana = self.cauta_persoana(id_persoana)
            self.__repository_persoane.sterge_persoana(id_persoana)
            for eveniment in self.__repository_participanti.get_participanti():
                if id_persoana in self.__repository_participanti.get_participanti()[eveniment]:
                    self.__repository_participanti.sterge_participant(id_persoana, eveniment)
                    break
            return "Persoana a fost stearsa cu succes!"
        except RepositoryError as re:
            return str(re)

    def modifica_persoana(self, id_persoana, nume, adresa):
        """
        Modifica persoana cu idul id_persoana din lista de persoane
        :param id_persoana: int
        :param nume: string
        :param adresa: string
        :return:
        """
        try:
            persoane = self.__repository_persoane.get_all()
            if not persoane:
                raise RepositoryError("Persoana inexistenta!")
            if id_persoana in persoane:
                self.cauta_persoana(id_persoana)
                self.__repository_persoane.modifica_persoana(id_persoana, nume, adresa)
                return "Persoana a fost modificata cu succes!"
            else:
                raise RepositoryError("Persoana inexistenta!")
        except RepositoryError as re:
            return str(re)

    def cauta_persoana(self, id_persoana):
        """
        Cauta persoana cu idul id_persoana in lista de persoane
        :param id_persoana: int
        :return: persoana gasita
        """
        try:
            if id_persoana in self.__repository_persoane.persoane:
                return self.__repository_persoane.get_all()[id_persoana]
            else:
                raise RepositoryError("Persoana inexistenta!")
        except RepositoryError as re:
            return str(re)