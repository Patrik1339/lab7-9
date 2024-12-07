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


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__repository_persoane = RepositoryPersoane('fisier_teste_persoane.txt')
        self.__repository_evenimente = RepositoryEvenimente('fisier_teste_evenimente.txt')
        self.__repository_participanti = RepositoryParticipanti('fisier_teste_participanti.txt')
        self.__validator_persoane = ValidatorPersoane()
        self.__validator_evenimente = ValidatorEvenimente()
        self.__service_persoane = ServicePersoane(self.__validator_persoane, self.__repository_persoane, self.__repository_participanti)
        self.__service_evenimente = ServiceEvenimente(self.__validator_evenimente, self.__repository_evenimente, self.__repository_participanti)
        self.__service_participanti = ServiceParticipanti(self.__validator_persoane, self.__validator_evenimente, self.__repository_persoane, self.__repository_evenimente, self.__repository_participanti, self.__service_persoane, self.__service_evenimente)
        self.eveniment1 = Evenimente(1, "11.11.2024", 120, "Eveniment")
        self.eveniment2 = Evenimente(2, "20.08.2022", 80, "Eveniment2")
        self.persoana1 = Persoane(1, "Alex", "strada Mihai Eminescu")
        self.persoana2 = Persoane(2, "Gigi", "strada Vaida Voievod")

    def tearDown(self):
        """
        Metoda care goleste dictionarele de persoane, evenimente si participanti
        :return: Nimic
        """
        self.__repository_persoane.set_persoane({})
        self.__repository_evenimente.set_evenimente({})
        self.__repository_participanti.set_participanti({})

    def test_participanti(self):
        """
        Test participanti
        :return:
        """
        self.tearDown()
        self.__repository_persoane.adauga_persoana(self.persoana1)
        self.__repository_evenimente.adauga_eveniment(self.eveniment1)
        self.__service_participanti.inscrie_persoana(1,1)
        self.assertEqual(self.__repository_participanti.get_participanti(),{1:[1]})


    def test_creeaza_persoana(self):
        """
        Test pentru constructorul clasei Persoane
        :return: Nimic
        """
        persoana = Persoane(1,"Alex", "strada Mihai Eminescu")
        self.assertEqual(persoana.get_id_persoana(), 1)
        self.assertEqual(persoana.get_nume(),"Alex")
        self.assertEqual(persoana.get_adresa(),"strada Mihai Eminescu")

    def test_adauga_eveniment_raise_exception(self):
        self.__repository_evenimente.adauga_eveniment(self.eveniment1)
        with self.assertRaises(RepositoryError) as context:
            self.__repository_evenimente.adauga_eveniment(self.eveniment1)
        self.assertEqual(str(context.exception), "Eveniment existent!")

    def test_sterge_eveniment_raise_exception(self):
        self.tearDown()
        self.assertEqual("Evenimentul nu exista!", self.__repository_evenimente.sterge_eveniment(99))

    def test_creeaza_evenimente(self):
        eveniment = Evenimente(1,"11.11.2024", 120, "Eveniment")
        self.assertEqual(eveniment.get_id_eveniment(), 1)
        self.assertEqual(eveniment.get_timp(), 120)
        self.assertEqual(eveniment.get_data(), "11.11.2024")
        self.assertEqual(eveniment.get_descriere(), "Eveniment")
        eveniment.set_timp(123)
        self.assertEqual(eveniment.get_timp(), 123)
        eveniment.set_descriere("Descriere setata")
        self.assertEqual(eveniment.get_descriere(), "Descriere setata")
        eveniment.set_data("15.09.2023")
        self.assertEqual(eveniment.get_data(), "15.09.2023")

    def test_service_adauga_persoana(self):
        """
        Metoda de teste pentru metoda adauga_persoana - BlackBox testing
        :return: Nimic
        """
        self.assertEqual("Id invalid!\n", self.__service_persoane.adauga_persoana(-1, "Alex", "strada Mihai Eminescu"))
        self.assertEqual("Numele trebuie sa aiba cel putin 3 caractere!\n", self.__service_persoane.adauga_persoana(1, "A", "strada Mihai Eminescu"))
        self.assertEqual("Numele trebuie sa fie nevid!\nNumele trebuie sa aiba cel putin 3 caractere!\n", self.__service_persoane.adauga_persoana(1, "", "strada Mihai Eminescu"))
        self.assertEqual("Numele nu poate fi un numar!\n", self.__service_persoane.adauga_persoana(1, "1234", "strada Mihai Eminescu"))
        self.assertEqual("Adresa trebuie sa fie nevida!\nAdresa trebuie sa aiba cel putin 5 caractere!\n", self.__service_persoane.adauga_persoana(1, "Alex", ""))
        self.assertEqual("Adresa trebuie sa aiba cel putin 5 caractere!\n", self.__service_persoane.adauga_persoana(1, "Alex", "A"))
        self.assertEqual("Adresa nu poate sa fie un numar!\n", self.__service_persoane.adauga_persoana(1, "Alex", "12345"))

    def test_sterge_persoana(self):
        """
        Metoda de test pentru metoda sterge_persoana - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        self.assertEqual("Persoana inexistenta!", self.__service_persoane.sterge_persoana(1))
        self.__repository_persoane.set_persoane({1:self.persoana1,2:self.persoana2})
        self.assertEqual({1: self.persoana1, 2: self.persoana2}, self.__repository_persoane.get_all())
        self.__service_persoane.sterge_persoana(1)
        self.assertEqual({2: self.persoana2}, self.__repository_persoane.get_all())

    def test_modifica_persoana(self):
        """
        Metoda de test pentru metoda modifica_persoana - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        self.assertEqual("Persoana inexistenta!", self.__service_persoane.modifica_persoana(1, "Alex", "strada Mihai Eminescu"))
        self.__repository_persoane.set_persoane({1: self.persoana1})
        self.__service_persoane.modifica_persoana(1, "Gigi", "strada Vaida Voievod")
        persoana_modificata = Persoane(1, "Gigi", "strada Vaida Voievod")
        self.assertEqual(self.__service_persoane.cauta_persoana(1), persoana_modificata)

    def test_cauta_persoana(self):
        """
        Metoda de test pentru metoda cauta_persoana - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        self.assertEqual("Persoana inexistenta!", self.__service_persoane.cauta_persoana(1))
        self.__repository_persoane.set_persoane({1: self.persoana1})
        self.assertEqual(self.persoana1, self.__service_persoane.cauta_persoana(1))

    def test_adauga_eveniment(self):
        """
        Metoda de test pentru metoda adauga_eveniment - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment = Evenimente(1, "11.11.1111", "3:20", "Eveniment")
        self.__service_evenimente.adauga_eveniment(1, "11.11.1111", "3:20", "Eveniment")
        dictionar_asteptat = {1: eveniment}
        self.assertEqual(dictionar_asteptat, self.__repository_evenimente.get_all())
        self.assertEqual("Eveniment existent!", self.__service_evenimente.adauga_eveniment(1, "11.11.1111", "3:20", "Eveniment"))
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__service_evenimente.adauga_eveniment(2, "20.09.2024", "5:30", "Eveniment2")
        dictionar_asteptat = {1:eveniment,2: eveniment2}
        self.assertEqual(dictionar_asteptat, self.__repository_evenimente.get_all())

    def test_sterge_eveniment(self):
        """
        Metoda de test pentru metoda sterge_eveniment - WhiteBox testing
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        self.assertEqual("Eveniment inexistent!", self.__service_evenimente.sterge_eveniment(1))
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        self.__service_evenimente.sterge_eveniment(1)
        dictionar_asteptat = {2:eveniment2}
        self.assertEqual(dictionar_asteptat, self.__repository_evenimente.get_all())

    def test_modifica_eveniment(self):
        """
        Metoda de test pentru metoda modifica_eveniment - WhiteBox testing
        :return: Nimic
        """
        self.__repository_evenimente.set_empty()
        self.assertEqual("Eveniment inexistent!", self.__service_evenimente.modifica_eveniment(1, "11.11.1111", "3:20", "Eveniment"))
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        self.__service_evenimente.modifica_eveniment(1, "10.10.1000", "3:00", "Eveniment modificat")
        eveniment3 = Evenimente(1, "10.10.1000", "3:00", "Eveniment modificat")
        dictionar_asteptat = {1:eveniment3,2:eveniment2}
        self.assertEqual(dictionar_asteptat, self.__repository_evenimente.get_all())

    def test_modifica_eveniment_succes(self):
        self.__repository_evenimente.set_empty()
        self.__service_evenimente.adauga_eveniment(1, "11.11.1111", "3:20", "Eveniment")
        eveniment_modificat = Evenimente(1, "11.11.1111", "3:20", "Eveniment modificat")
        self.assertEqual(self.__repository_evenimente.modifica_eveniment(1, "11.11.1111", "3:20", "Eveniment modificat"), eveniment_modificat)

    def test_modifica_eveniment_exceptie(self):
        with self.assertRaises(RepositoryError) as context:
            self.__repository_evenimente.modifica_eveniment(99, "2024-12-07", "15:00", "Eveniment inexistent")
        self.assertEqual(str(context.exception), "Evenimentul cu ID-ul 99 nu exista!")

    def test_get_persoane(self):
        self.tearDown()
        self.assertEqual(self.__service_persoane.get_persoane(),{})

    def test_cauta_eveniment(self):
        """
        Metoda de test pentru metoda cauta_eveniment - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        self.assertEqual("Eveniment inexistent!", self.__service_evenimente.cauta_eveniment(1))
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1:eveniment1,2:eveniment2})
        self.assertEqual(eveniment1, self.__service_evenimente.cauta_eveniment(1))

    def test_inscrie_persoana(self):
        """
        Metoda de test pentru metoda inscrie_persoana - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1: eveniment1,2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1,2: persoana2})
        self.__service_participanti.inscrie_persoana(2, 1)
        dictionar_asteptat = {1: [2]}
        self.assertEqual(self.__repository_participanti.get_participanti(), dictionar_asteptat)
        self.__service_participanti.inscrie_persoana(1, 1)
        dictionar_asteptat = {1: [2, 1]}
        self.assertEqual(self.__repository_participanti.get_participanti(), dictionar_asteptat)

    def test_participanti_2(self):
        participant1 = Participanti(1,1)
        participant2 = Participanti(2,2)
        self.assertEqual(participant1 == participant2, False)
        self.assertEqual(participant1, participant1)
        self.assertEqual(participant1.get_persoana(), 1)
        self.assertEqual(participant1.__repr__(), 'Evenimente(id_persoana=1, id_eveniment=1)')

    def test_sterge_participant(self):
        """
        Metoda de test pentru metoda sterge_participant - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "Eveniment1")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "Eveniment2")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1, 2: persoana2})
        self.__service_participanti.inscrie_persoana(1, 1)
        self.__service_participanti.sterge_participant(1, 1)
        dictionar_asteptat = {}
        self.assertEqual(self.__repository_participanti.get_participanti(), dictionar_asteptat)
        self.__service_participanti.inscrie_persoana(1, 1)
        self.__service_participanti.inscrie_persoana(2, 1)
        self.__service_participanti.sterge_participant(1, 1)
        dictionar_asteptat = {1: [2]}
        self.assertEqual(self.__repository_participanti.get_participanti(), dictionar_asteptat)

    def test_lista_descriere(self):
        """
        Metoda de test pentru metoda lista_descriere - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.1111", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana = Persoane(1, "Alex", "strada")
        self.__repository_persoane.set_persoane({1: persoana})
        self.__repository_participanti.set_participanti({1: [1], 2: [1]})
        lista_asteptata = [eveniment2, eveniment1]
        self.assertEqual(self.__service_participanti.lista_descriere(1), lista_asteptata)

    def test_lista_data(self):
        """
        Metoda de test pentru metoda lista_data - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.2024", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana = Persoane(1, "Alex", "strada")
        self.__repository_persoane.set_persoane({1: persoana})
        self.__repository_participanti.set_participanti({1: [1], 2: [1]})
        lista_asteptata = [eveniment2, eveniment1]
        self.assertEqual(self.__service_participanti.lista_data(1), lista_asteptata)

    def test_participare_maxima(self):
        """
        Metoda de test pentru metoda participare_maxima - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.2024", "3:20", "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", "5:30", "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1, 2: persoana2})
        self.__repository_participanti.set_participanti({1: [1, 2], 2: [1]})
        self.assertEqual(self.__service_participanti.participare_maxima(), persoana1)

    def test_maxim_participanti(self):
        """
        Metoda de test pentru metoda maxim_participanti - WhiteBox testing
        :return: Nimic
        """
        self.tearDown()
        eveniment1 = Evenimente(1, "11.11.2024", 150, "BBBBB")
        eveniment2 = Evenimente(2, "20.09.2024", 120, "AAAAA")
        self.__repository_evenimente.set_evenimente({1: eveniment1, 2: eveniment2})
        persoana1 = Persoane(1, "Alex", "strada")
        persoana2 = Persoane(2, "Gigi", "strada 2")
        self.__repository_persoane.set_persoane({1: persoana1, 2: persoana2})
        self.__repository_participanti.set_participanti({1: [1], 2: [1, 2]})
        lista_asteptata = [(eveniment2,2), (eveniment1,1)]
        lista = self.__service_participanti.maxim_participanti()
        self.assertEqual(lista, lista_asteptata)
        dictionar_asteptat = {eveniment2: [persoana1,persoana2], eveniment1: [persoana1]}
        dictionar = self.__service_participanti.get_dict_participanti()
        self.assertEqual(dictionar, dictionar_asteptat)