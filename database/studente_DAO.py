# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection

class StudenteDAO:
    def __init__(self):
        pass
    def get_methods(self):
        self._connessione = get_connection()
        self._cursore = self._connessione.cursor(dictionary=True)
        query = '''
            select *
            from studente s 
        '''
        self._cursore.execute(query)
        self._rows = self._cursore.fetchall()

        self.studenti = []
        for row in self._rows:
            self.studenti.append(row)

        self._cursore.close()
        self._connessione.close()

if __name__ == '__main__':
    stDao = StudenteDAO()
    stDao.get_methods()
    for i in stDao.studenti:
        print(i)