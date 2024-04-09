import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        '''
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )
        '''
        # Row 1
        self.selezionaCorsi = ft.Dropdown(label='corso', width=780)
        self.popolaCorsi()
        self.cercaIscritti_btn = ft.ElevatedButton(text='Cerca iscritti', on_click=self._controller.handle_iscritti)
        row1 = ft.Row([self.selezionaCorsi, self.cercaIscritti_btn],
                       alignment=ft.MainAxisAlignment.CENTER)

        # Row 2
        self.selezionaMatricola = ft.TextField(label='matricola')
        self.nomeStudente = ft.TextField(label='nome', read_only=True)
        self.cognomeStudente = ft.TextField(label='cognnome', read_only=True)
        row2 = ft.Row([self.selezionaMatricola, self.nomeStudente, self.cognomeStudente],
                       alignment=ft.MainAxisAlignment.CENTER)

        # Row 3
        self.cercaStudente_btn = ft.ElevatedButton(text='Cerca studente')
        self.cercaCorsi_btn = ft.ElevatedButton(text='Cerca corsi')
        self.iscrivi_btn = ft.ElevatedButton(text='Iscrivi')
        row3 = ft.Row([self.cercaStudente_btn, self.cercaCorsi_btn, self.iscrivi_btn],
                      alignment=ft.MainAxisAlignment.CENTER)
        '''
        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        '''
        self._page.add(row1, row2, row3)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def popolaCorsi(self):
        for corso in self.controller._model.listaCorsi:
            self.selezionaCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
