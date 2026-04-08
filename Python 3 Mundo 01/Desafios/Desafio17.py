# ============================================
# DESAFIO 17
# ============================================
# Crie um programa que:
# - Leia o valor do cateto oposto
# - Leia o valor do cateto adjacente
# - Calcule a hipotenusa
# - Mostre o resultado na tela
#
# DICA:
# - Use o Teorema de Pitágoras
# - Existe função pronta no math também

# Importa a função hypot da biblioteca math
# Essa função calcula diretamente a hipotenusa (√(co² + ca²))
from math import hypot

co = float(input("Digite o valor do cacteto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

# Calcula a hipotenusa usando a função hypot
# Isso equivale a: sqrt(co**2 + ca**2)
hi = hypot(co, ca)

# Mostra o resultado formatado com 2 casas decimais
print(f" A hipotenusa vai medir {hi:.2f}")