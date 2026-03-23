from view import View
from model import Model
import flet as ft

# classe che contiene solo metodi che sono i metodi che interagiscono con il view
# e interagiscono con il modello
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    def getNmax(self):              # devo scrivere questo metodo perchè model e view non possono comunicare
        return self._model.Nmax     # controller defe fare da tramite tra i due

    def getTentativiMax(self):
        return self._model.tentativiMax

    # ATTENZIONE devi sempre mettere "e" (sarebbe l'evento che ha generato la pressione di quel pulsante)
    # come parametro dei metodi che sono associati ad un pulsante
    # altrimenti ti dà errore sul numero di argomenti
    def reset(self, e):
        self._model.reset()     # resetto lo stato del gioco LATO MODELLO
        self._view._txtTentativiRimanenti = self._model.tentativiRimanenti  # il numero di tentativi rimanenti torna quello iniziale
        self._view._lvOut.controls.clear()  # pulisco la box che contiene il testo
        self._view._lvOut.controls.append(ft.Text("Inizia il gioco! Indovina a quale numero sto pensando."))
        self._view.update()  # ogni volta che ho modificato nel controller qualcosa che ha a che fare con l'interfaccia grafica devo fare questo
                             # cioè aggiornare la pagina

    def play(self, e):
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore! Devi inserire un valore numerico"))
            # ho aggiornato l'interfaccia grafica quindi devo aggiornare il view
            self._view.update()
            return

        res = self._model.play(tentativo)

        if res == 0:
            """Ho vinto!"""
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto! Il valore corretto era: {tentativo}", color="green"))
            self._view.update()
            return

        elif res == 2:
            """Non ho più vite"""
            self._view._lvOut.controls.append(ft.Text(f"Hai perso! Il valore corretto era: {self._model.daIndovinare}", color="red"))
            self._view.update()
            return

        elif res == -1:
            """Il numero da indovinare è più piccolo del tentativo dell'utente"""
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il numero da indovinare è più piccolo di: {tentativo}"))
            self._view.update()
            return

        else:
            """Il numero da indovinare è più grande del tentativo dell'utente"""
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il numero da indovinare è più grande di: {tentativo}"))
            self._view.update()
            return

