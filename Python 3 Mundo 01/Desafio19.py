# ============================================
# DESAFIO 19
# ============================================
# Crie um programa que:
# - Leia o nome de 4 alunos
# - Escolha um deles aleatoriamente
# - Mostre o nome do escolhido
#
# DICA:
# - Use listas
# - Use biblioteca de sorteio (random)

# Importa a função choice da biblioteca random
# Essa função serve para escolher um item aleatório de uma lista
from random import choice 
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("digite o nome do sgundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("digite o nome do quarto aluno: ")

lista = [n1, n2, n3, n4] # Cria uma lista com todos os nomes digitados
escolha = choice(lista)# Escolhe aleatoriamente um nome da lista
print(f"O aluno escolhido foi {escolha}")