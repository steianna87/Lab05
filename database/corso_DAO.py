# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection

class CorsoDAO:
    def __init__(self):
        pass
    def get_methods(self):
        self._connessione = get_connection()
        self._cursore = self._connessione.cursor(dictionary=True)
        query = '''
            select *
            from corso c 
        '''
        self._cursore.execute(query)
        self._rows = self._cursore.fetchall()

        self.corsi = []
        for row in self._rows:
            self.corsi.append(row)

        self._cursore.close()
        self._connessione.close()

if __name__ == '__main__':
    stDao = CorsoDAO()
    stDao.get_methods()
    for i in stDao.corsi:
        print(i)