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

  # ==========================================
# DESAFIO 38
# ==========================================

# OBJETIVO
#
# Comparar dois números inteiros
# e informar qual deles é maior
# ou se ambos são iguais.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler dois números inteiros,
# guardando cada um em sua variável.

# PASSO 2
# Comparar o primeiro número
# com o segundo.

# PASSO 3
# Se o primeiro for maior,
# informar que ele é o maior.

# PASSO 4
# Caso contrário,
# verificar se o segundo
# é maior que o primeiro.

# PASSO 5
# Se o segundo for maior,
# informar que ele é o maior.

# PASSO 6
# Caso nenhum dos dois
# seja maior,
# informar que os valores são iguais.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Comparar valores
# utilizando operadores relacionais.

# Utilizar if, elif e else
# para tratar todas as possibilidades.

# Garantir que apenas
# uma das mensagens
# seja exibida.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ int()
# ✔ variável
# ✔ if
# ✔ elif
# ✔ else
# ✔ operadores de comparação (>, <)
# ✔ print()