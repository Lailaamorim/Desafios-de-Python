"""
===========================================================
🐍 INTRODUÇÃO AO PYTHON 3 – CONCEITOS BÁSICOS
===========================================================

Este arquivo contém explicações básicas sobre:

- O que é Python
- Para que serve
- Como funciona
- Variáveis
- Tipos de dados
- Entrada e saída
- Operadores
- Conversão de tipos

Tudo explicado com comentários para facilitar o aprendizado.
"""

# =========================================================
# 📌 O QUE É PYTHON?
# =========================================================

# Python é uma linguagem de programação de alto nível,
# interpretada e de propósito geral.
# Ela é conhecida por sua sintaxe simples e fácil leitura.

# Em Python, não precisamos declarar o tipo da variável antes.
# A linguagem identifica automaticamente.


# =========================================================
# 📌 COMO EXIBIR UMA MENSAGEM NA TELA
# =========================================================

print("Hello world!")  # print() serve para mostrar algo na tela


# =========================================================
# 📌 VARIÁVEIS
# =========================================================

# Variáveis são espaços na memória que armazenam valores.
# Para criar uma variável, basta usar:

nome = "Maria"      # Variável do tipo texto (string)
idade = 25          # Variável do tipo inteiro (int)
altura = 1.68       # Variável do tipo decimal (float)
estudando = True    # Variável do tipo booleano (bool)

# Mostrando os valores
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Está estudando?", estudando)


# =========================================================
# 📌 TIPOS DE DADOS PRINCIPAIS
# =========================================================

# int     -> números inteiros (10, -5, 0)
# float   -> números decimais (3.14, 2.5)
# str     -> textos ("Olá")
# bool    -> verdadeiro ou falso (True ou False)

numero = 10
decimal = 5.5
texto = "Python"
verdadeiro = True

print(type(numero))      # Mostra o tipo da variável
print(type(decimal))
print(type(texto))
print(type(verdadeiro))


# =========================================================
# 📌 ENTRADA DE DADOS (input)
# =========================================================

# input() permite que o usuário digite algo

nome_usuario = input("Digite seu nome: ")
print("Prazer em te conhecer,", nome_usuario)

# IMPORTANTE:
# Tudo que vem do input() é do tipo string (texto).
# Mesmo que o usuário digite um número.


# =========================================================
# 📌 CONVERTENDO TIPOS DE DADOS
# =========================================================

# Para transformar o que o usuário digitou em número:

numero1 = int(input("Digite um número inteiro: "))
numero2 = float(input("Digite um número decimal: "))

soma = numero1 + numero2

print("A soma é:", soma)


# =========================================================
# 📌 OPERADORES MATEMÁTICOS
# =========================================================

a = 10
b = 3

print("Soma:", a + b)          # +
print("Subtração:", a - b)     # -
print("Multiplicação:", a * b) # *
print("Divisão:", a / b)       # /
print("Divisão inteira:", a // b)  # //
print("Resto da divisão:", a % b)  # %
print("Potência:", a ** b)     # **


# =========================================================
# 📌 OPERADORES DE COMPARAÇÃO
# =========================================================

print(a > b)   # Maior que
print(a < b)   # Menor que
print(a == b)  # Igual
print(a != b)  # Diferente
print(a >= b)  # Maior ou igual
print(a <= b)  # Menor ou igual


# =========================================================
# 📌 ESTRUTURA CONDICIONAL (if)
# =========================================================

idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# =========================================================
# 📌 RESUMO FINAL
# =========================================================

"""
Você aprendeu neste arquivo:

✔ O que é Python
✔ Como usar print()
✔ O que são variáveis
✔ Tipos de dados
✔ Como usar input()
✔ Conversão de tipos
✔ Operadores matemáticos
✔ Operadores de comparação
✔ Estrutura condicional (if/else)

Esses são os fundamentos da programação em Python.
"""

print("Fim da introdução ao Python! 🚀")