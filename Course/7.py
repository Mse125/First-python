ratings1 = {
    "Aro": (1,4,3,2,6),
    "Tomasz": (5,3,2,6,4)
   }

people1 = [
    {'id': 'dsfsdfsdf', 'name': 'seba', 'age': 54},
    {'id': 'dfhgkkkkk', 'name': 'tom', 'age': 66},
    {'id': 'gfhfgjfgj', 'name': 'fot', 'age': 77},
    {'id': 'dfbdfhdfh', 'name': 'ali', 'age': 88}    
        ]

people2 = {
    "id1": {'dsfsdfsdf': 11, 'name': 'seba', 'age': 54},
    "id2": {'dfhgkkkkk': 22, 'name': 'tom', 'age': 66},
    "id3": {'gfhfgjfgj': 33, 'name': 'fot', 'age': 77},
    "id4": {'dfbdfhdfh': 55, 'name': 'ali', 'age': 88}    
        }

'''
for dictionary in people1:
    for value in dictionary:
        print(value,":", dictionary[value])
'''

"""""
for key in people2:
    print("ID:", key)
    for key2 in people2[key]:
        print(key2,people2[key][key2])
"""""

for id, dictionary in people2.items():
    print("identyfikator", id)
    for key in dictionary:
        print(key, dictionary[key])
