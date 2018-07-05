#!/usr/bin/python3


class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 10

    def latir(self):
        self.energia -= 1
        print('Woof Woof! Energia: {}'.format(self.energia))

    def andar(self):
        print('Andando...')
        self.energia -= 1

    def dormir(self):
        self.energia = 10
        print('\n' + '#'*40 + '''
        

            Energia recuperada! 
        
            Energia: {}

        '''.format(self.energia)+ '\n' + '#'*40 + '\n')

    def brincar(self):
        self.energia -= 1
        print('Joga bolinha... Energia: {}'.format(self.energia))

    def agradar(self):
        self.energia += 1
        print('Faz carinho... Energia: {}'.format(self.energia))



dog1 = Dog('Bilu', 2)

# print('Energia: {}'.format(dog1.energia))
# dog1.latir()
# dog1.andar()
# print('Energia: {}'.format(dog1.energia))
# dog1.dormir()

while True:
    opcao = int(input(''' Selecione sua próxima ação:
        1 - Latir
        2 - Brincar
        3 - Agradar
        4 - Dormir
        5 - Sair
            
        Opção: 
        '''))
    if dog1.energia == 0:
        print('Seu cachorro morreu! Game Over!')
        break
    elif opcao != 5:
        if opcao == 1:
            dog1.latir()
        elif opcao == 2:
            dog1.brincar()
        elif opcao == 3:
            dog1.agradar()
        elif opcao == 4:
            dog1.dormir()
    else:
        break