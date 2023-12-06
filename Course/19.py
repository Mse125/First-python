
from enum import IntEnum
figury = IntEnum('figury', 'prostokata kwadratu trojkata trapezu')



def prostokat(a, b):
        if (b == 0):
            return
        
        return (a * b)

def kwadrat(a):
    if (a == 0): 
        return
    
    return (a * a)

def trojkat(a, h):
    if (a == 0) or (h == 0):
        return
       
    return ((a * h) / 2)


while(True):
    print("1. Policz powierzchnie prostokata: ")
    print("2. Policz powierzchnie kwadratu: ")
    print("3. Policz powierzchnie trojkata: ")
    print("4. Policz powierzchnie trapezu: ")
    print("5. Zakoncz: ")
    
    wybor = float(input("Co chcesz zrobić: "))
       
    if wybor == (figury.prostokata):
        a = float(input("podaj bok a: "))
        b = float(input("podaj bok b: "))
        print(prostokat (a, b))
        
        
    if wybor == (figury.kwadratu):
        a = float(input("podaj bok kwadratu: "))
        print(kwadrat (a)) 
        
        
    if wybor == (figury.trojkata):
        a = float(input("podaj bok a: "))
        h = float(input("podaj wysokosc h: "))
        print(trojkat(a, h)) 
