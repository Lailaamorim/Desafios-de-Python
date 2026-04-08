# DESAFIO 24:
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".
#
# Regras:
# - Considerar letras maiúsculas e minúsculas
#
# Exemplo:
# Entrada: Santo André
# Saída: True

cidade = input("Digite o nome de uma cidade: ").strip() # Uso de strip() para evitar espaços extras
print(cidade[:5].upper() == "SANTO") # Verifica se os primeiros 5 caracteres, convertidos para maiúsculo, são "SANTO")