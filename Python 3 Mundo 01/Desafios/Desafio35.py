# ==================================================
# DESAFIO 35
# ==================================================

# Desenvolva um programa que leia o COMPRIMENTO de TRÊS RETAS

# E diga ao usuário se elas podem ou não FORMAR UM TRIÂNGULO.

# ==================================================
# EXEMPLOS DE SAÍDA (OUTPUT)
# ==================================================

# Caso 1 (Pode formar):
# Primeiro segmento: 3
# Segundo segmento: 4
# Terceiro segmento: 5
# Os segmentos acima PODEM FORMAR um triângulo!

# Caso 2 (Não pode formar):
# Primeiro segmento: 1
# Segundo segmento: 2
# Terceiro segmento: 9
# Os segmentos acima NÃO PODEM FORMAR um triângulo!

# ==================================================
print("-=-" * 10)
print("ANALISADOR DE TRIÂNGULOS")
print("-=-" * 10)
# Entrada dos dados
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

# Verificando se forma um triângulo (desigualdade triangular)
if a + b > c and a + c > b and b + c > a:
    print("Os segmentos acima PODEM formar um triângulo.")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo.")



# Para que três segmentos de reta formem um triângulo,
# eles precisam obedecer à regra chamada "desigualdade triangular".

# Regra:
# A soma de dois lados sempre deve ser maior que o terceiro lado.

# Ou seja, para lados a, b e c:
# a + b > c
# a + c > b
# b + c > a

# Se alguma dessas condições NÃO for verdadeira,
# então não é possível formar um triângulo.

# Exemplo:
# lados 3, 4 e 5 -> formam triângulo (todas as condições são verdadeiras)
# lados 2, 3 e 6 -> NÃO formam triângulo (2 + 3 não é maior que 6)