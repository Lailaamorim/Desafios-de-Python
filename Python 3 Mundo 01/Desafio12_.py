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