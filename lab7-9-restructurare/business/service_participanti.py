from domeniu.participanti import Participanti
from erori.repository_error import RepositoryError
from datetime import datetime

class ServiceParticipanti:
    def __init__(self, validator_persoane, validator_evenimente, repository_persoane, repository_evenimente, repository_participanti, service_persoane, service_evenimente):
        self.__validator_persoane = validator_persoane
        self.__validator_evenimente = validator_evenimente
        self.__repository_persoane = repository_persoane
        self.__repository_evenimente = repository_evenimente
        self.__repository_participanti = repository_participanti
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente

    def inscrie_persoana(self, id_persoana,id_eveniment):
        """
        Metoda care inscrie persoana cu idul id_persoana la evenimentul cu idul id_eveniment
        :param id_persoana: int
        :param id_eveniment: int
        :return: mesaj
        """
        try:
            if id_eveniment not in self.__repository_evenimente.get_all().keys():
                raise RepositoryError("Eveniment inexistent!")
            if id_persoana not in self.__repository_persoane.get_all().keys():
                raise RepositoryError("Persoana inexistenta!")
            eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
            persoana = self.__service_persoane.cauta_persoana(id_persoana)
            mesaj = self.__repository_participanti.adauga_persoana(persoana, eveniment)
            return mesaj
        except RepositoryError as re:
            return str(re)

    def get_participanti(self):
        """
        Metoda care returneaza lista de participanti
        :return: Nimic
        """
        participanti = self.__repository_participanti.get_participanti()
        return participanti

    def get_dict_participanti(self):
        participanti2 = {}
        participanti = self.__repository_participanti.get_participanti()
        for id_eveniment in participanti:
            eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
            participanti2[eveniment] = []
            for id_persoana in participanti[id_eveniment]:
                participant = self.__service_persoane.cauta_persoana(id_persoana)
                participanti2[eveniment].append(participant)
        return participanti2

    def sterge_participant(self, id_participant, id_eveniment):
        """
        Metoda care sterge participantul cu idul id_participant de la evenimentul cu idul id_eveniment
        :param id_participant: int
        :param id_eveniment: int
        :return: mesaj
        """
        try:
            if not id_eveniment in self.__repository_participanti.get_participanti().keys():
                raise RepositoryError("Evenimentul nu are participanti!")
            if not id_participant in self.__repository_participanti.get_participanti()[id_eveniment]:
                raise RepositoryError("Persoana nu participa la acest eveniment!")
            self.__repository_participanti.sterge_participant(id_participant, id_eveniment)
            if len(self.__repository_participanti.get_participanti()[id_eveniment]) == 0:
                del self.__repository_participanti.get_participanti()[id_eveniment]
            return "Participantul a fost sters cu succes!"
        except RepositoryError as re:
            return str(re)

    def lista_descriere(self, id_persoana):
        """
        Metoda care returneaza lista de evenimente la care participa persoana cu idul id_persoana, ordonate dupa descriere
        :param id_persoana: int
        :return: lista de evenimente ordonata alfabetic dupa descriere
        """
        evenimente = []
        for id_eveniment, lista_persoane in self.__repository_participanti.get_participanti().items():
            if id_persoana in lista_persoane:
                eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
                evenimente.append(eveniment)
        evenimente = sorted(evenimente, key=lambda e: e.get_descriere())
        return evenimente

    def lista_data(self, id_persoana):
        """
        Metoda care returneaza lista de evenimente la care participa persoana cu idul id_persoana, ordonate dupa date
        :param id_persoana: int
        :return: lista de evenimente ordonata dupa date
        """
        evenimente = []
        for id_eveniment, lista_persoane in self.__repository_participanti.get_participanti().items():
            if id_persoana in lista_persoane:
                eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
                evenimente.append(eveniment)
        evenimente = sorted(evenimente, key=lambda e: datetime.strptime(e.get_data(), "%d.%m.%Y"))
        return evenimente

    def participare_maxima(self):
        """
        Metoda care returneaza persoana care participa la cele mai multe evenimente.
        :return: Persoana care participa la cele mai multe evenimente
        """
        participanti = self.__repository_participanti.get_participanti()
        if not participanti:
            raise RepositoryError("Nu exista participanti la nici un eveniment!")
        participari_persoane = {}
        for lista_persoane in participanti.values():
            for id_persoana in lista_persoane:
                if id_persoana not in participari_persoane:
                    participari_persoane[id_persoana] = 1
                else:
                    participari_persoane[id_persoana] += 1
        id_persoana_max = max(participari_persoane, key=participari_persoane.get)
        persoana_max = self.__service_persoane.cauta_persoana(id_persoana_max)
        return persoana_max

    def maxim_participanti(self):
        """
        Metoda care returneaza o lista de tuple (eveniment, numar_participanti) sortata descrescator dupa numarul de participanti
        si numarul maxim de participanti.
        :return: (lista_evenimente_tuplu, numar_maxim_participanti)
        """
        evenimente = {}
        for id_eveniment, lista_persoane in self.__repository_participanti.get_participanti().items():
            eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
            evenimente[eveniment] = len(lista_persoane)
        if not evenimente:
            raise RepositoryError("Nu exista participanti la nici un eveniment!")
        evenimente_sortate = sorted(evenimente.items(), key=lambda item: item[1], reverse=True)
        lista_evenimente_tuplu = [(eveniment, numar_participanti) for eveniment, numar_participanti in
                                  evenimente_sortate]
        return lista_evenimente_tuplu


