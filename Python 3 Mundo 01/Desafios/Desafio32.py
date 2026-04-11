# ==================================================
# DESAFIO 32
# ==================================================

# Faça um programa que leia um ano qualquer

# E mostre se ele é BISSEXTO

# ==================================================
# EXEMPLOS DE FUNCIONAMENTO
# ==================================================

# Um ano é bissexto quando:
# - É divisível por 4
# - Não é divisível por 100, EXCETO se for divisível por 400

# Exemplos de anos bissextos:
# 2020, 2024, 2000

# Exemplos de anos não bissextos:
# 1900, 2023

from datetime import date  # importa a função para trabalhar com datas
ano = int(input("Digite um ano: "))

if ano == 0:
    ano = date.today().year # se o usuário digitar 0, pega o ano atual do sistema

# verifica se o ano é bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    # condição:
    # - divisível por 4
    # - e (não divisível por 100 OU divisível por 400)
    print(f"O ano {ano} é Bissexto!")  # mostra que é bissexto
else: 
    print(f"O ano {ano} Não é Bissexto!")  # caso contrário, não é bissexto