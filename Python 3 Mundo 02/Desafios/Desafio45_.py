import random
from time import sleep

print("=" * 70)

print("""
     ██╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  ██████╗
     ██║██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
     ██║██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝██║   ██║
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔═══╝ ██║   ██║
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝
""")

print("=" * 70)

jogador_nome = input("Digite o seu nome: ").strip()
computador_nome = "Hamorym"

print(f"\n👤 Jogador: {jogador_nome}")
print(f"🤖 Computador: {computador_nome}")

print("\nEscolha sua jogada:")
print("[0] ✊ PEDRA")
print("[1] ✋ PAPEL")
print("[2] ✌️ TESOURA")

jogador = int(input("\nQual é a sua jogada? "))

if jogador < 0 or jogador > 2:
    print("\n❌ Jogada inválida!")
else:
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    computador = random.randint(0, 2)

    print()
    print("JO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PÔ!!!")
    sleep(1)

    print("=" * 70)
    print(f"🤖 {computador_nome} jogou: {opcoes[computador]}")
    print(f"👤 {jogador_nome} jogou: {opcoes[jogador]}")
    print("=" * 70)

    if jogador == computador:
        print("\n🤝 EMPATE!")

    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print(f"\n🏆 PARABÉNS, {jogador_nome.upper()}! VOCÊ VENCEU!")

    else:
        print(f"\n🤖 {computador_nome.upper()} VENCEU!")

print("\nObrigado por jogar! 🎮")