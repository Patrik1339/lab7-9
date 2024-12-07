import os
from erori.repository_error import RepositoryError


class RepositoryParticipanti:
    def __init__(self, fisier):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.fisier = fisier
        self.participanti = {}
        if not os.path.exists(self.fisier):
            open(self.fisier, "w").close()
        self.incarca_din_fisier()

    def incarca_din_fisier(self):
        """
        Incarca participantii din fisierul text.
        """
        self.participanti = {}
        with open(self.fisier, "r") as f:
            for linie in f:
                linie = linie.strip()
                if linie:
                    id_eveniment, id_participanti = linie.split(":")
                    id_eveniment = int(id_eveniment)
                    lista_participanti = list(map(int, id_participanti.split(","))) if id_participanti else []
                    self.participanti[id_eveniment] = lista_participanti

    def salveaza_in_fisier(self):
        """
        Salveaza participantii in fisierul text.
        """
        with open(self.fisier, "w") as f:
            for id_eveniment, lista_participanti in self.participanti.items():
                linie = f"{id_eveniment}:{','.join(map(str, lista_participanti))}\n"
                f.write(linie)

    def adauga_persoana(self, persoana, eveniment):
        """
        Adauga o persoana in lista de participanti a evenimentului dat.
        """
        id_eveniment = eveniment.get_id_eveniment()
        id_persoana = persoana.get_id_persoana()

        if id_eveniment in self.participanti:
            if id_persoana in self.participanti[id_eveniment]:
                raise RepositoryError("Persoana participa deja la acest eveniment!")
            self.participanti[id_eveniment].append(id_persoana)
        else:
            self.participanti[id_eveniment] = [id_persoana]

        self.salveaza_in_fisier()

    def get_participanti(self):
        """
        Returneaza dictionarul de participanti.
        """
        return self.participanti

    def sterge_participant(self, id_participant, id_eveniment):
        """
        Sterge participantul cu idul dat din evenimentul specificat.
        """
        if id_eveniment in self.participanti and id_participant in self.participanti[id_eveniment]:
            self.participanti[id_eveniment].remove(id_participant)
            self.salveaza_in_fisier()
        else:
            raise RepositoryError("Participantul sau evenimentul nu exista!")

    def sterge_eveniment(self, id_eveniment):
        """
        Sterge toate datele legate de un eveniment specific.
        """
        if id_eveniment in self.participanti:
            del self.participanti[id_eveniment]
            self.salveaza_in_fisier()
        else:
            raise RepositoryError("Evenimentul nu exista!")

    def set_empty(self):
        """
        Goleste dictionarul de participanti si actualizeaza fisierul.
        """
        self.participanti = {}
        self.salveaza_in_fisier()

    def set_participanti(self, dictionar):
        """
        Inlocuieste dictionarul curent cu unul nou si actualizeaza fisierul.
        """
        self.participanti = dictionar
        self.salveaza_in_fisier()

class RepositoryParticipantiFaraFisier:
    def __init__(self):
        """
        Initializeaza repository-ul si incarca datele din fisier, daca exista.
        Creeaza fisierul daca nu exista.
        """
        self.participanti = {}

    def adauga_persoana(self, persoana, eveniment):
        """
        Adauga o persoana in lista de participanti a evenimentului dat.
        """
        id_eveniment = eveniment.get_id_eveniment()
        id_persoana = persoana.get_id_persoana()

        if id_eveniment in self.participanti:
            if id_persoana in self.participanti[id_eveniment]:
                raise RepositoryError("Persoana participa deja la acest eveniment!")
            self.participanti[id_eveniment].append(id_persoana)
        else:
            self.participanti[id_eveniment] = [id_persoana]

    def get_participanti(self):
        """
        Returneaza dictionarul de participanti.
        """
        return self.participanti

    def sterge_participant(self, id_participant, id_eveniment):
        """
        Sterge participantul cu idul dat din evenimentul specificat.
        """
        if id_eveniment in self.participanti and id_participant in self.participanti[id_eveniment]:
            self.participanti[id_eveniment].remove(id_participant)
        else:
            raise RepositoryError("Participantul sau evenimentul nu exista!")

    def sterge_eveniment(self, id_eveniment):
        """
        Sterge toate datele legate de un eveniment specific.
        """
        if id_eveniment in self.participanti:
            del self.participanti[id_eveniment]
        else:
            raise RepositoryError("Evenimentul nu exista!")

    def set_empty(self):
        """
        Goleste dictionarul de participanti si actualizeaza fisierul.
        """
        self.participanti = {}

    def set_participanti(self, dictionar):
        """
        Inlocuieste dictionarul curent cu unul nou si actualizeaza fisierul.
        """
        self.participanti = dictionar