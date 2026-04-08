# DESAFIO 23:
# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.
#
# Exemplo:
# Digite o número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = int(input("Digite um número de 0 a 9999: "))
u = num % 10 # Pega o último dígito (resto da divisão por 10)
d = (num // 10) % 10 # Remove o último dígito (// 10) e pega o novo último
c = (num // 100) % 10 # Remove os dois últimos dígitos e pega o próximo
m = (num // 1000) % 10 # Remove os três últimos dígitos e pega o próximo

print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")