# DESAFIO 27:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#
# Exemplo:
# Entrada: Ana Maria de Souza
# Saída:
# Primeiro: Ana
# Último: Souza

# Pede para o usuário digitar o nome completo
# .strip() remove espaços extras no início e no final
nomes = input("Digite seu nome: ").strip()

# .split() divide o nome em partes, separando por espaços
# Ex: "João Silva Souza" → ["João", "Silva", "Souza"]
nome = nomes.split()

# Exibe uma mensagem de boas-vindas com o nome completo
print(f"Muito Prazer {nomes}")

# Mostra o primeiro nome (primeiro elemento da lista)
# [0] acessa a primeira posição da lista
print(f"Seu primeiro nome é {nome[0]}")

# Mostra o último nome (último elemento da lista)
# [-1] acessa o último item da lista
print(f"Seu último nome é {nome[-1]}")