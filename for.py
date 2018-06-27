#!/usr/bin/python3

nomes = ['daniel', 'joao', 'maria', 'marcelo']

for nome in nomes:
    print(nome.title())

for x in range(55, 65):
    print(x)

num = int(input("Digite um numero"))

for x in range(num):
    if x % 2 == 0:
        print("{} par".format(x))
    else:
        print("{} impar".format(x))