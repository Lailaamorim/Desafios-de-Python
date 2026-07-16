# DESAFIO 11 – Pintando Parede
# Crie um programa que leia a largura e a altura de uma parede em metros.
# Em seguida, calcule a área da parede e a quantidade de tinta necessária para pintá-la.
# Considere que cada litro de tinta pinta uma área de 2 metros quadrados.
#
# Exemplo:
# Digite a largura da parede: 4
# Digite a altura da parede: 2.5
# A área da parede é 10.0 m²
# Você precisará de 5.0 litros de tinta

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"Sua parede tem a dimenção de {largura}X{altura} e sua área é de {area}m²")
# Não consegui fazer sozinha ಥ_ಥ

# ==========================================
# DESAFIO 11
# ==========================================

# OBJETIVO
#
# Calcular a área de uma parede
# e a quantidade de tinta necessária
# para pintá-la.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Ler a largura e a altura da parede,
# guardando cada valor em sua variável.

# PASSO 2
# Calcular a área da parede
# multiplicando a largura pela altura.

# PASSO 3
# Calcular a quantidade de tinta necessária,
# dividindo a área por 2.

# PASSO 4
# Mostrar:
# - a largura;
# - a altura;
# - a área da parede;
# - a quantidade de tinta necessária.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# A área de um retângulo
# é calculada multiplicando
# a largura pela altura.

# Cada litro de tinta
# pinta 2 m².

# Por isso,
# divide-se a área por 2
# para descobrir
# quantos litros serão necessários.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ input()
# ✔ float()
# ✔ variável
# ✔ operadores (*) e (/)
# ✔ print()