#!/usr/bin/python3

""" 
frutas = {'Fruta':'Maça', 'Valor':'2', 'Fruta':'Pera', 'Valor':'3'}

# print(frutas.keys())

for x, y in frutas.items():
    print(x, y) """

frutas = [
    {'fruta':'laranja', 'valor':2.0, 'qtd':10},
    {'fruta':'abacaxi', 'valor':5.55, 'qtd':20},
    {'fruta':'uva', 'valor':4.5, 'qtd':2},
    {'fruta':'melancia', 'valor':7.0, 'qtd':4},
    {'fruta':'morango', 'valor':5.0, 'qtd':11},
]

# faturamento = 0
for fruta in frutas:
    faturamento = fruta['valor'] * fruta['qtd']
    




""" frutas2 = []
for fruta in frutas:
    fruta['valor'] += fruta['valor'] * 0.1
    frutas2.append(fruta)

print(frutas2) """