#!/usr/bin/python3

nome = input("Qual o seu nome? ")
nome = nome.title()
nota1 = int(input("Qual a nota da sua primeira prova? "))
nota2 = int(input("Qual a nota da sua segunda prova? "))
calculanota = (nota1 + nota2) / 2
print("{}, sua média é {}".format(nome, calculanota))
