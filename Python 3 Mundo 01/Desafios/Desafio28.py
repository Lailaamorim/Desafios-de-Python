# ==================================================
# DESAFIO 28
# ==================================================

# Faça um programa onde o computador "pense"
# em um número inteiro entre 0 e 5

# O programa deve pedir para o usuário tentar adivinhar
# qual número foi escolhido

# Depois disso, o programa deve comparar:
# - o número digitado pelo usuário
# - com o número escolhido pelo computador

# E mostrar o resultado:

# Se o usuário acertar:
# "Você venceu!"

# Se o usuário errar:
# "Você perdeu!"

# ==================================================
# EXEMPLOS DE FUNCIONAMENTO
# ==================================================

# Exemplo 1:
# Entrada: 3
# Saída:
# Você venceu!

# Exemplo 2:
# Entrada: 1
# Saída:
# Você perdeu!

import random
print("="*30)
print("       VAMOS BRINCAR!😊   ")
print("="*30)
num = int(input("Adivinhe o número que eu estou pensando: "))
comp = random.randint(1,5) 
print(f"ADIVINHE UM NÚMERO DE 1 A 5: {comp}")
if num == comp:
  print("DROGA... VOCÊ VENCEU!😒")
else:
  print("HAHA! EU GANHEI TROUXA !!😎")  