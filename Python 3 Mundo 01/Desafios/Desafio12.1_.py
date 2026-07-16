produto = float(input("Digite o preço do produto: "))
desconto = produto - (produto * 0.05) 
print(f"O produto que custava {produto} na promoção fica {desconto}")

# ==========================================
# DESAFIO 12 - RESOLUÇÃO DO PROFESSOR
# ==========================================

# OBJETIVO
#
# Calcular o novo preço
# de um produto com 5% de desconto.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler o preço do produto,
# guardando-o em uma variável.

# PASSO 2
# Calcular o novo preço,
# subtraindo 5% do valor original.

# PASSO 3
# Mostrar o preço original
# e o novo preço com desconto.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Não é obrigatório criar uma variável
# apenas para guardar o valor do desconto.

# O cálculo pode ser feito diretamente
# na expressão que calcula o preço final.

# Isso deixa o código mais enxuto.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (*) e (-)
# ✔ print()