# ==================================================
# DESAFIO 29
# ==================================================

# Escreva um programa que leia a velocidade de um carro

# Se a velocidade ultrapassar 80 Km/h,
# o programa deve mostrar uma mensagem dizendo
# que o motorista foi multado

# A multa vai custar R$7,00
# para cada Km acima do limite permitido

# ==================================================
# EXEMPLO DE FUNCIONAMENTO
# ==================================================

# Se estiver acima de 80 Km/h → leva multa
# Se estiver até 80 Km/h → não leva multa

velocidade = int(input("Informe a velocidade do carro: "))
if velocidade > 80:
  valor = velocidade - 80 # calcula quanto o carro ultrapassou o limite
  multa =  7 * valor # calcula o valor da multa (R$7 por km acima)

  print(f"Você foi multado Em R$ {multa}")
else: 
  print("TUDO CERTO!")  