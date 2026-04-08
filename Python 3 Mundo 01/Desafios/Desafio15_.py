# DESAFIO 15
# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço total a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.
# Ao final, exiba o valor total a ser pago.
km = float(input("Quantos KM foram percorridos? "))
dias = int(input("Quantos dias o carro foi alugado? "))

total = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${total:.2f}")