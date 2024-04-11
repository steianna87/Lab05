from database.corso_DAO import CorsoDAO
from database.iscrizione_DAO import IscrizioneDAO
from database.studente_DAO import StudenteDAO
from model.corso import Corso
from model.studente import Studente


class Model:
    def __init__(self):
        self.listaCorsi = []
        self.listaStudenti = []
        self.initialize()

    def initialize(self):
        self.add_corsi()
        self.add_studenti()
        self.add_iscrizioni()

    def add_corsi(self):
        corsoDAO = CorsoDAO()
        corsoDAO.get_methods()
        for cDAO in corsoDAO.corsi:
            c = Corso(cDAO['codins'], cDAO['crediti'], cDAO['nome'], cDAO['pd'], [])
            self.listaCorsi.append(c)

    def add_studenti(self):
        stDAO = StudenteDAO()
        stDAO.get_methods()
        for sDAO in stDAO.studenti:
            s = Studente(sDAO['matricola'], sDAO['cognome'], sDAO['nome'], sDAO['CDS'], [])
            self.listaStudenti.append(s)

    def get_corso(self, codins):
        for corso in self.listaCorsi:
            if corso.codins == codins:
                return corso

    def get_studente(self, matricola):
        for studente in self.listaStudenti:
            if studente.matricola == matricola:
                return studente

    def add_iscrizioni(self):
        iscrizioneDAO = IscrizioneDAO()
        iscrizioneDAO.get_methods()
        for iscrizione in iscrizioneDAO.iscrizioni:
            studente = self.get_studente(iscrizione['matricola'])
            corso = self.get_corso(iscrizione['codins'])
            # Iscrizioni nelle rispettive classi (Corso, Studente):
            studente.add_corso(corso)
            corso.add_iscritto(studente)

    def iscriviStudente(self, studente: Studente, corso: Corso) -> bool:
        if (studente.corsi_dove_iscritto.__contains__(corso)
                and corso.studenti_iscritti.__contains__(studente)):
            return False
        nuovaIscrizione = IscrizioneDAO()
        nuovaIscrizione.get_methods()
        nuovaIscrizione.nuova_iscrizione(studente, corso)
        # Iscrizioni nelle rispettive classi (Corso, Studente):
        studente.add_corso(corso)
        corso.add_iscritto(studente)
        return True




if __name__ == '__main__':
    m = Model()
    print(m.listaCorsi)
    print(m.listaStudenti)
