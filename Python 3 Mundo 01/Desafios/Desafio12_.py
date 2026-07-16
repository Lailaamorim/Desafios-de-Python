# DESAFIO 12 – Desconto de Produto
# Crie um programa que leia o preço de um produto.
# Em seguida, mostre o novo preço com 5% de desconto.
#
# Exemplo:
# Digite o preço do produto: 100.00
# O novo preço com 5% de desconto é 95.00

num = float(input("Digite o preço do produto: "))
desconto = num * 0.05
valor_final = num - desconto 
print(f"O novo preço com 5% de desconto é {valor_final}")

# ==========================================
# DESAFIO 12
# ==========================================

# OBJETIVO
#
# Calcular o valor de um produto
# com 5% de desconto.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler o preço do produto,
# guardando-o em uma variável.

# PASSO 2
# Calcular o valor do desconto
# correspondente a 5% do preço.

# PASSO 3
# Subtrair o desconto
# do preço original.

# PASSO 4
# Mostrar o novo preço do produto.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Para calcular uma porcentagem,
# multiplica-se o valor
# pela porcentagem em decimal.

# Exemplo:

# 5% = 0.05

# Depois,
# subtrai-se o desconto
# do valor original.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (*) e (-)
# ✔ print()