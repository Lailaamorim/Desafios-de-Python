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

# ==========================================
# DESAFIO 13
# ==========================================

# OBJETIVO
#
# Calcular o novo salário
# com 15% de aumento.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler o salário do funcionário,
# guardando-o em uma variável.

# PASSO 2
# Calcular o valor do aumento,
# correspondente a 15% do salário.

# PASSO 3
# Somar o aumento
# ao salário original.

# PASSO 4
# Mostrar o novo salário.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Para calcular um aumento,
# multiplica-se o valor
# pela porcentagem em decimal.

# Exemplo:

# 15% = 0.15

# Depois,
# soma-se o aumento
# ao valor original.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (*) e (+)
# ✔ print()