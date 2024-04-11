from dataclasses import *

#from model.studente import Studente


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    studenti_iscritti: list

    def __str__(self):
        return f'{self.nome} ({self.codins})'

    def add_iscritto(self, studente):
        self.studenti_iscritti.append(studente)
