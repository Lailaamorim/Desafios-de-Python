# DESAFIO 25:
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.
#
# Regras:
# - Considerar letras maiúsculas e minúsculas
#
# Exemplo:
# Entrada: Maria Silva Santos
# Saída: True

nome = input("Digite o nome de uma pessoa: ").strip() # Uso de strip() para evitar espaços extras
print(f"Seu nome tem 'SILVA'? {"silva" in nome.lower()}") # Verifica se "silva" está presente no nome, convertendo tudo para minúsculo para garantir a comparação correta independentemente do caso.