slownik = {} 

while(True):
    print("1. Dodaj definicje")
    print("2. Wyszukaj definicje")
    print("3. Usun definicje")
    print("4. Zakoncz program")
 
    wybor = input("Co chcesz zrobic: ")

    if (wybor == "1"):
        klucz = input("Podaj nazwe definicji: ")
        definicja = input("Podaj tresc: ")
        slownik[klucz] = definicja
        print("Defnicja dodana pomyslnie")
    elif (wybor == "2"):
        klucz = input("Podaj szukana definicje: ")
        if klucz in slownik:
            print(definicja[klucz])
        else:
            print("Nie znaleziono definicji", klucz)
    elif (wybor == "3"):
        klucz = input("Jaka definicje chcesz usunac: ")
        if klucz in slownik:
            del slownik[klucz]
            print("Usunieto definicje o nazwie", klucz)
        else:
            print("Definicja o nazwie", klucz, "nie istnieje")
    elif (wybor == "4"):
        print("Program został zakonczony")
        break
