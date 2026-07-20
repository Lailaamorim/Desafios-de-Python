# DESAFIO 040 – Aquele Clássico da Média

# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#
# Exemplo:
# Digite a primeira nota: 7
# Digite a segunda nota: 8
#
# A média foi 7.5
# APROVADO
#
# ----------------------------------------
#
# Exemplo:
# Digite a primeira nota: 3
# Digite a segunda nota: 4
#
# A média foi 3.5
# REPROVADO
#
# ----------------------------------------
#
# Exemplo:
# Digite a primeira nota: 5
# Digite a segunda nota: 6
#
# A média foi 5.5
# RECUPERAÇÃO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
print()

media = (nota1 + nota2) / 2
print(f"A média foi {media}")

if media >= 7:
  print("APROVADO!!")

elif media < 7 and media >= 5:
  print("RECUPERAÇÃO!!")

else:
    print("REPROVADO!!")

    # ==========================================
# DESAFIO 40
# ==========================================

# OBJETIVO
#
# Calcular a média de um aluno
# e informar sua situação
# de acordo com a nota obtida.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler as duas notas do aluno,
# guardando cada uma em sua variável.

# PASSO 2
# Calcular a média das notas.

# PASSO 3
# Mostrar a média obtida.

# PASSO 4
# Verificar se a média
# é maior ou igual a 7.

# PASSO 5
# Se for,
# informar que o aluno
# está APROVADO.

# PASSO 6
# Caso contrário,
# verificar se a média
# está entre 5 e 6.9.

# PASSO 7
# Se estiver,
# informar que o aluno
# está em RECUPERAÇÃO.

# PASSO 8
# Caso a média seja menor que 5,
# informar que o aluno
# está REPROVADO.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Resolver um problema
# utilizando faixas de valores.

# Utilizar if, elif e else
# para classificar um resultado.

# Fazer as comparações
# em uma ordem lógica,
# do maior valor para o menor.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (+) e (/)
# ✔ if
# ✔ elif
# ✔ else
# ✔ operadores de comparação (>=, <)
# ✔ operador lógico (and)
# ✔ print()