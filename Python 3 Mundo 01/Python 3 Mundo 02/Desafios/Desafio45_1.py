from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Suas opções: 
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input("Qual é a sua jogada? "))
print("-=" * 11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 11)
if computador == 0: # computador jogou pedra  
    if jogador == 0: 
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:    
        print("COMPUTADOR VENCE!")
    else:
        print("Jogada inválida! Tente novamente.")
elif computador == 1: # computador jogou papel
    if jogador == 0: 
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:    
        print("JOGADOR VENCE!")
    else:
        print("Jogada inválida! Tente novamente.")
elif computador == 2: # computador jogou tesoura 
    if jogador == 0:    
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:   
        print("EMPATE!") 
    else:
        print("Jogada inválida! Tente novamente.")    
