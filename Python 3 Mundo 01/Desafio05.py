# DESAFIO 05 
# – Sucessor e Antecessor
# Crie um programa que leia um número inteiro digitado pelo usuário.
# Em seguida, mostre na tela qual é o seu antecessor e o seu sucessor.
#
# Exemplo:
# Digite um número: 10
# O antecessor de 10 é 9
# O sucessor de 10 é 11

num = int(input("Digite um número: "))
ant = num - 1
suce = num + 1
print(f"O Antecessor de {num} é {ant} o e o seu sucessor é {suce}")
