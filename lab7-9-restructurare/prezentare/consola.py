from domeniu.persoane import Persoane
from erori.repository_error import RepositoryError


class Ui:
    def __init__(self, service_persoane, service_evenimente, service_participanti):
        """
        Constructor pentru clasa Ui
        :param service_persoane: service pentru persoane
        :param service_evenimente: service pentru evenimente
        :param service_participanti: service pentru participanti
        """
        self.__service_persoane = service_persoane
        self.__service_evenimente = service_evenimente
        self.__service_participanti = service_participanti
        self.__comenzi = {
            'adauga_persoana': self.ui_adauga_persoana,
            'sterge_persoana': self.ui_sterge_persoana,
            'modifica_persoana': self.ui_modifica_persoana,
            'cauta_persoana': self.ui_cauta_persoana,
            'afisare_persoane': self.afisare_persoane,
            'adauga_eveniment': self.ui_adauga_eveniment,
            'sterge_eveniment': self.ui_sterge_eveniment,
            'modifica_eveniment': self.ui_modifica_eveniment,
            'cauta_eveniment': self.ui_cauta_eveniment,
            'afisare_evenimente': self.afisare_evenimente,
            'inscrie_persoana': self.ui_inscrie_persoana,
            'sterge_participant': self.ui_sterge_participant,
            'afisare_participanti': self.afisare_participanti,
            'lista_evenimente_descriere': self.ui_lista_evenimente_descriere,
            'lista_evenimente_data': self.ui_lista_evenimente_data,
            'participare_maxima': self.participare_maxima,
            'maxim_participanti': self.maxim_participanti,
            }

    def ui_adauga_persoana(self):
        try:
            id_persoana = int(input('Id persoana:'))
        except ValueError:
            print("Id invalid!")
            return
        nume = input('Nume:')
        adresa = input('Adresa:')
        print(self.__service_persoane.adauga_persoana(id_persoana, nume, adresa))

    def ui_sterge_persoana(self):
        id_persoana = int(input('Id persoana:'))
        print(self.__service_persoane.sterge_persoana(id_persoana))

    def ui_modifica_persoana(self):
        id_persoana = int(input('Id persoana:'))
        nume = input('Nume:')
        adresa = input('Adresa:')
        print(self.__service_persoane.modifica_persoana(id_persoana, nume, adresa))

    def ui_cauta_persoana(self):
        id_persoana = int(input('Id persoana:'))
        persoana = self.__service_persoane.cauta_persoana(id_persoana)
        if persoana is None:
            print("Persoana nu a fost gasita!")
            return
        print(f"Id: {persoana.get_id_persoana()} Nume: {persoana.get_nume()} Adresa: {persoana.get_adresa()}")

    def afisare_persoane(self):
        persoane = self.__service_persoane.get_persoane()
        if len(persoane) == 0:
            print("Nu exista persoane in lista!")
            return
        for id_persoana in persoane:
            print(f"Id: {persoane[id_persoana].get_id_persoana()} Nume: {persoane[id_persoana].get_nume()} Adresa: {persoane[id_persoana].get_adresa()}")

    def ui_adauga_eveniment(self):
        id_eveniment = int(input('Id eveniment:'))
        data = input('Data:')
        timp = input('Timp:')
        descriere = input('Descriere:')
        print(self.__service_evenimente.adauga_eveniment(id_eveniment, data, timp, descriere))

    def ui_sterge_eveniment(self):
        id_eveniment = int(input('Id eveniment:'))
        print(self.__service_evenimente.sterge_eveniment(id_eveniment))

    def ui_modifica_eveniment(self):
        id_eveniment = int(input('Id eveniment:'))
        data = input('Data:')
        timp = input('Timp:')
        descriere = input('Descriere:')
        print(self.__service_evenimente.modifica_eveniment(id_eveniment, data, timp, descriere))

    def ui_cauta_eveniment(self):
        id_eveniment = int(input('Id eveniment:'))
        eveniment = self.__service_evenimente.cauta_eveniment(id_eveniment)
        if eveniment is None:
            print("Evenimentul nu a fost gasit!")
            return
        print(f"Id: {eveniment.get_id_eveniment()} Data: {eveniment.get_data()} Timp: {eveniment.get_timp()} Descriere: {eveniment.get_descriere()}")

    def afisare_evenimente(self):
        evenimente = self.__service_evenimente.get_evenimente()
        if len(evenimente) == 0:
            print("Nu exista evenimente in lista!")
            return
        for id_eveniment in evenimente:
            print(f"Id: {evenimente[id_eveniment].get_id_eveniment()} Data: {evenimente[id_eveniment].get_data()} Timp: {evenimente[id_eveniment].get_timp()} Descriere: {evenimente[id_eveniment].get_descriere()}")

    def ui_inscrie_persoana(self):
        id_persoana = int(input('Id persoana:'))
        id_eveniment = int(input('Id eveniment:'))
        print(self.__service_participanti.inscrie_persoana(id_persoana, id_eveniment))

    def ui_sterge_participant(self):
        id_persoana = int(input('Id persoana:'))
        id_eveniment = int(input('Id eveniment:'))
        print(self.__service_participanti.sterge_participant(id_persoana, id_eveniment))

    def afisare_participanti(self):
        participanti = self.__service_participanti.get_participanti()
        if len(participanti) == 0:
            print("Nu exista participanti in lista!")
            return
        '''for eveniment in participanti:
            print(f"Id eveniment: {eveniment.get_id_eveniment()} Data: {eveniment.get_data()} Timp: {eveniment.get_timp()} Descriere: {eveniment.get_descriere()}")
            for participant in participanti[eveniment]:
                print(f"Id_participant: {participant.get_id_persoana()} Nume: {participant.get_nume()} Adresa: {participant.get_adresa()}")'''
        for id_eveniment in participanti:
            i = 1
            print(f"Idurile persoanelor care participa la evenimentul cu idul {id_eveniment} sunt:")
            for id_persoana in participanti[id_eveniment]:
                print(f"Id persoana {i}: {id_persoana}")
                i = i + 1

    def ui_lista_evenimente_descriere(self):
        id_persoana = int(input('Id persoana:'))
        evenimente = self.__service_participanti.lista_descriere(id_persoana)
        for eveniment in evenimente:
            print(f"Id: {eveniment.get_id_eveniment()} Data: {eveniment.get_data()} Timp: {eveniment.get_timp()} Descriere: {eveniment.get_descriere()}")

    def ui_lista_evenimente_data(self):
        id_persoana = int(input('Id persoana:'))
        evenimente = self.__service_participanti.lista_data(id_persoana)
        for eveniment in evenimente:
            print(f"Id: {eveniment.get_id_eveniment()} Data: {eveniment.get_data()} Timp: {eveniment.get_timp()} Descriere: {eveniment.get_descriere()}")

    def participare_maxima(self):
        persoana = self.__service_participanti.participare_maxima()
        print(f"Id persoana: {persoana.get_id_persoana()} Nume: {persoana.get_nume()} Adresa: {persoana.get_adresa()}")

    def maxim_participanti(self):
        evenimente = self.__service_participanti.maxim_participanti()
        n = int(len(evenimente) * 0.2) + 1
        if evenimente == []:
            print("Nu exista nici un participant la nici un eveniment!")
            return
        for i in range(n):
            ceva = evenimente[i]
            eveniment = ceva[0]
            numar_participanti = ceva[1]
            print(f"Descriere: {eveniment.get_id_eveniment()} Numar participanti: {numar_participanti}")

    def run(self):
        while True:
            print("----LISTA COMENZI----")
            print("COMENZI LISTA PERSOANE: adauga_persoana;   sterge_persoana; modifica_persoana;   afisare_persoane\nCOMENZI LISTA EVENIMENTE: adauga_eveniment;   sterge_eveniment;   modifica_eveniment;   afisare_evenimente\nCOMENZI CAUTARE: cauta_persoana;   cauta_eveniment\nCOMENZI PARTICIPANTI: inscrie_persoana;   sterge_participant;   afisare_participanti\nCOMENZI RAPOARTE: lista_evenimente_descriere;   lista_evenimente_data;   participare_maxima;   maxim_participanti")
            print("---------------")
            nume_comanda = input("COMANDA:")
            nume_comanda = nume_comanda.strip()
            if nume_comanda == "":
                continue
            if nume_comanda == "exit":
                return
            if nume_comanda not in self.__comenzi:
                print("Comanda invalida!")
            if nume_comanda in self.__comenzi:
                self.__comenzi[nume_comanda]()