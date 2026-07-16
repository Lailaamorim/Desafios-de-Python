# DESAFIO 07 – Média do Aluno
# Crie um programa que leia duas notas de um aluno.
# Em seguida, calcule e mostre a média entre essas duas notas.
#
# Exemplo:
# Digite a primeira nota: 7.5
# Digite a segunda nota: 8.0
# A média do aluno é 7.75

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media= (nota1+nota2) / 2
print(f"A media do aluno é: {media:.1f}")

#Consegui fazer igual ao do professor(❁´◡`❁)

# ==========================================
# DESAFIO 07
# ==========================================

# OBJETIVO
#
# Calcular a média de duas notas.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler a primeira e a segunda nota,
# guardando cada uma em sua variável correspondente.

# PASSO 2
# Somar as duas notas.

# PASSO 3
# Dividir o resultado por 2
# para obter a média.

# PASSO 4
# Mostrar a média.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar o tipo float()
# para aceitar notas com casas decimais.

# Utilizar parênteses
# para realizar a soma antes da divisão.

# Formatar a saída
# para mostrar apenas uma casa decimal.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (+) e (/)
# ✔ print()