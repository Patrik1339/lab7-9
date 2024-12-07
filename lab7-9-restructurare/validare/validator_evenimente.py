from domeniu.evenimente import Evenimente


class ValidatorEvenimente:
    def __init__(self):
        pass

    def valideaza_eveniment(self, eveniment):
        """
        Functie care verifica daca idul int al evenimentului este pozitiv, daca data string este nevida, daca timpul este nevid si daca descrierea este nevida
        :return: Nimic, daca persoana este valida
        :raise: ValueError cu mesajul:
                "Id invalid!\n", cand idul este <=0
                "Data invalida!\n", cand data este ""
                "Timp invalid!\n", cand timpul este ""
                "Descriere invalida\n", cand descrierea este ""
        """
        erori = ""
        if eveniment.get_id_eveniment() <= 0:
            erori += "Idul trebuie sa fie un numar intreg pozitiv, nenul!\n"
        data = eveniment.get_data()
        if len(data) != 10:
            erori += "Data trebuie sa aiba exact 10 caractere!\n"
        elif data[2] != '.' or data[5] != '.':
            erori += "Data trebuie sa fie despartita de '.' !\n"
        else:
            zi_str, luna_str, an_str = data[:2], data[3:5], data[6:]
            if not (zi_str.isdigit() and luna_str.isdigit() and an_str.isdigit()):
                erori += "Data trebuie sa fie formata din cifre!\n"
            """else:
                zi, luna, an = int(zi_str), int(luna_str), int(an_str)
                if zi < 1 or zi > 31:
                    erori += "Data invalida!\n"
                if luna < 1 or luna > 12:
                    erori += "Data invalida!\n"
                if an < 1900 or an > 2100:
                    erori += "Data invalida!\n"""
        if eveniment.get_timp() == "":
            erori += "Timpul trebuie sa fie nevid!\n"
        if eveniment.get_descriere() == "":
            erori += "Descrierea trebuie sa fie nevida!\n"
        if eveniment.get_descriere().isdigit():
            erori += "Descrierea nu poate sa fie un numar!\n"
        return erori