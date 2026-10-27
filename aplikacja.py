#IMPORT POTRZEBNYCH RZECZY 
import tkinter as tk

class Aplikacja:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title("Testowa aplikacja") #tekst który jest nazwą aplikacji/ tytułem
        self.okno.geometry("600x400") #rozmiar
        self.okno.configure(bg="red") #kolor tła

okno = tk.Tk() # tworzy główne okno aplikacji.
aplikacja = Aplikacja(okno) 
okno.mainloop() # uruchamia pętlę obsługi zdarzeń, dzięki której okno pozostaje otwarte