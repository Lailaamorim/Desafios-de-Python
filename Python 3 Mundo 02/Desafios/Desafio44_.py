# DESAFIO 044 – Gerenciador de Pagamentos

# Elabore um programa que calcule
# o valor a ser pago por um produto,
# considerando o seu preço normal
# e condição de pagamento:
#
# - À vista dinheiro/cheque:
#   10% de desconto
#
# - À vista no cartão:
#   5% de desconto
#
# - Em até 2x no cartão:
#   preço normal
#
# - 3x ou mais no cartão:
#   20% de juros
#
# Exemplo:
# Preço das compras: R$100
# Forma de pagamento: 1
#
# Total a pagar: R$90.00

print("=" * 40)
print("GERENCIADOR DE PAGAMENTOS".center(40))
print("=" * 40)

valor_compras = float(input("Preço das compras: R$ "))

print("""
Escolha a forma de pagamento:

[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
""")

pagamento = int(input("Digite a opção: "))
print()

if pagamento == 1:
    total = valor_compras - (valor_compras * 10 / 100)
    print("Forma de pagamento: À vista dinheiro/cheque")
    print("Desconto de 10%")
    print(f"Total a pagar: R$ {total:.2f}")

elif pagamento == 2:
    total = valor_compras - (valor_compras * 5 / 100)
    print("Forma de pagamento: À vista no cartão")
    print("Desconto de 5%")
    print(f"Total a pagar: R$ {total:.2f}")

elif pagamento == 3:
    total = valor_compras
    parcela = total / 2
    print("Forma de pagamento: 2x no cartão")
    print("Sem desconto.")
    print(f"Total a pagar: R$ {total:.2f}")
    print(f"2 parcelas de R$ {parcela:.2f}")

elif pagamento == 4:
    total = valor_compras + (valor_compras * 20 / 100)
    parcelas = int(input("Quantas parcelas? "))
    valor_parcela = total / parcelas

    print("Forma de pagamento: 3x ou mais no cartão")
    print("Juros de 20%")
    print(f"Total a pagar: R$ {total:.2f}")
    print(f"{parcelas} parcelas de R$ {valor_parcela:.2f}")

else:
    print("Opção inválida!")