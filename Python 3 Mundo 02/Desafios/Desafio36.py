# DESAFIO 036 – Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
#
# O programa vai perguntar:
# - valor da casa
# - salário do comprador
# - em quantos anos ele vai pagar
#
# Calcule o valor da prestação mensal.
# A prestação não pode exceder 30% do salário,
# senão o empréstimo será negado.
#
# Exemplo:
# Valor da casa: R$ 120000
# Salário do comprador: R$ 5000
# Quantos anos vai pagar: 30
#
# Empréstimo APROVADO!

print("="*30)
print("EMPRÉSTIMO BANCÁRIO")
print("="*30)

valor_casa = float(input("Insira o valor da casa: R$ "))
salario = float(input("Insira o seu salário: R$ "))
anos = int(input("Quantos anos vai pagar: "))
print()

prestacao = valor_casa / (anos * 12)
limite = salario * 30

print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos} anos,")
print(f"a prestação será de R$ {prestacao:.2f}")
print()

if prestacao <= limite: 
  print("Empréstimo APROVADO!")
else: 
  print("Empréstimo NEGADO")
