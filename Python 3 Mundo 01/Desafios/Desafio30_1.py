# Resolução do Desafio 30:
num =  int(input("Digite um número inteiro: "))
resultado = num  % 2
if resultado == 0:
    print(f"✅ O número {num} é PAR — Ele pode ser dividido por 2 sem deixar resto.")
else:
    print(f"🔢 O número {num} é ÍMPAR — A divisão por 2 deixa resto.")    
