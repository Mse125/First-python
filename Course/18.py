numbers = [1, -1, 20, -54, 24, -64]

def sum_numb():
    total = 0
    
    for number in numbers:
        if number > 0:
            total += number
            
    return total

print(sum_numb())
