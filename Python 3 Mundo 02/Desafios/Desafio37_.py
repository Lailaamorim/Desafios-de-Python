# DESAFIO 037 – Conversor de Bases Numéricas
# Escreva um programa que leia um número inteiro
# e peça para o usuário escolher qual será a base da conversão:
#
# 1 para binário
# 2 para octal
# 3 para hexadecimal
#
# Exemplo:
# Digite um número inteiro: 25
#
# Escolha uma das bases para conversão:
# 1 - Binário
# 2 - Octal
# 3 - Hexadecimal
#
# Sua opção: 1
# 25 convertido para BINÁRIO é 11001

numero = int(input("Digite um número: "))
opcao = int(input("Escolha uma opção: [1], [2] ou [3]: "))

if opcao == 1:
  resultado = bin(numero)
  print(f"O numero {numero} convertido para  BINÁRIO é {resultado}")
  # Converter para binário

elif opcao == 2:  
  resultado = oct(numero)
  print(f"O numero {numero} convertido para OCTAL é {resultado}")
  # Converter para octal

elif opcao == 3:
  resultado = hex(numero)
  print(f"O número {numero} convertido para HEXADECIMAL é {resultado}")
  # Converter para hexadecimal

else:
  print("Opção Inválida")
  # Opção Inválida
