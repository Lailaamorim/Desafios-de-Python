# DESAFIO 042 – Analisando Triângulos v2.0

# Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
#
# - Equilátero:
#   todos os lados iguais
#
# - Isósceles:
#   dois lados iguais
#
# - Escaleno:
#   todos os lados diferentes
#
# Exemplo:
# Primeiro segmento: 6
# Segundo segmento: 6
# Terceiro segmento: 6
#
# Os segmentos podem formar um triângulo.
# Tipo: EQUILÁTERO

# A soma de dois lados deve ser maior que o terceiro lado.

print("=" * 40)
print("Analisando Triângulos".center(40))
print("=" * 40)

a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))
print()

if a + b > c and a + c > b and b + c > a:
    print("Os segmentos podem formar um triângulo.")

    if a == b == c:
        print("Tipo: EQUILÁTERO")
        print("Todos os lados são iguais.")

    elif a != b and a != c and b != c:
        print("Tipo: ESCALENO")
        print("Todos os lados são diferentes.")

    else:
        print("Tipo: ISÓSCELES")
        print("Dois lados são iguais.")

else:
    print("Os segmentos não podem formar um triângulo.")