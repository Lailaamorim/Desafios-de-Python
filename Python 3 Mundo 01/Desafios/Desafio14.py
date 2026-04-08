# Escreva um programa que leia uma temperatura em graus Celsius (C)
# digitada pelo usuário e a converta para graus Fahrenheit (F).
# Utilize a fórmula: F = ((9 * c) / 5) + 32clera
# .
# Ao final, exiba o valor convertido na tela.

c = float(input("Digite a temperatura em graus celsius: "))
f = 9 * c / 5 + 32
print(f"A temperatura de {c}°C corresponde a {f}°F")