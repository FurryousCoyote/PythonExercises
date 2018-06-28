#!/usr/bin/python3


# Dicionario usa chaves
dicionario = {}
pessoas =  {'nome':'daniel', 'email':'daniel@daniel'}
print(pessoas['nome'])

#Dicionario dentro da lsita
pessoas2 = [
    {'nome':'daniel', 'idade':34},
    {'nome':'roberto', 'idade':54},
    {'nome':'josh', 'idade':4},
    {'nome':'patricia', 'idade':14},
    {'nome':'andressa', 'idade':31},
]

print(pessoas2[4]['idade'])

print(pessoas.keys())

for x in pessoas.values():
    print(x)

for x, y in pessoas.items():
    print (x, y)