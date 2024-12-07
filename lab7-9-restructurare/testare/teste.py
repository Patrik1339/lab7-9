from logging import exception
from erori.repository_error import RepositoryError
from infrastructura.repository_persoane import RepositoryPersoane
from infrastructura.repository_evenimente import RepositoryEvenimente
from infrastructura.repository_participanti import RepositoryParticipanti
from validare.validator_evenimente import ValidatorEvenimente
from validare.validator_persoane import ValidatorPersoane
from business.service_persoane import ServicePersoane
from business.service_participanti import ServiceParticipanti
from business.service_evenimente import ServiceEvenimente
from domeniu.participanti import Participanti
from domeniu.evenimente import Evenimente
from domeniu.persoane import Persoane
import unittest


class Teste:
    def __init__(self):
        self.__repository_persoane = RepositoryPersoane('infrastructura/fisier_teste_persoane.txt')
        self.__repository_evenimente = RepositoryEvenimente('infrastructura/fisier_teste_evenimente.txt')
        self.__repository_participanti = RepositoryParticipanti('infrastructura/fisier_teste_participanti.txt')
        self.__validator_persoane = ValidatorPersoane()
        self.__validator_evenimente = ValidatorEvenimente()
        self.__service_persoane = ServicePersoane(self.__validator_persoane, self.__repository_persoane, self.__repository_participanti)
        self.__service_evenimente = ServiceEvenimente(self.__validator_evenimente, self.__repository_evenimente, self.__repository_participanti)
        self.__service_participanti = ServiceParticipanti(self.__validator_persoane, self.__validator_evenimente, self.__repository_persoane, self.__repository_evenimente, self.__repository_participanti, self.__service_persoane, self.__service_evenimente)

    def test_adauga_persoana(self):
        """
        Metoda de teste pentru metoda adauga_persoana
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        persoana1 = Persoane(1, "Alex", "strada Mihai Eminescu")
        self.__service_persoane.adauga_persoana(1, "Alex", "strada Mihai Eminescu")
        dictionar_asteptat = {1: persoana1}
        assert dictionar_asteptat == self.__repository_persoane.get_all()
        assert "Persoana existenta!" == self.__service_persoane.adauga_persoana(1, "Alex", "strada Mihai Eminescu")
        self.__service_persoane.adauga_persoana(1, "Alex", "strada Mihai Eminescu")
        assert dictionar_asteptat == self.__repository_persoane.get_all()
        self.__service_persoane.adauga_persoana(2, "Gigi", "strada 2")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        dictionar_asteptat = {1: persoana1, 2: persoana2}
        assert dictionar_asteptat == self.__repository_persoane.get_all()

    def test_sterge_persoana(self):
        """
        Metoda de test pentru metoda sterge_persoana
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        assert "Persoana inexistenta!" == self.__service_persoane.sterge_persoana(1)
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1:persoana1,2:persoana2})
        assert {1:persoana1,2:persoana2} == self.__repository_persoane.get_all()
        self.__service_persoane.sterge_persoana(1)
        assert {2:persoana2} == self.__repository_persoane.get_all()

    def test_modifica_persoana(self):
        """
        Metoda de test pentru metoda modifica_persoana
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        assert "Persoana inexistenta!" == self.__service_persoane.modifica_persoana(1, "Alex", "strada Mihai Eminescu")
        persoana1 = Persoane(1, "Alex", "strada")
        persoana_asteptata = Persoane(1, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1:persoana1})
        self.__service_persoane.modifica_persoana(1, "Gigi", "strada 2")
        assert {1: persoana_asteptata} == self.__repository_persoane.get_all()

    def test_cauta_persoana(self):
        """
        Metoda de test pentru metoda cauta_persoana
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        assert "Persoana inexistenta!" == self.__service_persoane.cauta_persoana(1)
        persoana1 = Persoane(1, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1:persoana1})
        assert persoana1 == self.__service_persoane.cauta_persoana(1)

    def test_adauga_eveniment(self):
        """
        Metoda de test pentru metoda adauga_eveniment
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        eveniment = Evenimente(1, "11.11.1111", "3:20", "Eveniment")
        self.__service_evenimente.adauga_eveniment(1, "11.11.1111", "3:20", "Eveniment")
        dictionar_asteptat = {1: eveniment}
        assert dictionar_asteptat == self.__repository_evenimente.get_all()
        assert "Eveniment existent!" == self.__service_evenimente.adauga_eveniment(1, "11.11.1111", "3:20", "Eveniment")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__service_evenimente.adauga_eveniment(2, "20.09.2024", "5:30", "Eveniment2")
        dictionar_asteptat = {1:eveniment,2: eveniment2}
        assert dictionar_asteptat == self.__repository_evenimente.get_all()

    def test_sterge_eveniment(self):
        """
        Metoda de test pentru metoda sterge_eveniment
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        assert "Eveniment inexistent!" == self.__service_evenimente.sterge_eveniment(1)
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        self.__service_evenimente.sterge_eveniment(1)
        dictionar_asteptat = {2:eveniment2}
        assert dictionar_asteptat == self.__repository_evenimente.get_all()

    def test_modifica_eveniment(self):
        """
        Metoda de test pentru metoda modifica_eveniment
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        assert "Eveniment inexistent!" == self.__service_evenimente.modifica_eveniment(1, "11.11.1111", "3:20", "Eveniment")
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        self.__service_evenimente.modifica_eveniment(1, "10.10.1000", "3:00", "Eveniment modificat")
        eveniment3 = Evenimente(1, "10.10.1000", "3:00", "Eveniment modificat")
        dictionar_asteptat = {1:eveniment3,2:eveniment2}
        assert dictionar_asteptat == self.__repository_evenimente.get_all()

    def test_cauta_eveniment(self):
        """
        Metoda de test pentru metoda cauta_eveniment
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        assert "Eveniment inexistent!" == self.__service_evenimente.cauta_eveniment(1)
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        assert eveniment1 == self.__service_evenimente.cauta_eveniment(1)

    def test_inscrie_persoana(self):
        """
        Metoda de test pentru metoda inscrie_persoana
        :return: Nimic
        """
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1: eveniment1,2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1,2: persoana2})
        self.__service_participanti.inscrie_persoana(2, 1)
        dictionar_asteptat = {1: [2]}
        assert self.__repository_participanti.get_participanti() == dictionar_asteptat
        self.__service_participanti.inscrie_persoana(1, 1)
        dictionar_asteptat = {1: [2, 1]}
        assert self.__repository_participanti.get_participanti() == dictionar_asteptat

    def test_sterge_participant(self):
        """
        Metoda de test pentru metoda sterge_participant
        :return: Nimic
        """
        self.__repository_participanti.set_empty()
        self.__repository_evenimente.set_empty()
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1, 2: persoana2})
        self.__service_participanti.inscrie_persoana(1, 1)
        self.__service_participanti.sterge_participant(1, 1)
        dictionar_asteptat = {}
        assert self.__repository_participanti.get_participanti() == dictionar_asteptat
        self.__service_participanti.inscrie_persoana(1, 1)
        self.__service_participanti.inscrie_persoana(2, 1)
        self.__service_participanti.sterge_participant(1, 1)
        dictionar_asteptat = {1: [2]}
        assert self.__repository_participanti.get_participanti() == dictionar_asteptat

    def test_lista_descriere(self):
        """
        Metoda de test pentru metoda lista_descriere
        :return: Nimic
        """
        self.__repository_participanti.set_empty()
        self.__repository_evenimente.set_empty()
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana = Persoane(1, "Alex", "strada")
        self.__repository_persoane.set_persoane({1: persoana})
        self.__repository_participanti.set_participanti({1: [1], 2: [1]})
        lista_asteptata = [eveniment2, eveniment1]
        assert self.__service_participanti.lista_descriere(1) == lista_asteptata

    def test_lista_data(self):
        """
        Metoda de test pentru metoda lista_data
        :return: Nimic
        """
        self.__repository_participanti.set_empty()
        self.__repository_evenimente.set_empty()
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.2024", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana = Persoane(1, "Alex", "strada")
        self.__repository_persoane.set_persoane({1: persoana})
        self.__repository_participanti.set_participanti({1: [1], 2: [1]})
        lista_asteptata = [eveniment2, eveniment1]
        assert self.__service_participanti.lista_data(1) == lista_asteptata

    def test_participare_maxima(self):
        """
        Metoda de test pentru metoda participare_maxima
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        self.__repository_evenimente.set_empty()
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.2024", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1, 2: persoana2})
        self.__repository_participanti.set_participanti({1: [1, 2], 2: [1]})
        assert self.__service_participanti.participare_maxima() == persoana1

    def test_maxim_participanti(self):
        """
        Metoda de test pentru metoda maxim_participanti
        :return: Nimic
        """
        self.__repository_persoane.set_empty()
        self.__repository_evenimente.set_empty()
        self.__repository_participanti.set_empty()
        eveniment1 = Evenimente(1, "11.11.2024", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_participanti.set_participanti({1: [1], 2: [1, 2]})
        lista_asteptata = [eveniment2, eveniment1]
        #assert self.__service_participanti.maxim_participanti() == lista_asteptata

    def ruleaza_toate_testele(self):
        self.test_adauga_persoana()
        self.test_sterge_persoana()
        self.test_modifica_persoana()
        self.test_cauta_persoana()
        self.test_adauga_eveniment()
        self.test_sterge_eveniment()
        self.test_modifica_eveniment()
        self.test_cauta_eveniment()
        self.test_inscrie_persoana()
        self.test_sterge_participant()
        self.test_lista_descriere()
        self.test_lista_data()
        self.test_participare_maxima()
        self.test_maxim_participanti()