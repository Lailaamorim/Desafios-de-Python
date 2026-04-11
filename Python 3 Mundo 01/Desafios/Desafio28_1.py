# Resolução do Desafio 28:
from random import randint
from time import sleep

print("-=-"*20)
computador = randint(0,5) # Faz o computador "PENSAR" em um número entre 0 e 5
print("VAMOS BRINCAR!😊")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == computador: 
    print("VOCÊ VENCEU!😊")
else:
    print("VOCÊ PERDEU!😒")