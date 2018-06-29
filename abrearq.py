#!/usr/bin/python3
# open('novo.txt', 'r')

#le linhas e imprime
with open('novo.txt', 'r') as arquivo:
    print(arquivo.read())

# Le linhas e adiciona em uma lista
with open('novo.txt', 'r') as arquivo:
    print(arquivo.readlines())

# Le apenas uma linha de cada vez
with open('novo.txt', 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())

# Le apenas uma linha de cada vez, usando o .seek(0) volta a primeira linha do arquivo
with open('novo.txt', 'r') as arquivo:
    print(arquivo.readline())
    arquivo.seek(0)
    print(arquivo.readline())