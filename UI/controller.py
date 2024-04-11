import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_iscritti(self, e):
        daCercare = self._view.selezionaCorsi.value
        if daCercare is None or daCercare == '':
            self._view.create_alert('Selezionare un corso!')
            return
        risultato = []
        corso = self._model.get_corso(daCercare)
        for studente in corso.studenti_iscritti:
            risultato.append(studente)
        output = f'Ci sono {len(risultato)} iscritti al corso:\n'
        for i, s in enumerate(risultato):
            if i != 0:
                output += '\n'
            output += s.__str__()

        self._view.txt_result.controls.append(ft.Text(value=output))
        self._view.update_page()

    def handle_studente(self, e):
        daCercare = self._view.selezionaMatricola.value
        if daCercare is None or daCercare == '':
            self._view.create_alert("Selezionare una Matricola!")
            return
        studente = self._model.get_studente(int(daCercare))
        if studente is None:
            self._view.create_alert("Non c'è nessuno studente con questa Matricola!")
            return


        self._view.nomeStudente.value = studente.nome
        self._view.cognomeStudente.value = studente.cognome
        self._view.update_page()

    def handle_corsi(self, e):
        matr_daCercare = self._view.selezionaMatricola.value
        if matr_daCercare is None or matr_daCercare == '':
            self._view.create_alert("Selezionare una Matricola!")
            return
        if self._view.nomeStudente.value == '' or self._view.cognomeStudente.value == '':
            self._view.create_alert("Cerca prima lo studente!")
            return
        studente = self._model.get_studente(int(matr_daCercare))
        if len(studente.corsi_dove_iscritto) == 0:
            self._view.create_alert("Questo studente non è iscritto in nessun corso!")
            return

        risultato = []
        for corso in studente.corsi_dove_iscritto:
            risultato.append(corso)
        output = f'Risultano {len(risultato)} corsi:\n'
        for i, c in enumerate(risultato):
            if i != 0:
                output += '\n'
            output += c.__str__()

        self._view.txt_result.controls.append(ft.Text(value=output))
        self._view.update_page()

    def iscrivi(self, e):
        matr_daIscrivere = self._view.selezionaMatricola.value
        corso_su_cui_iscrivere = self._view.selezionaCorsi.value
        if matr_daIscrivere is None or matr_daIscrivere == '':
            self._view.create_alert("Selezionare una Matricola!")
            return
        if corso_su_cui_iscrivere is None or corso_su_cui_iscrivere == '':
            self._view.create_alert('Selezionare un corso!')
            return
        studente = self._model.get_studente(int(matr_daIscrivere))
        corso = self._model.get_corso(corso_su_cui_iscrivere)
        if studente is None:
            self._view.create_alert("Non c'è nessuno studente con questa Matricola!")
            return

        aggiunto = self._model.iscriviStudente(studente, corso)
        if aggiunto:
            output = 'Studente aggiunto con successo'
        else:
            output = 'Studente già iscritto a questo corso'

        self._view.txt_result.controls.append(ft.Text(value=output))
        self._view.update_page()


