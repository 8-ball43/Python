import tkinter as tk 

class Aplikacja:
    def  __init__(self, okno):
        self.okno = okno
        self.okno.title("Wprowadzanie danych do paszportu. Wykonał: 0000")
        self.okno.geometry("600x400")
        self.okno.configure(bg="#ADD8E6")

        self.etykieta = tk.Label(
            okno,
            text="Numer",
            bg="#ADD8E6",
            fg="#000000",
            font=("Arial", 12)
        )
        self.etykieta.place(x=30, y=30)

        # Pole do wpisywania tekstu
        self.input = tk.Entry(okno, font=("Arial", 12))
        self.input.place(x=200, y=30, width=200)


okno = tk.Tk()
aplikacja = Aplikacja(okno)
okno.mainloop() 