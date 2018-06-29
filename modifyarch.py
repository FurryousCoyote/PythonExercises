#!/usr/bin/python3

with open('nomes2.txt', 'r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{}-{}\n'.format(linha.strip(), cont))
    cont += 1

print(alterado)
y = 0

with open('nomenovo.txt', 'w+') as arquivo:
    for x in alterado:
        arquivo.write(alterado[y])
        y += 1

