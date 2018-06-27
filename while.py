#!/usr/bin/python3

""" contador = 1
while contador <= 10:
    print(contador)
    contador += 1


soma = 0
while True:
    num = int(input("digite um numero ou 0 para sair"))
    if num == 0:
        break
    soma += num
print('total: {}'.format(soma)) """

nomes = []

while True:
    nome = input("Digite um nome para adicionar a lista ou 'sair' para encerrar: ")
    if nome.lower() != 'sair':
        nomes.append(nome.title())
    else:
        break

    print(nomes)

name = 'Marcelo'
print(True if name.lower() == 'marcelo' else 'False')