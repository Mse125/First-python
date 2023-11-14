'''
imiona = ["as", "ad", "af"]
  
# for imie in imiona: 
    # print(imie)
      
imiona[1] = "adf"
print(imiona)
print(imiona[1])

'''
 
imiona = ["Wojtek","Lukasz","Sebastian","Zbychu"]

'''
if ("Tobi" in imiona):
    print("eluwa Wojtek")
else: 
    print("Tobi wyjechał")
    
if (int(3) not in imiona):
    print("nie ma takiej liczby")
    
    
liczba = [4] + imiona
print(liczba)

'''
imie = input("Podaj imie: ")
imie = imie.capitalize()

if imie == "Zbychu" or imie == "Seba":
    print("masz dostęp")
else:
    print("brak dostępu")
