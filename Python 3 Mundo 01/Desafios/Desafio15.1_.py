# Esse foi o primeiro que fiz desse enunciado pois, ele é mais detalhado para que eu possa 
# entender melhor que que foi pedido e feito e se tudo está correto. e se eu entendi bem, 
# o outro é curto pois peguei a ideia do professor 
km = int(input("Quantos KM foram percorridos? "))
dias = int(input("Quantos dias o carro foi alugado? "))
dia_carro = dias * 60
km_rodado = km * 0.15
print(f"O carro foi alugado por {dias} e o valor a ser pago {dia_carro}")
print(f"O carro rodou {km} e deve ser pago o valor {km_rodado}")
print(f"O valor total a ser pago será de R${dia_carro + km_rodado}")