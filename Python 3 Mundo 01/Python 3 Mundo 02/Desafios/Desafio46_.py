# ==========================================
# DESAFIO 46
# ==========================================

# ENUNCIADO:
#
# Faça um programa que mostre na tela uma
# contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre cada número.

# ------------------------------------------
# EXEMPLO DE EXECUÇÃO NO TERMINAL
# ------------------------------------------

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
#
# 🎆 BOOM! 🎆
# (Ou a mensagem que você escolher para indicar
# o estouro dos fogos.)

# ------------------------------------------
# O QUE O PROGRAMA DEVE FAZER
# ------------------------------------------

# Mostrar os números de 10 até 0.
#
# Esperar 1 segundo entre cada número.
#
# Ao final da contagem, mostrar uma mensagem
# indicando o estouro dos fogos.
import time

for i in range(10, -1, -1): #inicio, fim, passo
    print(i)
    time.sleep(1)
print("🎆 BOOM! 🎆")     























# ==========================================
# DESAFIO 46
# ==========================================

# OBJETIVO
#
# Fazer uma contagem regressiva
# de 10 até 0,
# aguardando 1 segundo entre cada número.

# ------------------------------------------
# RECEITA DA LÓGICA
# ------------------------------------------

# PASSO 1
# Iniciar uma repetição
# que conte de 10 até 0.

# PASSO 2
# Mostrar cada número da contagem.

# PASSO 3
# Aguardar 1 segundo
# antes de mostrar o próximo número.

# PASSO 4
# Quando a contagem terminar,
# mostrar uma mensagem indicando
# o estouro dos fogos.

# ------------------------------------------
# O QUE O PROFESSOR QUIS ENSINAR
# ------------------------------------------

# Utilizar o laço for
# para realizar uma contagem regressiva.

# Utilizar uma pausa de 1 segundo
# entre cada repetição.

# Executar um comando
# somente após o término do laço.

# ------------------------------------------
# FERRAMENTAS UTILIZADAS
# ------------------------------------------

# ✔ for
# ✔ range()
# ✔ print()
# ✔ time.sleep()