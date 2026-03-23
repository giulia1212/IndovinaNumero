import random

# implementa in una singola classe tutta la logica che finora avevamo fatto nei laboratori
# tutta la parte di interazione con i dati, in questo caso tutta la parte che regola il comportamento del gioco
class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._tentativiMax = 6
        self._tentativiRimanenti = self._tentativiMax
        self._daIndovinare = None

    def reset(self):
        """
        Questo metodo resetta lo stato del gioco.
        Imposta il numero segreto a un valore randomico fra 0 e Nmax
        e ripristina il numero di tentativi rimanenti.
        """
        self._daIndovinare = random.randint(0, self._Nmax)   # genera un numero ramdomico tra 0 e 100
        self._tentativiRimanenti = self._tentativiMax           # ripristina numero di vite nel gioco
        print(self._daIndovinare)

    def play(self, tentativo):
        """
        Questo metodo riceve come argomento un valore intero che sarà il tentativo (num inserito) del giocatore
        e lo confronta con il numero da indovinare
        :return:
        -1 se il numero da indovinare è più piccolo del tentativo
        0 se il tentativo è uguale al segreto
        1 se il segreto è più grande del tentativo
        2 se non ho più tentativi disponibili
        """

        self._tentativiRimanenti -= 1

        if tentativo == self._daIndovinare:
            """Ho vinto!!!"""
            return 0

        if self._tentativiRimanenti == 0:
            """Allora non ho più vite, non posso più giocare"""
            return 2

        if tentativo > self._daIndovinare:
            """Il tentativo dell'utente è più grande del numero da indovinare """
            return -1
        else:
            return 1

    @property
    def Nmax(self):
        return self._Nmax

    @property
    def tentativiMax(self):
        return self._tentativiMax

    @property
    def tentativiRimanenti(self):
        return self._tentativiRimanenti

    @property
    def daIndovinare(self):
        return self._daIndovinare

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(20))
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(70))
    print(m.play(80))
    print(m.play(60))
    print(m.play(50))
