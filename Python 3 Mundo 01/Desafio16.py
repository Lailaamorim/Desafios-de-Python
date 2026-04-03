# ============================================
# DESAFIO 16
# ============================================
# Crie um programa que:
# - Leia um número real (com casas decimais)
# - Mostre apenas a parte inteira desse número
#
# Exemplo:
# Entrada: 6.127
# Saída: 6
#
# DICA:
# - Pense em funções da biblioteca math
# - Ou em formas de "remover" a parte decimal
num = float(input("Digite um número:)"))
print(f"O valor digitado foi {num} e a sua parte inteira é {int(num)}")