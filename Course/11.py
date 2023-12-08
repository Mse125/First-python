liczby = [1, 2, 3, 4, 5, 6]

element = [element**2 
           for element in liczby]  
print(element)

parzyste = [(element % 2 == 0) for element in liczby]
print(parzyste) 

parzyste2 = [element
             for element in liczby
             if (element % 2 == 0)
             ]
print(parzyste2)

# 1. Co zrobic na elemencie | for element in lista | warunek oparty na elmencie
