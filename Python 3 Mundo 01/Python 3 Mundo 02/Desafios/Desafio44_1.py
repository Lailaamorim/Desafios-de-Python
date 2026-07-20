print(f"{'LOJAS HAMORYM':^40}")
preco = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[1] Á vista dinheiro/cheque
[2] Á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão     ''')

opcao = int(input("Qual é a opção? "))
if opcao == 1: 
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3: 
    total = preco
    parcela = total / 2 
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print(f"Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS")    
print(f"sua compre de R${preco:.2f} vai custar R${preco:.2f} vai custar R${total:.2f} no final")
