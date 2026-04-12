# ==================================================
# DESAFIO 33
# ==================================================

# Faça um programa que leia TRÊS NÚMEROS

# E mostre qual é o MAIOR e qual é o MENOR.

# ==================================================
# EXEMPLO DE SAÍDA (OUTPUT)
# ==================================================

# Primeiro valor: 9
# Segundo valor: 4
# Terceiro valor: 27

# O menor valor digitado foi 4
# O maior valor digitado foi 27

# ==================================================
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

# Verificando o menor valor entre os três números
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o maior valor entre os três números
maior = n1 
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")                