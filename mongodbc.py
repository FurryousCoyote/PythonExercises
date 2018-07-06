#!/usr/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['pessoas']
except Exception as e:
    print("Erro {}".format(e))

#dados = db.pessoas.find_one({'_id':1})
dados = db.pessoas.find()
# usa list comprehension para adicionar todos objetos em uma lista
dados = [x for x in dados]

print(dados)

#db.pessoas.insert({'_id':5, 'nome':'Fulano'})
db.pessoas.remove()


