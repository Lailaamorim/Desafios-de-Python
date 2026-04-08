# DESAFIO 22:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar os espaços)
# - Quantas letras tem o primeiro nome

# MARIA SILVA SANTOS
# maria silva santos
# 16
# 5

nome_completo = input("Digite seu nome: ").strip() # Uso de strip() para evitar espaços extras no início/fim

# Exibição do nome em diferentes formatos
print("Nome em maiúsculas:", nome_completo.upper())
print("Nome em minúsculas:", nome_completo.lower())

# Contagem de letras (sem espaços)
total_letras = len(nome_completo.replace(" ", ""))
print("Total de letras (sem espaços):", total_letras)

# Separação do primeiro nome
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)

print("Letras do primeiro nome:", letras_primeiro_nome)
