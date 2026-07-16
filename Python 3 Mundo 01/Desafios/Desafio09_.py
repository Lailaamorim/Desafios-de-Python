# DESAFIO 09 – Tabuada
# Crie um programa que leia um número inteiro digitado pelo usuário.
# Em seguida, mostre na tela a sua tabuada de multiplicação.
#
# Exemplo:
# Digite um número: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

num = int(input("Digite um número para ver sua tabuada: "))
print('='*20)
print(f" {num:2d} X 0 = {num*0}")
print(f" {num:2d} X 1 = {num*1}")
print(f" {num:2d} X 2 = {num*2}")
print(f" {num:2d} X 3 = {num*3}")
print(f" {num:2d} X 4 = {num*4}")
print(f" {num:2d} X 5 = {num*5}")
print(f" {num:2d} X 6 = {num*6}")
print(f" {num:2d} X 7 = {num*7}")
print(f" {num:2d} X 8 = {num*8}")
print(f" {num:2d} X 9 = {num*9}")
print(f" {num:2d} X 10 = {num*10}")
print('='*20)

# Consegui fazer igual ao do professor(❁´◡`❁)
# ==========================================
# DESAFIO 09
# ==========================================

# OBJETIVO
#
# Mostrar a tabuada de multiplicação
# de um número informado pelo usuário.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler um número inteiro,
# guardando-o em uma variável.

# PASSO 2
# Multiplicar esse número
# pelos valores de 0 até 10.

# PASSO 3
# Mostrar o resultado
# de cada multiplicação em formato de tabuada.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar o operador (*)
# para realizar as multiplicações.

# Utilizar f-strings
# para montar a tabuada de forma organizada.

# Utilizar a formatação :2d
# para alinhar os números na impressão.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ int()
# ✔ variável
# ✔ operador (*)
# ✔ f-string
# ✔ print()