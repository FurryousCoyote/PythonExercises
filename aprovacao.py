#!/usr/bin/python3

nome = input("Qual o seu nome? ")
nome = nome.title()
nota1 = float(input("Qual a nota da sua primeira prova? "))
nota2 = float(input("Qual a nota da sua segunda prova? "))

calculanota = (nota1 + nota2) / 2

if calculanota  >= 7:
    print("{}, sua média é {} - Você foi aprovado!".format(nome, calculanota))
elif calculanota >= 6 and calculanota < 7:
    print("{}, sua média é {} - Você esta de recuperação!".format(nome, calculanota))
else:
    print("""
        Ei! {},
        sua média é {}
        Você foi reprovado!
        """.format(nome, calculanota))

'''
print('a')
a.k.a. gambiarra para comentários
'''