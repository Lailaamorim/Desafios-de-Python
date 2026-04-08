"""
Tipos Primitivos (Python)

Tipos primitivos são os tipos básicos de dados que o Python usa para guardar informações.

Os principais são:

int → números inteiros
Exemplo: 10, -3, 25

float → números com casas decimais
Exemplo: 3.14, 7.5, 10.0

str → textos (strings)
Exemplo: "Python", "Olá mundo"

bool → valores lógicos
Exemplo: True ou False

Esses tipos servem para armazenar diferentes tipos de informação dentro das variáveis.

Saída de Dados

Saída de dados é quando o programa mostra informações na tela para o usuário.

Em Python isso é feito principalmente com o comando:

print()

Exemplo:

print("Olá, mundo!")

Esse comando faz o programa exibir uma mensagem no terminal ou na tela.

✅ Resumo geral

Tipos primitivos → tipos básicos de dados que guardam informações.

Saída de dados → forma de mostrar informações para o usuário usando print().

"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = n1 + n2
print(f"A soma entre {n1} e {n2} é {s}")
