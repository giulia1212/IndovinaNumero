import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):       # qui andiamo a scrivere tutte le definizioni degli oggetti grafici che vogliamo utilizzare nella nostra applicazione
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        # campo numero massimo
        self._txtNmax = ft.TextField(label="Numero Max",     # casella di testo che contiene il numero massimo
                                     value=self._controller.getNmax(),
                                     disabled=True)    # casella di testo di cui non posso modificare il contenuto

        # campo num tentativi massimo
        self._txtTentativiMax = ft.TextField(label="Num tentativi max",
                                    value=self._controller.getTentativiMax(),
                                    disabled=True)

        # campo tentativi rimanenti
        self._txtTentativiRimanenti = ft.TextField(label="Num tentativi rimanenti",
                                                   disabled=True)

        # aggiungo i tre campi alla riga
        self._row1 = ft.Row(controls=[self._txtNmax, self._txtTentativiMax, self._txtTentativiRimanenti])

        # campo del valore inserito dall'utente
        self._txtInTentativo = ft.TextField(label="Valore")    # disabled = False è sottointeso

        # creo i pulsanti
        #------- Pulsante di reset - inizio nuova partita
        self._bntReset = ft.ElevatedButton(text= "Nuova Partita",
                                           on_click= self._controller.reset)  # ATTENZIONE devi passare il NOME del metodo NON LA CHIAMATA AL METODO
                                                                              # quindi reset NON reset()
        # ------- Pulsante per giocare - lo schiaccio dopo aver inserito il valore per provare a indovinare
        self._bntPlay = ft.ElevatedButton(text="Indovina",
                                           on_click=self._controller.play)

        # aggiungo il campo valore e bottoni a una riga
        self._row2 = ft.Row(controls=[self._txtInTentativo, self._bntReset, self._bntPlay])

        # devo creare anche un contenitore di strighe per tutte le stampe che riguardano il gioco
        self._lvOut = ft.ListView(expand=True)        # expand = True è per far si che io possa scrollarlo

        # aggiungo le righe e il box di testo alla pagina
        self._page.add(self._row1, self._row2, self._lvOut)
        self._page.update()

    # metodo che setta il controller
    def setController(self,controller):     # va a dire al nostro view "questo è il tuo controller" e al nostro controller "questo è il tuo view"
        self._controller = controller       # in modo che le due classi si conoscano a vicenda

    def update(self):           # aggiorna l'interfaccia grafica
        self._page.update()