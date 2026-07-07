# DESAFIO 043 – Índice de Massa Corporal

# Desenvolva uma lógica que leia o peso
# e a altura de uma pessoa, calcule seu
# IMC e mostre seu status, de acordo
# com a tabela abaixo:
#
# - Abaixo de 18.5:
#   Abaixo do Peso
#
# - Entre 18.5 e 25:
#   Peso Ideal
#
# - 25 até 30:
#   Sobrepeso
#
# - 30 até 40:
#   Obesidade
#
# - Acima de 40:
#   Obesidade Mórbida

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

print(f"\nSeu IMC é {imc:.2f}")

if imc < 18.5:
    print("Status: Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Status: Peso ideal")
elif imc >= 25 and imc < 30:
    print("Status: Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")