#!/usr/bin/python3

from datetime import datetime

users = ['Daniel', 'Pedro', 'Maria', 'Joao']

while True:
    try:
        num = (input('''
        USER
        0 - Daniel
        1 - Pedro
        2 - Maria
        3 - João
        4 - Sair

        Digite um usuário:
        '''))
        if num == 's':
            break
        
        #num = int(num)
        print('O usuário {} esta logado'.format(users[int(num)]))
    except IndexError as error:
        d = datetime.now()
        with open('python.log', 'a') as arquivo:
            result= "{}, {}".format(error, d.strftime("%Y-%m-%d %H:%M:%S\n"))
            arquivo.write(result)
        break
    except KeyboardInterrupt as error:
        d = datetime.now()
        with open('python.log', 'a') as arquivo:
            result= "Finalizado pelo usuario - {}".format(d.strftime("%Y-%m-%d %H:%M:%S\n"))
            arquivo.write(result)
        break