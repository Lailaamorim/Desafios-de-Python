# Resolução do Desafio 29:
velocidade = float(input("Qual a velocidade atual do carro: "))
if velocidade > 80:
    print(f"VOCÊ FOI MULTADO!😒\nO valor da multa é R$ {(velocidade - 80) * 7:.2f}")
print("Tenha um bom dia! Dirija com cuidado!!😊")    