# ============================================
# DESAFIO 20
# ============================================
# Crie um programa que:
# - Leia o nome de 4 alunos
# - Mostre a ordem sorteada de apresentação
#
## ============================================
# DESAFIO 21
# ============================================
# Crie um programa que:
# - Abra um arquivo de áudio MP3
# - Toque esse áudio
#
# DICA:
# - Você vai precisar instalar uma biblioteca externa
# - Exemplo: pygame
# - O arquivo deve estar na mesma pasta do programa DICA:
# - Não é escolher um só
# - É embaralhar todos

from random import shufflel # Importa a função shuffle da biblioteca random
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do qurto aluno: ")
lista = [n1, n2, n3, n4] # Cria uma lista com os nomes dos alunos
shufflel(lista) # Embaralha a lista de alunos
print(f"A ordem de apresentação será {lista}")
