#!/usr/bin/python3

linguagem = input('Qual a melhor linguagem? ')

if linguagem.strip().lower() == 'python':
    print('Você acertou!')
else:
    print('Você errou!')

linguagem2 = input('Qual a melhor linguagem? ')

if linguagem2 == 'python':
    print('Você acertou!')
elif linguagem2 == 'golang':
    print('Você quase acertou')
else:
    print('Você errou!')