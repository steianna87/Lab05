from database.corso_DAO import CorsoDAO
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

    def add_corsi(self):
        corsoDAO = CorsoDAO()
        corsoDAO.get_methods()
        for cDAO in corsoDAO.corsi:
            c = Corso(cDAO['codins'], cDAO['crediti'], cDAO['nome'], cDAO['pd'])
            self.listaCorsi.append(c)

    def add_studenti(self):
        stDAO = StudenteDAO()
        stDAO.get_methods()
        for sDAO in stDAO.studenti:
            s = Studente(sDAO['matricola'], sDAO['cognome'], sDAO['nome'], sDAO['CDS'])
            self.listaStudenti.append(s)

if __name__ == '__main__':
    m = Model()
    print(m.listaCorsi)
    print(m.listaStudenti)