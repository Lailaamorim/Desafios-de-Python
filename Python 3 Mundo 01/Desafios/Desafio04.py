# DESAFIO 4
# Crie um programa que:
# 1. Leia qualquer coisa digitada pelo usuário
# 2. Mostre qual é o tipo primitivo do que foi digitado
# 3. Mostre várias informações sobre esse valor usando métodos de string
# 4. Verifique se:
#    - tem apenas espaços
#    - é um número
#    - é alfabético
#    - é alfanumérico
#    - está em letras maiúsculas
#    - está em letras minúsculas
#    - está capitalizado
a = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(a)}.")
print(f"Tem apenas espaços? {a.isspace()}")
print(f"É um número? {a.isnumeric()}")
print(f"É alfabético? {a.isalpha()}")
print(f"É alfanumérico? {a.isalnum()}")
print(f"Está em letras maiúsculas? {a.isupper()}")
print(f"Está em letras minúsculas? {a.islower()}")
print(f"Está capitalizado? {a.istitle()}")
