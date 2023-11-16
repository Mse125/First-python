listagosci = {
    ('Aro', 50, 'mezczyzna'),
    ('Roman', 43, 'mezczyzna'),
    ('Sofia', 65, 'kobieta')
}

listagosci2 = { 
    ('Aro', 50, 'mezczyzna'),
    ('r', 43, 'mezczyzna'),
    ('s', 65, 'kobieta')
} 

print(listagosci)
listagosci3 = listagosci | listagosci2
print(listagosci3)