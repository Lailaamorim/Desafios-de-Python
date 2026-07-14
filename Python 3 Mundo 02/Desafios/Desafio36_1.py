casa = float(input("Valor da casa: R$ "))
salario = float (input("Salário do comprador: "))
anos = int(input("Em quantos anos vai pagar?"))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Empréstimo negado!")