from domeniu.evenimente import Evenimente
from erori.repository_error import RepositoryError


class ServiceEvenimente:
    def __init__(self, validator_evenimente, repository_evenimente, repository_participanti):
        self.__validator_evenimente = validator_evenimente
        self.__repository_evenimente = repository_evenimente
        self.__repository_participanti = repository_participanti

    def adauga_eveniment(self, id_eveniment, data, timp, descriere):
        """
        Adauga un eveniment in lista de evenimente
        :param id_eveniment: int
        :param data: string
        :param timp: string
        :param descriere: string
        :return: Nimic
        """
        try:
            if id_eveniment in self.__repository_evenimente.get_all():
                raise RepositoryError("Eveniment existent!")
            eveniment = Evenimente(id_eveniment, data, timp, descriere)
            erori = self.__validator_evenimente.valideaza_eveniment(eveniment)
            if len(erori) > 0:
                raise RepositoryError(erori)
            self.__repository_evenimente.adauga_eveniment(eveniment)
            return "Evenimentul a fost adaugat cu succes!"
        except RepositoryError as re:
            return str(re)

    def get_evenimente(self):
        """
        Afișează evenimentele
        :return: lista de evenimente sau un mesaj de eroare
        """
        try:
            evenimente = self.__repository_evenimente.get_all()
            if not evenimente:
                raise RepositoryError("Nu exista evenimente in lista!")
            return evenimente
        except RepositoryError as re:
            return str(re)

    def sterge_eveniment(self, id_eveniment):
        """
        Sterge evenimentul cu idul id_eveniment din lista de evenimente
        :param id_eveniment: int
        :return: Nimic
        """
        try:
            if self.__repository_evenimente.get_all() is not None:
                if id_eveniment not in self.__repository_evenimente.get_all():
                    raise RepositoryError("Eveniment inexistent!")
            self.__repository_evenimente.sterge_eveniment(id_eveniment)
            self.__repository_participanti.sterge_eveniment(id_eveniment)
            return "Evenimentul a fost sters cu succes!"
        except RepositoryError as re:
            return str(re)

    def modifica_eveniment(self, id_eveniment, data, timp, descriere):
        """
        Modifica evenimentul cu idul id_eveniment din lista de evenimente
        :param id_eveniment: int
        :param data: string
        :param timp: string
        :param descriere: string
        :return:
        """
        try:
            if self.__repository_evenimente.get_all() is not None:
                if id_eveniment not in self.__repository_evenimente.get_all():
                    raise RepositoryError("Eveniment inexistent!")
            self.cauta_eveniment(id_eveniment)
            self.__repository_evenimente.modifica_eveniment(id_eveniment, data, timp, descriere)
            return "Evenimentul a fost modificat cu succes!"
        except RepositoryError as re:
            return str(re)

    def cauta_eveniment(self, id_eveniment):
        """
        Cauta evenimentul cu idul id_eveniment in lista de evenimente
        :param id_eveniment: int
        :return: evenimentul gasit
        """
        try:
            if self.__repository_evenimente.get_all() is not None:
                if id_eveniment in self.__repository_evenimente.get_all():
                    return self.__repository_evenimente.evenimente[id_eveniment]
            raise RepositoryError("Eveniment inexistent!")
        except RepositoryError as re:
            return str(re)