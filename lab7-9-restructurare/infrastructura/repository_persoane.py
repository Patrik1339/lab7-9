import os
from domeniu.persoane import Persoane
from erori.repository_error import RepositoryError


class RepositoryPersoane:
    def __init__(self, fisier):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.fisier = fisier
        self.persoane = {}
        if not os.path.exists(self.fisier):
            open(self.fisier, "w").close()
        self.incarca_din_fisier()

    def incarca_din_fisier(self):
        """
        Incarca persoanele din fisierul text.
        """
        self.persoane = {}
        with open(self.fisier, "r") as f:
            for linie in f:
                linie = linie.strip()
                if linie:
                    id_persoana, nume, adresa = linie.split(",")
                    self.persoane[int(id_persoana)] = Persoane(int(id_persoana), nume, adresa)

    def salveaza_in_fisier(self):
        """
        Salveaza persoanele in fisierul text.
        """
        with open(self.fisier, "w") as f:
            for id_persoana, persoana in self.persoane.items():
                linie = f"{id_persoana},{persoana.get_nume()},{persoana.get_adresa()}\n"
                f.write(linie)

    def adauga_persoana(self, persoana):
        """
        Adauga o persoana in lista de persoane
        :param persoana: persoana care trebuie adaugata
        :type persoana: Persoane
        """
        id_persoana = persoana.get_id_persoana()
        if id_persoana in self.persoane:
            raise RepositoryError("Persoana existenta!")
        self.persoane[id_persoana] = persoana
        self.salveaza_in_fisier()

    def sterge_persoana(self, id_persoana):
        """
        Sterge persoana cu idul id_persoana din lista de persoane
        :param id_persoana: int
        """
        if id_persoana in self.persoane:
            del self.persoane[id_persoana]
            self.salveaza_in_fisier()
        else:
            raise RepositoryError("Persoana nu exista!")

    def modifica_persoana(self, id_persoana, nume, adresa):
        """
        Modifica persoana cu idul id_persoana
        :param adresa: string
        :param nume: string
        :param id_persoana: int
        """
        if id_persoana not in self.persoane:
            raise RepositoryError(f"Persoana cu ID-ul {id_persoana} nu exista!")
        persoana = self.persoane[id_persoana]
        persoana.set_nume(nume)
        persoana.set_adresa(adresa)
        self.salveaza_in_fisier()

    def get_all(self):
        """
        Returneaza lista de persoane
        :return: dictionar de persoane
        """
        return self.persoane

    def set_empty(self):
        """
        Goleste lista de persoane si actualizeaza fisierul.
        """
        self.persoane = {}
        self.salveaza_in_fisier()

    def set_persoane(self, dictionar):
        """
        Inlocuieste dictionarul curent de persoane cu unul nou si actualizeaza fisierul.
        :param dictionar: Dictionar cu persoane
        """
        self.persoane = dictionar
        self.salveaza_in_fisier()

class RepositoryPersoaneFaraFisier:
    def __init__(self):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.persoane = {}

    def adauga_persoana(self, persoana):
        """
        Adauga o persoana in lista de persoane
        :param persoana: persoana care trebuie adaugata
        :type persoana: Persoane
        """
        id_persoana = persoana.get_id_persoana()
        if id_persoana in self.persoane:
            raise RepositoryError("Persoana existenta!")
        self.persoane[id_persoana] = persoana

    def sterge_persoana(self, id_persoana):
        """
        Sterge persoana cu idul id_persoana din lista de persoane
        :param id_persoana: int
        """
        if id_persoana in self.persoane:
            del self.persoane[id_persoana]
        else:
            raise RepositoryError("Persoana nu exista!")

    def modifica_persoana(self, id_persoana, nume, adresa):
        """
        Modifica persoana cu idul id_persoana
        :param adresa: string
        :param nume: string
        :param id_persoana: int
        """
        if id_persoana not in self.persoane:
            raise RepositoryError(f"Persoana cu ID-ul {id_persoana} nu exista!")
        persoana = self.persoane[id_persoana]
        persoana.set_nume(nume)
        persoana.set_adresa(adresa)

    def get_all(self):
        """
        Returneaza lista de persoane
        :return: dictionar de persoane
        """
        return self.persoane

    def set_empty(self):
        """
        Goleste lista de persoane si actualizeaza fisierul.
        """
        self.persoane = {}

    def set_persoane(self, dictionar):
        """
        Inlocuieste dictionarul curent de persoane cu unul nou si actualizeaza fisierul.
        :param dictionar: Dictionar cu persoane
        """
        self.persoane = dictionar