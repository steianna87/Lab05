from dataclasses import *

#from model.corso import Corso


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    corsi_dove_iscritto: list

    def __str__(self):
        return f'{self.nome}, {self.cognome} ({self.matricola})'

    def add_corso(self, corso):
        self.corsi_dove_iscritto.append(corso)
