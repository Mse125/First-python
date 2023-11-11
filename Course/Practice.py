slownik= {}
 
while(True):
    print("1. Pokaz slownik: ")
    print("2. Znajdz definicje: ")
    print("3. Dodaj definicje: ")
    print("4. Usun definicje: ")
    print("5. Zakoncz: ")

     
    wybor = input("Co chesz zrobić: ")
    
    if wybor == ("1"):
        print(slownik)
        
    if wybor == ("2"):
        klucz = input("Podaj szukana definicje: "),
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print("Podana definicja nie istnieje")                          
    
    if wybor == ("3"):
        klucz = input("Podaj definicje: "),
        definicja = input("Podaj tresc definciji: "),
        slownik[klucz] = definicja
        print("Dodano definicje")
        
    if wybor == ("4"):
        klucz = input("Podaj definicje do usuniecia: "),
        if klucz in slownik:
            del slownik[klucz]
            print("Definicja usunieta")
        else:
            print("Definicja", klucz, "nie istnieje")
            
    if wybor == ("5"):
        print("Program zakonczony")
        break
    
