from domeniu.persoane import Persoane


class ValidatorPersoane:
    def __init__(self):
        pass

    def valideaza_persoana(self, persoana):
        """
        Functie care verifica daca idul int al persoanei este pozitiv, daca numele string este nevid si daca adresa este nevida
        :return: Nimic, daca persoana este valida
        :raise: ValueError cu mesajul:
                "Id invalid!\n", cand idul este <=0
                "Nume invalid!\n", cand numele este "", < 3 sau un numar
                "Adresa invalida!\n", cand adresa este "", < 5 sau un numar
        """
        erori = ""
        if persoana.get_id_persoana() <= 0:
            erori += "Id invalid!\n"
        if persoana.get_nume() == "":
            erori += "Numele trebuie sa fie nevid!\n"
        if len(persoana.get_nume()) < 3:
            erori += "Numele trebuie sa aiba cel putin 3 caractere!\n"
        if persoana.get_nume().isdigit():
            erori += "Numele nu poate fi un numar!\n"
        if persoana.get_adresa() == "":
            erori += "Adresa trebuie sa fie nevida!\n"
        if len(persoana.get_adresa()) < 5:
            erori += "Adresa trebuie sa aiba cel putin 5 caractere!\n"
        if persoana.get_adresa().isdigit():
            erori += "Adresa nu poate sa fie un numar!\n"
        return erori