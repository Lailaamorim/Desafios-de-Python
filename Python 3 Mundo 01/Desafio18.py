# ============================================
# DESAFIO 18
# ============================================
# Crie um programa que:
# - Leia um ângulo em graus
# - Mostre o seno, cosseno e tangente desse ângulo
#
# DICA:
# - A biblioteca math trabalha com radianos
# - Você vai precisar converter graus → radianos
# Importa funções da biblioteca math:
# radians -> converte graus para radianos
# sin -> calcula o seno
# cos -> calcula o cosseno
# tan -> calcula a tangente
from math import radians, sin, cos, tan
angulo = float(input("Digite o ângilo que você deseja? "))

# Calcula o seno do ângulo
# Primeiro converte o ângulo para radianos, pois as funções trigonométricas usam radianos
seno = sin(radians(angulo))
print(f"O Ângulo de {angulo} tem o SENO de {seno:.2f}")

# Calcula o cosseno do ângulo (também convertendo para radianos)
cosseno = cos(radians(angulo))
print(f"O Ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")

# Calcula a tangente do ângulo
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")