from datetime import date 
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}.")
if idade == 18:
    print("Você tem que se alistar IMEDIATEMENTE!")
elif idade < 18: 
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento.")
    ano = atual + saldo
    print(f"Seu alistamento será em {atual + saldo}.")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    ano = atual - saldo
    print(f"Seu alistamento foi em {atual - saldo}.")
    # ==========================================
# DESAFIO 39
# ==========================================

# OBJETIVO
#
# Verificar a situação
# do alistamento militar
# de acordo com a idade
# da pessoa.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Obter o ano atual.

# PASSO 2
# Ler o ano de nascimento.

# PASSO 3
# Calcular a idade da pessoa.

# PASSO 4
# Verificar se a idade
# é igual a 18 anos.

# PASSO 5
# Se for igual a 18,
# informar que o alistamento
# deve ser feito imediatamente.

# PASSO 6
# Se for menor que 18,
# calcular quantos anos faltam
# para o alistamento
# e em que ano ele deverá acontecer.

# PASSO 7
# Se for maior que 18,
# calcular há quantos anos
# o alistamento deveria ter sido feito
# e informar em que ano isso ocorreu.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar a data atual
# para que o programa
# funcione em qualquer ano.

# Calcular a idade
# a partir do ano de nascimento.

# Resolver um problema
# com três possibilidades diferentes
# utilizando if, elif e else.

# Realizar cálculos diferentes
# conforme a situação da pessoa.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ from datetime import date
# ✔ date.today().year
# ✔ input()
# ✔ int()
# ✔ variável
# ✔ operadores (+) e (-)
# ✔ if
# ✔ elif
# ✔ print()
