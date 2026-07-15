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

# ==========================================
# DESAFIO 05 - RESOLUÇÃO DO PROFESSOR
# ==========================================

# OBJETIVO
#
# Ler um número inteiro
# e mostrar o seu antecessor
# e o seu sucessor.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Pedir um número inteiro.

# PASSO 2
# Guardar o número em uma variável.

# PASSO 3
# Mostrar o antecessor
# calculando "número - 1".

# PASSO 4
# Mostrar o sucessor
# calculando "número + 1".

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Não é obrigatório criar uma variável
# para guardar o antecessor e o sucessor.

# Se o cálculo for simples e for usado
# apenas uma vez,
# ele pode ser feito diretamente no print().

# Em vez de:

# antecessor = numero - 1
# sucessor = numero + 1

# Pode fazer diretamente:

# numero - 1
# numero + 1

# dentro do print().

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ int()
# ✔ variável
# ✔ operadores (+) e (-)
# ✔ print()