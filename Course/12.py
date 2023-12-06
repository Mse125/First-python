names = {"Seba", "Luki", "Arnold", "Zenon"}
numbers = {1,2,3,4,5,6}
 
nameLengt = { 
    name : len(name)
    for name in names
    if name.startswith("S")
}

print(nameLengt)

multiNumber = {
    number : number*number
    for number in numbers
}
print(multiNumber)
