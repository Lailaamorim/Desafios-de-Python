# DESAFIO 10 – Conversor de Moeda
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira.
# Em seguida, mostre quantos dólares ela pode comprar, considerando a taxa de câmbio atual.
#
# Exemplo:
# Digite quanto dinheiro você tem: 100.00
# Considerando o dólar a R$5.00
# Você pode comprar 20.00 dólares
valor = float(input("Digite quando dinheiro você tem: "))
dolar = valor / 5.24
print(f"Você pode comprar: {dolar:.2f} dólares")
# Consegui fazer igual ao do professor(❁´◡`❁)