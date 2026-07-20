# DESAFIO 041 – Classificando Atletas

# A Confederação Nacional de Natação
# precisa de um programa que leia o
# ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
#
# - Até 9 anos:
#   MIRIM
#
# - Até 14 anos:
#   INFANTIL
#
# - Até 19 anos:
#   JUNIOR
#
# - Até 20 anos:
#   SÊNIOR
#
# - Acima:
#   MASTER
#
# Exemplo:
# Digite o ano de nascimento: 2012
#
# O atleta tem 13 anos.
# Categoria: INFANTIL

from datetime import date
ano = int(input("Digite o ano que você nasceu: "))
print("="*40)
print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("="*40)
print()

idade = date.today().year - ano
print(f"O atleta tem {idade} anos")

if idade <= 9:
  print("Categoria: MIRIM")
elif idade <= 14:
  print("Categoria: INFANTIL")  
elif idade <= 19:
  print("JUNIOR")  
elif idade <= 25:
  print("Categoria: SÊNIOR")
else:
  print("Categoria: MASTER")  

# ==========================================
# DESAFIO 41
# ==========================================

# OBJETIVO
#
# Descobrir a categoria
# de um atleta
# de acordo com sua idade.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Obter o ano atual.

# PASSO 2
# Ler o ano de nascimento
# do atleta.

# PASSO 3
# Calcular a idade do atleta.

# PASSO 4
# Mostrar a idade calculada.

# PASSO 5
# Comparar a idade
# com os limites
# de cada categoria.

# PASSO 6
# Informar a categoria
# correspondente.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar a data atual
# para calcular a idade.

# Classificar um valor
# utilizando faixas de idade.

# Organizar as comparações
# do menor limite
# para o maior.

# Utilizar if, elif e else
# para que apenas
# uma categoria seja exibida.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ from datetime import date
# ✔ date.today().year
# ✔ input()
# ✔ int()
# ✔ variável
# ✔ operadores (-)
# ✔ if
# ✔ elif
# ✔ else
# ✔ operadores de comparação (<=)
# ✔ print()