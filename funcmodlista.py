#!/usr/bin/python3

lista = ['a', 'b', 'c']

def alterar_lista(lista):
    for item in lista:
        indice = lista.index(item)
        lista[indice] = item + "\n"
    return lista

print(alterar_lista(lista))