#!/usr/bin/python3


nome_arquivo = input("Digite o nome do arquivo a ser exibido: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        print(arquivo.read())
except Exception as error:
    print("Arquivo digitado não encontrado - {}".format(error))