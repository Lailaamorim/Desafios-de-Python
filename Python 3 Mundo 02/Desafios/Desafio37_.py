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

# ==========================================
# DESAFIO 37
# ==========================================

# OBJETIVO
#
# Converter um número inteiro
# para a base numérica escolhida
# pelo usuário.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler um número inteiro.

# PASSO 2
# Pedir ao usuário
# que escolha a base
# para a conversão.

# PASSO 3
# Verificar qual opção
# foi escolhida.

# PASSO 4
# Realizar a conversão
# correspondente à opção escolhida.

# PASSO 5
# Mostrar o resultado
# da conversão.

# PASSO 6
# Caso a opção seja inválida,
# informar o usuário.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar uma estrutura
# de múltiplas decisões (if, elif e else).

# Executar uma ação diferente
# para cada opção escolhida.

# Utilizar as funções
# de conversão do Python
# para binário, octal
# e hexadecimal.

# Validar a entrada do usuário,
# tratando opções inválidas.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ int()
# ✔ variável
# ✔ if
# ✔ elif
# ✔ else
# ✔ bin()
# ✔ oct()
# ✔ hex()
# ✔ print()