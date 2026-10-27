import random

def wypelnij_tablice(tablica):
    for i in range(50):
        tablica.append(random.randint(1, 100))


def szukaj_z_wartownikiem(tablica, szukana):
    tablica.append(szukana)  # dodanie wartownika
    i = 0

    while tablica[i] != szukana:
        i += 1

    if i == len(tablica) - 1:
        return -1  # nie znaleziono elementu

    return i


def main():
    tablica = []

    wypelnij_tablice(tablica)

    szukana = int(input("Podaj szukaną liczbę: "))

    pozycja = szukaj_z_wartownikiem(tablica, szukana)

    tablica.pop()  # usunięcie wartownika

    print("Zawartość tablicy:")
    print(", ".join(map(str, tablica)))

    if pozycja == -1:
        print("Nie znaleziono podanej liczby.")
    else:
        print("Znaleziono liczbę pod indeksem:", pozycja)


if __name__ == "__main__":
    main()