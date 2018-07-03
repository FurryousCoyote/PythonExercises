#!/usr/bin/python3

# Funcao simples
def boas_vindas(nome, idade):
    print('Oi sou o {} tenho {} anos'.format(nome,idade))

boas_vindas('joao', '25')

# Funcao simples, com o default nos parametros.
def boas_vindas2(nome='rogerio', idade='38'):
    print('Oi sou o {} tenho {} anos'.format(nome,idade))

boas_vindas2()

# Funcao simples, com o default nos parametros e com return.
def boas_vindas3(nome='rogerio', idade='38'):
    return 'Oi sou o {} tenho {} anos'.format(nome,idade)

a = boas_vindas3('Daniel', '68')
print(a)

def somar(x, y):
    return x + y

b = somar(3, 2)
print(b)