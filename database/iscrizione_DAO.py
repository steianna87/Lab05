from database.DB_connect import get_connection

class IscrizioneDAO:
    def __init__(self):
        pass

    def get_methods(self):
        self._connessione = get_connection()
        self._cursore = self._connessione.cursor(dictionary=True)
        query = '''
            select *
            from iscrizione i 
        '''
        self._cursore.execute(query)
        self._rows = self._cursore.fetchall()

        self.iscrizioni = []
        for row in self._rows:
            self.iscrizioni.append(row)

        self._cursore.close()
        self._connessione.close()

    def nuova_iscrizione(self, studente, corso):
        self._connessione = get_connection()
        self._cursore = self._connessione.cursor()
        query = '''INSERT INTO iscrizione (matricola, codins) 
        VALUES (%s, %s)'''
        self._cursore.execute(query, (studente.matricola, corso.codins))
        self._connessione.commit()

        self._cursore.close()
        self._connessione.close()

