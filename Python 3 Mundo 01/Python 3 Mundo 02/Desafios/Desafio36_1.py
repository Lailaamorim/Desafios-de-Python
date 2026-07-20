casa = float(input("Valor da casa: R$ "))
salario = float (input("Salário do comprador: "))
anos = int(input("Em quantos anos vai pagar?"))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Empréstimo negado!")

    # ==========================================
# DESAFIO 36 - APROVANDO EMPRÉSTIMO
# ==========================================

# OBJETIVO
#
# Verificar se um empréstimo
# pode ser aprovado
# com base no salário do comprador.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler o valor da casa,
# o salário do comprador
# e a quantidade de anos
# para pagar o financiamento.

# PASSO 2
# Calcular o valor
# da prestação mensal.

# PASSO 3
# Calcular 30% do salário
# do comprador.

# PASSO 4
# Comparar o valor da prestação
# com o limite de 30% do salário.

# PASSO 5
# Se a prestação for menor
# ou igual ao limite,
# aprovar o empréstimo.

# PASSO 6
# Caso contrário,
# negar o empréstimo.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Resolver um problema
# utilizando cálculos
# e uma estrutura de decisão.

# Antes de comparar,
# é necessário calcular
# os valores que serão analisados.

# Utilizar o if/else
# para tomar uma decisão
# com base em uma condição.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ int()
# ✔ variável
# ✔ operadores (*), (/)
# ✔ if
# ✔ else
# ✔ operador de comparação (<=)
# ✔ print()