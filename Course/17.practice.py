
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
    
    wybor = input("Co chcesz zrobić: ")   
       
    if wybor == ("1"):
        a = int(input("podaj bok a: "))
        b = int(input("podaj bok b: "))
        print(prostokat (a, b))
        
        
    if wybor == ("2"):
        a = int(input("podaj bok kwadratu: "))
        print(kwadrat (a)) 
        
        
    if wybor == ("3"):
        a = int(input("podaj bok a: "))
        h = int(input("podaj wysokosc h: "))
        print(trojkat(a, h)) 
