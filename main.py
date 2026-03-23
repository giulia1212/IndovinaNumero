import flet as ft
from controller import Controller
from view import View

def main(page: ft.Page):
    v = View(page)          # classe che definisce l'interfaccia grafica
    c = Controller(v)       # classe che farà parlare il view con il modello
    v.setController(c)      # fa parlare il view con il controller
    v.caricaInterfaccia()   # metodo della view all'interno del quale noi scriveremo tutti i controlli della nostra interfaccia grafica

ft.app(target=main)