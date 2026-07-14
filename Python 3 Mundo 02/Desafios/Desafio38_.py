# DESAFIO 038 – Comparando Números
# Faça um programa que leia dois números inteiros.
# Em seguida, mostre na tela qual valor é maior
# ou se os dois números são iguais.
#
# Exemplo:
# Digite o primeiro número: 8
# Digite o segundo número: 15
# O segundo valor é maior

# Exemplo:
# Digite o primeiro número: 10
# Digite o segundo número: 10
# Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print()

if num1 > num2 :
  print("O primeiro número é maior")
elif num2 > num1:  
  print("O segundo número é maior") 
else:
  print("Não existe valor maior, os dois são iguais")  