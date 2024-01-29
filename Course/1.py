szukanaliczba = 50
zgadywanaliczba = 0

while zgadywanaliczba != szukanaliczba:
    zgadywanaliczba = int(input("Podaj liczbę:  "))
   
    if zgadywanaliczba == szukanaliczba: 
        print("brawo") 
     
    elif zgadywanaliczba < szukanaliczba:
        print("za mala")
    
    else: 
        print("za duza")
  
