#!/usr/bin/python3

numero = int(input("Digite um número: "))

resultado = []
resultado.append(numero)

if numero % 2 == 0:
    resultado.append('Par')
else:
    resultado.append('Impar')

print(resultado)