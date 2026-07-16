# DESAFIO 08 – Conversão de Medidas
# Crie um programa que leia um valor em metros.
# Em seguida, exiba esse valor convertido em centímetros e milímetros.
#
# Exemplo:
# Digite um valor em metros: 2
# 2 metros equivalem a 200 centímetros
# 2 metros equivalem a 2000 milímetros

valor1 = float(input("Digite o número: "))
cent = valor1 * 100
mil = valor1 * 1000
print(f"{valor1} metros equivalem a {cent} centímetros")
print(f"metros equivalem a {mil} milímetros")

# Consegui fazer igual ao do professor(❁´◡`❁)

# ==========================================
# DESAFIO 08
# ==========================================

# OBJETIVO
#
# Converter uma medida em metros
# para centímetros e milímetros.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler um valor em metros,
# guardando-o em uma variável.

# PASSO 2
# Calcular o valor em centímetros.

# PASSO 3
# Calcular o valor em milímetros.

# PASSO 4
# Mostrar as duas conversões.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Para converter metros em centímetros,
# multiplica-se por 100.

# Para converter metros em milímetros,
# multiplica-se por 1000.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operador (*)
# ✔ print()