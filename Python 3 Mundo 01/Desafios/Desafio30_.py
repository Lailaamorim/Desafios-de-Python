# ==================================================
# DESAFIO 30
# ==================================================

# Crie um programa que leia um número inteiro

# E mostre na tela se ele é:
# PAR ou ÍMPAR

# ==================================================
# EXEMPLOS DE FUNCIONAMENTO
# ==================================================

# Um número é PAR quando é divisível por 2
# Um número é ÍMPAR quando não é divisível por 2

num = int(input("Digite um número inteiro: "))

# verifica se o número é divisível por 2
if num % 2 == 0:
    # se o resto da divisão por 2 for 0, o número é par
    print("✅ O número é PAR — Ele pode ser dividido por 2 sem deixar resto.")
else:
    # caso contrário, o número é ímpar
    print("🔢 O número é ÍMPAR — A divisão por 2 deixa resto.")