#!/usr/bin/python3


var = lambda x: x*2
print(var(4))

fruta = {'nome':'laranja', 'valor': 5.55, 'qtd': 26}
var2 = lambda x, y: x * y

print(var2(fruta['valor'], fruta['qtd']))