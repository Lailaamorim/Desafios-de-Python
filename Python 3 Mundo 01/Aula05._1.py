# =========================================
# MANIPULAÇÃO DE STRINGS EM PYTHON
# =========================================

frase = "Eu sou uma programadora determinada e vou dominar Python"

# -----------------------------------------
# FATIAMENTO DE STRING
# Serve para pegar partes da frase
# [início:fim] → pega do início até o fim (sem incluir o fim)
# -----------------------------------------
print(frase[0:6])  # Resultado: 'Eu sou'


# -----------------------------------------
# len()
# Serve para contar quantos caracteres tem na frase (incluindo espaços)
# -----------------------------------------
print(len(frase))  # Exemplo de resultado: 60


# -----------------------------------------
# count()
# Serve para contar quantas vezes um caractere ou palavra aparece
# -----------------------------------------
print(frase.count("a"))  # Resultado: 8


# -----------------------------------------
# find()
# Serve para mostrar a posição onde começa uma palavra
# Se não encontrar, retorna -1
# -----------------------------------------
print(frase.find("programadora"))  # Resultado: 13


# -----------------------------------------
# replace()
# Serve para substituir uma palavra por outra
# -----------------------------------------
print(frase.replace("determinada", "incrível"))
# Resultado: 'Eu sou uma programadora incrível e vou dominar Python'


# -----------------------------------------
# upper()
# Serve para deixar toda a frase em MAIÚSCULO
# -----------------------------------------
print(frase.upper())
# Resultado: 'EU SOU UMA PROGRAMADORA DETERMINADA E VOU DOMINAR PYTHON'


# -----------------------------------------
# lower()
# Serve para deixar toda a frase em minúsculo
# -----------------------------------------
print(frase.lower())
# Resultado: 'eu sou uma programadora determinada e vou dominar python'


# -----------------------------------------
# capitalize()
# Serve para deixar apenas a primeira letra da frase maiúscula
# -----------------------------------------
print(frase.capitalize())
# Resultado: 'Eu sou uma programadora determinada e vou dominar python'


# -----------------------------------------
# title()
# Serve para deixar a primeira letra de cada palavra maiúscula
# -----------------------------------------
print(frase.title())
# Resultado: 'Eu Sou Uma Programadora Determinada E Vou Dominar Python'


# -----------------------------------------
# strip()
# Serve para remover espaços do começo e do fim da frase
# -----------------------------------------
frase2 = "   Eu vou dominar Python   "
print(frase2.strip())
# Resultado: 'Eu vou dominar Python'


# -----------------------------------------
# join()
# Serve para juntar elementos de uma lista em uma frase
# -----------------------------------------
lista = ["Eu", "vou", "ser", "uma", "programadora", "incrível"]
print(" ".join(lista))
# Resultado: 'Eu vou ser uma programadora incrível'