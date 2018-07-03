#!/usr/bin/python3

try:
    num = int(input("Digite um numero: "))
    print(num)
except ValueError as erro:
    print("Não é um inteiro: {}".format(erro))

# Trata qualquer tipo de Exception, não necessariamente um em específico.
except Exception as error:
    print("não é um inteiro: {}".format(error))