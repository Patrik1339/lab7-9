import os
from domeniu.evenimente import Evenimente
from erori.repository_error import RepositoryError


class RepositoryEvenimente:
    def __init__(self, fisier):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.fisier = fisier
        self.evenimente = {}
        if not os.path.exists(self.fisier):
            open(self.fisier, "w").close()
        self.incarca_din_fisier()

    def incarca_din_fisier(self):
        """
        Incarca evenimentele din fisierul text.
        """
        self.evenimente = {}
        with open(self.fisier, "r") as f:
            for linie in f:
                linie = linie.strip()
                if linie:
                    id_eveniment, data, timp, descriere = linie.split(",")
                    self.evenimente[int(id_eveniment)] = Evenimente(int(id_eveniment), data, timp, descriere)

    def salveaza_in_fisier(self):
        """
        Salveaza evenimentele in fisierul text.
        """
        with open(self.fisier, "w") as f:
            for id_eveniment, eveniment in self.evenimente.items():
                linie = f"{id_eveniment},{eveniment.get_data()},{eveniment.get_timp()},{eveniment.get_descriere()}\n"
                f.write(linie)

    def adauga_eveniment(self, eveniment):
        """
        Adauga un eveniment in lista de evenimente.
        :param eveniment: evenimentul care trebuie adaugat
        """
        id_eveniment = eveniment.get_id_eveniment()
        if id_eveniment in self.evenimente:
            raise RepositoryError("Eveniment existent!")
        self.evenimente[id_eveniment] = eveniment
        self.salveaza_in_fisier()

    def sterge_eveniment(self, id_eveniment):
        """
        Sterge evenimentul cu idul id_eveniment din lista de evenimente.
        :param id_eveniment: int
        """
        try:
            if id_eveniment in self.evenimente:
                del self.evenimente[id_eveniment]
                self.salveaza_in_fisier()
            else:
                raise RepositoryError("Evenimentul nu exista!")
        except RepositoryError as re:
            return str(re)

    def modifica_eveniment(self, id_eveniment, data, timp, descriere):
        """
        Modifica evenimentul cu idul id_eveniment.
        :param id_eveniment: int
        :param data: string
        :param timp: string
        :param descriere: string
        """
        if id_eveniment not in self.evenimente:
            raise RepositoryError(f"Evenimentul cu ID-ul {id_eveniment} nu exista!")
        eveniment = self.evenimente[id_eveniment]
        eveniment.set_data(data)
        eveniment.set_timp(timp)
        eveniment.set_descriere(descriere)

        self.salveaza_in_fisier()
        return eveniment
    def get_all(self):
        """
        Returneaza dictionarul de evenimente.
        :return: dictionar de evenimente
        """
        return self.evenimente

    def set_empty(self):
        """
        Goleste lista de evenimente si actualizeaza fisierul.
        """
        self.evenimente = {}
        self.salveaza_in_fisier()

    def set_evenimente(self, dictionar):
        """
        Inlocuieste dictionarul curent de evenimente cu unul nou si actualizeaza fisierul.
        :param dictionar: Dictionar cu evenimente
        """
        self.evenimente = dictionar
        self.salveaza_in_fisier()

class RepositoryEvenimenteFaraFisier:
    def __init__(self):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.evenimente = {}

    def adauga_eveniment(self, eveniment):
        """
        Adauga un eveniment in lista de evenimente.
        :param eveniment: evenimentul care trebuie adaugat
        """
        id_eveniment = eveniment.get_id_eveniment()
        if id_eveniment in self.evenimente:
            raise RepositoryError("Eveniment existent!")
        self.evenimente[id_eveniment] = eveniment

    def sterge_eveniment(self, id_eveniment):
        """
        Sterge evenimentul cu idul id_eveniment din lista de evenimente.
        :param id_eveniment: int
        """
        if id_eveniment in self.evenimente:
            del self.evenimente[id_eveniment]
        else:
            raise RepositoryError("Evenimentul nu exista!")

    def modifica_eveniment(self, id_eveniment, data, timp, descriere):
        """
        Modifica evenimentul cu idul id_eveniment.
        :param id_eveniment: int
        :param data: string
        :param timp: string
        :param descriere: string
        """
        if id_eveniment not in self.evenimente:
            raise RepositoryError(f"Evenimentul cu ID-ul {id_eveniment} nu exista!")
        eveniment = self.evenimente[id_eveniment]
        eveniment.set_data(data)
        eveniment.set_timp(timp)
        eveniment.set_descriere(descriere)
        return eveniment

    def get_all(self):
        """
        Returneaza dictionarul de evenimente.
        :return: dictionar de evenimente
        """
        return self.evenimente

    def set_empty(self):
        """
        Goleste lista de evenimente si actualizeaza fisierul.
        """
        self.evenimente = {}

    def set_evenimente(self, dictionar):
        """
        Inlocuieste dictionarul curent de evenimente cu unul nou si actualizeaza fisierul.
        :param dictionar: Dictionar cu evenimente
        """
        self.evenimente = dictionar

