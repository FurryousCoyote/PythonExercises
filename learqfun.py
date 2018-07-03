#!/home/developer/520-noturno/venv/bin/python3

def abre_arquivo (arquivo):
    try:
        with open (arquivo, 'r') as arq:
            return arq.readlines()
    except Exception as erro:
        return "{} Arquivo não encontrado!".format(erro)

arquivo = input('Digite o nome do arquivo a ser aberto: ')

print(abre_arquivo(arquivo))


