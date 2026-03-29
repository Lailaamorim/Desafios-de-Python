# DESAFIO 06 – Dobro, Triplo e Raiz Quadrada
# Crie um programa que leia um número digitado pelo usuário.
# Em seguida, mostre na tela o dobro, o triplo e a raiz quadrada desse número.
#
# Exemplo:
# Digite um número: 9
# O dobro de 9 é 18
# O triplo de 9 é 27
# A raiz quadrada de 9 é 3

num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz = num ** 0.5
print(f"O dobro de {num} é {dobro}")
print(f"O triplo de {num} é {triplo}")
print(f"A raiz quadrada de {num} é {raiz}")