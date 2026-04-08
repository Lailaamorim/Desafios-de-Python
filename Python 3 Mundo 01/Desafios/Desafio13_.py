# DESAFIO 13 – Aumento de Salário
# Crie um programa que leia o salário de um funcionário.
# Em seguida, mostre o novo salário com 15% de aumento.
#
# Exemplo:
# Digite o salário do funcionário: 2000.00
# O novo salário com 15% de aumento é 2300.00
salario = float(input("Digite o salário do funcionario: "))
aumento =  salario * 0.15
valor_final = salario + aumento
print(f"O novo salário com 15% de aumento é R${valor_final} ")
