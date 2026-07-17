# ==========================================
# DESAFIO 52
# ==========================================

# O QUE É UM NÚMERO PRIMO?
#
# Um número primo é aquele que possui
# exatamente 2 divisores.
#
# Ele só pode ser dividido:
#
# 1. Por 1.
# 2. Por ele mesmo.
#
# Se existir qualquer outro divisor,
# ele NÃO é primo.

# ------------------------------------------
# EXEMPLOS DE NÚMEROS PRIMOS
# ------------------------------------------

# 2  -> Primo
# 3  -> Primo
# 5  -> Primo
# 7  -> Primo
# 11 -> Primo
# 13 -> Primo
# 17 -> Primo
# 19 -> Primo

# ------------------------------------------
# EXEMPLOS DE NÚMEROS QUE NÃO SÃO PRIMOS
# ------------------------------------------

# 4
# Pode ser dividido por:
# 1, 2 e 4
#
# Como possui mais de dois divisores,
# NÃO é primo.

# 6
# Pode ser dividido por:
# 1, 2, 3 e 6
#
# NÃO é primo.

# 9
# Pode ser dividido por:
# 1, 3 e 9
#
# NÃO é primo.

# 10
# Pode ser dividido por:
# 1, 2, 5 e 10
#
# NÃO é primo.

# ==========================================
# COMO DESCOBRIR SE UM NÚMERO É PRIMO?
# ==========================================

# Imagine que o usuário digitou o número 7.

# Você precisa verificar:
#
# 7 ÷ 1
# 7 ÷ 2
# 7 ÷ 3
# 7 ÷ 4
# 7 ÷ 5
# 7 ÷ 6
# 7 ÷ 7

# Depois pergunte:

# Em quais dessas divisões o resto foi zero?

# Apenas:

# 7 ÷ 1 = 7
# 7 ÷ 7 = 1

# Só existem dois divisores.

# Então:
# O número é primo.

# ==========================================
# OUTRO EXEMPLO
# ==========================================

# Número: 12

# Testando:

# 12 ÷ 1 ✔
# 12 ÷ 2 ✔
# 12 ÷ 3 ✔
# 12 ÷ 4 ✔
# 12 ÷ 5 ✘
# 12 ÷ 6 ✔
# ...
# 12 ÷ 12 ✔

# Existem vários divisores.

# Então:
# 12 NÃO é primo.

# ==========================================
# ENUNCIADO
# ==========================================

# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

# ------------------------------------------
# EXEMPLO DE EXECUÇÃO NO TERMINAL
# ------------------------------------------

# Digite um número: 13
#
# O número 13 é PRIMO.

# ------------------------------------------
# OUTRO EXEMPLO
# ------------------------------------------

# Digite um número: 18
#
# O número 18 NÃO é PRIMO.

# ------------------------------------------
# O QUE O PROGRAMA DEVE FAZER
# ------------------------------------------

# Ler um número inteiro.
#
# Verificar por quais números ele pode
# ser dividido sem deixar resto.
#
# Contar quantos divisores ele possui.
#
# Se possuir exatamente 2 divisores,
# ele é primo.
#
# Caso contrário,
# ele não é primo.