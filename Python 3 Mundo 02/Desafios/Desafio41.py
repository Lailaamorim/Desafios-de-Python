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
