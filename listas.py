#!/usr/bin/python3

nomes = ['Daniel', 'Maria', 'Jose', 'Joao']

copia = nomes[:] #necessário adicionar : indice, caso contrário a variável só referencia a lista original.

nomes.append('Marcelo')

print(nomes)
print(copia)

nomes.append([1, 2, 3])

""" print(type(nomes[-1]))
print(nomes)
print(nomes[-2])
print(nomes[-1][0])

nomes.insert(0, 'Richard')
print(nomes)
nomes.pop() #remove o ultimo item da lista
nomes.remove('Marcelo') """

numeros = list(range(100))
print(numeros[38:66])

#Também válido para strings
if 66 in numeros:
    print('SIM')
else:
    print('NÃO')