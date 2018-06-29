#!/usr/bin/python3

with open('nomes.txt', 'a+') as arquivo:
    while True:
        nome = input('Digite um nome para escrita, ou digite sair para encerrar: ')
        if nome.strip().lower() != 'sair':
            arquivo.write(nome.title() + '\n')
        else:
            break
    print(arquivo.read())

# with open('nomes.txt', 'r') as arquivo:

        