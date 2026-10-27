import random
board = []
for i in range (50): # jawne 50 elementów
    random_integer = random.randint(1, 100) #losowanie liczby z zakresu od 1 do 100
    board.append(random_integer) # wprowadzanie losowych liczb do tablicy

szukana = int(input("Podaj szukany element:"))    



if szukana in board: #szukanie elementu w tabliczy 
    print("znalazłem")
    pozycja = board.index(szukana) #szukanie pozycji elementu w tabliczy
    print("Na pozycji",pozycja)
else:
    print("brak takiego elementu")