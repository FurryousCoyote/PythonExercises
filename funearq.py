#!/home/developer/520-noturno/venv/bin/python3

# ler
# lista e escrever no arquivo

def escreverArquivo (arquivo, lista):
    try:
        with open (arquivo, 'a') as arq:
            arq.writelines(lista)
            return True
    except Exception as erro:
        return '{} Erro!!'.format(erro)

lista = []
while True:
    nome = input('Digite um nome a ser adicionado ao arquivo ou Next para ir a próxima etapa: ')
    if nome.lower().strip() != 'next':
        lista.append(nome + '\n')
    else:
        break
#print(lista)

arquivo = input('Digite o nome do arquivo a ser editado: ')

print(escreverArquivo(arquivo, lista))


