# DESAFIO 26:
# Faça um programa que leia uma frase qualquer pelo teclado
# e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
#
# Regras:
# - Considerar letras maiúsculas e minúsculas
#
# Exemplo:
# Entrada: Arara azul
# Saída:
# 5
# 1
# 5
# Pede para o usuário digitar uma frase
# .upper() transforma tudo em maiúsculas
# .strip() remove espaços no início e no fim
frase = input("Digite uma frase: ").upper().strip()

# Conta quantas vezes a letra 'A' aparece na frase
print(f"A letra 'A' aparece {frase.count('A')} vezes")

# Encontra a posição da primeira ocorrência de 'A'
# .find('A') retorna a posição começando do 0
# +1 ajusta para começar do 1 (mais intuitivo para o usuário)
print(f"A primeira letra 'A' apareceu na posição {frase.find('A') + 1}")

# Encontra a posição da última ocorrência de 'A'
# .rfind('A') procura da direita para a esquerda
# +1 também ajusta a posição
print(f"A última letra 'A' apareceu na posição {frase.rfind('A') + 1}")