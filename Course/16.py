"""
def pole_prostokata(a, b):
    print(a * b) 
    
pole_prostokata(2, 5)


def pole_prostokata(a, b):
    return a * b

# print(5 * pole_prostokata(2, 8))

poleA = (5 * pole_prostokata(2, 8))
poleB = (5 * pole_prostokata(6, 12))

print("Twoje pole wynosi", poleA)
print(poleB)
"""

def dzielenie(a, b):
    if (b == 0):
        return
    
    return a / b

# print(dzielenie(10, 0))

dzielnieA = dzielenie(10, 2)

if (dzielnieA):
    print("Podzielono poprawnie", dzielnieA)
    
else:
    print("Cos poszlo nie tak")
    
    
    
    
