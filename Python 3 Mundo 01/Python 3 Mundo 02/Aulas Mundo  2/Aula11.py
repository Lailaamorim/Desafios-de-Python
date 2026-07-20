# =================================================================
# AULA COMPLETA: ESTRUTURAS CONDICIONAIS (IF, ELIF, ELSE)
# =================================================================

# 1. O QUE SÃO?
# São blocos de código que controlam o fluxo do programa.
# O Python analisa uma condição (que sempre resulta em Verdadeiro ou Falso)
# e decide qual caminho seguir.

# Vamos criar uma variável para usar de exemplo na nossa aula:
nota = 7.5

# 2. A REGRA DE OURO DA INDENTAÇÃO:
# Repare nos 4 espaços (ou um Tab) antes do 'print'. 
# No Python, isso mostra o que está "dentro" de cada condição.

print("--- EXEMPLO 1: ESTRUTURA COMPLETA ---")

if nota >= 9.0:
    # O 'if' é SEMPRE o primeiro. É a condição principal.
    # Só roda se a nota for maior ou igual a 9.
    print("Excelente! Você ganhou uma medalha!")

elif nota >= 7.0:
    # O 'elif' (senão se) é o nosso Plano B.
    # Você pode ter QUANTOS ELIF QUISER entre o if e o else.
    # Só é testado se o 'if' lá de cima der FALSO.
    print("Aprovado! Parabéns!")

elif nota >= 5.0:
    # Mais um 'elif' (nosso Plano C).
    # Só é testado se o 'if' E o 'elif' de cima falharem.
    print("Recuperação. Ainda dá para recuperar!")

else:
    # O 'else' (senão) é o "porto seguro". Ele FECHA a estrutura.
    # ATENÇÃO: Nunca escreva 'elise' (com i) pois dá erro no VS Code!
    # O 'else' NÃO tem condição ao lado dele (não tem 'nota < 5').
    # Ele simplesmente assume o controle se TUDO lá de cima falhar.
    print("Reprovado. Vamos estudar mais no próximo bimestre.")


# =================================================================
# REGRAS IMPORTANTES PARA VOCÊ DECORAR:
# =================================================================

# Regra 1: Você PODE usar um 'if' sozinho.
# Regra 2: Você NÃO PODE usar um 'elif' ou um 'else' sem um 'if' antes.
# Regra 3: Só é possível ter UM 'if' e UM 'else' por bloco de votação.
# Regra 4: Você pode ter INFINITOS 'elif' entre eles.
# Regra 5: O Python lê de cima para baixo. Assim que ele acha uma 
#          condição VERDADEIRA, ele executa o bloco dela e IGNORA o resto.

print("\n--- EXEMPLO 2: COMPRANDO UM CARRO (MÚLTIPLOS ELIFS) ---")

dinheiro = 45000

if dinheiro >= 100000:
    print("Comprar um carro de luxo.")
elif dinheiro >= 70000:
    print("Comprar um SUV seminovo.")
elif dinheiro >= 40000:
    print("Comprar um hatch compacto.")
elif dinheiro >= 20000:
    print("Comprar um carro usado antigo.")
else:
    # Se o dinheiro for menor que 20000, cai direto aqui:
    print("Melhor ir de transporte público ou guardar mais dinheiro.")

print("\nFim da aula! Modifique os valores das variáveis no VS Code e teste!")