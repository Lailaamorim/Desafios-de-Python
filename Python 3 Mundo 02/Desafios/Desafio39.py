# DESAFIO 039 – Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
#
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
#
# O programa também deverá mostrar
# quanto tempo falta ou quanto tempo passou do prazo.
#
# ----------------------------------------
# EXEMPLO 1 – Ainda não chegou a hora
#
# Digite o ano de nascimento: 2010
#
# Você tem 16 anos.
# Ainda não chegou a hora de se alistar.
# Faltam 2 anos para o alistamento.
#
# ----------------------------------------
# EXEMPLO 2 – Está na hora
#
# Digite o ano de nascimento: 2008
#
# Você tem 18 anos.
# Está na hora de se alistar!
#
# ----------------------------------------
# EXEMPLO 3 – Já passou da hora
#
# Digite o ano de nascimento: 2004
#
# Você tem 22 anos.
# Já passou da hora de se alistar.
# Você deveria ter se alistado há 4 anos.
#
# ----------------------------------------

ano_nascimento = int(input("Digite o ano que você nasceu: "))
anoAtual = 2026

idade =  (anoAtual - ano_nascimento)
anosFaltantes = 18 - idade

print(f"Você tem {idade} anos")
print()

if idade < 18 :
  print("Você ainda vai se alistar ao Serviso Militar ")
  print(f"Faltam {anosFaltantes} ano(s) para o alistamento.")

elif idade == 18 :
  print("Está na hora de se alistar ao Serviço Militar")

else:
  print("Já passou da hora de se alistar ao Serviço Militar")
  print(f"Você deveria ter se alistado há {anosFaltantes} ano(s).")
