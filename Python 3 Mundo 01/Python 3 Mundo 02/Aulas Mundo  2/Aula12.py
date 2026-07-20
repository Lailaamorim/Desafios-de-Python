# ============================
# LAÇOS DE REPETIÇÃO (LOOPS)
# ============================

# Um laço de repetição é uma estrutura que permite executar o mesmo bloco
# de código várias vezes, sem precisar escrever o código repetidamente.

# A repetição continua enquanto uma condição for verdadeira
# ou durante uma quantidade determinada de vezes.

# A principal vantagem é deixar o código menor, mais organizado
# e evitar repetições desnecessárias.

# ============================
# O QUE É ITERAÇÃO?
# ============================

# Iteração é cada vez que o laço executa o seu bloco de código.

# Exemplo:
# Se um laço repetir 5 vezes, ele realizou 5 iterações.

# Cada passagem pelo laço é chamada de uma iteração.

# ============================
# VARIÁVEL DE CONTROLE
# ============================

# A variável de controle é a variável que acompanha o andamento do laço.

# Ela muda de valor a cada iteração e ajuda a controlar
# quantas vezes o laço será executado.

# No laço for, normalmente essa variável é chamada de i,
# mas ela pode ter qualquer nome.

# Exemplo:
# for i in range(5):
#     print(i)

# Nesse exemplo, a variável de controle é "i".

# ============================
# O LAÇO FOR
# ============================

# O for é usado quando sabemos quantas vezes
# queremos repetir uma ação.

# Ele percorre uma sequência de valores
# e executa o bloco de código para cada valor.

# Sintaxe básica:
#
# for variavel in range(valor):
#     bloco de código

# ============================
# FUNÇÃO RANGE()
# ============================

# A função range() gera uma sequência de números.

# range(5)
# Gera: 0, 1, 2, 3, 4

# range(inicio, fim)
# Exemplo:
# range(2, 6)
# Gera: 2, 3, 4, 5

# range(inicio, fim, passo)
# Exemplo:
# range(0, 10, 2)
# Gera: 0, 2, 4, 6, 8

# O último número informado no range()
# nunca é incluído na sequência.

# ============================
# RESUMINDO
# ============================

# Laço de repetição:
# Estrutura que repete um bloco de código.

# Iteração:
# Cada execução do bloco dentro do laço.

# Variável de controle:
# Variável que muda de valor a cada repetição
# e controla o andamento do laço.

# For:
# Utilizado quando sabemos a quantidade de repetições.

# Range():
# Gera a sequência de valores utilizada pelo for.



# ============================
# VOCABULÁRIO DO FOR
# ============================

# for = para / para cada
# (Não significa "laço". O laço de repetição é chamado de "loop".)

# loop = laço de repetição

# iteration = iteração

# control variable = variável de controle

# in = em / dentro de

# range = intervalo / sequência de números

# print = imprimir / mostrar na tela




# ==========================================
# FOR + ELSE
# ==========================================

# O else também pode ser usado com o for.

# O bloco do else será executado quando o for
# terminar todas as repetições normalmente.

# Ou seja:
# Se o for chegar ao final sem ser interrompido
# por um break, o else será executado.

# Sintaxe:

# for variavel in range(...):
#     código que será repetido
# else:
#     código executado quando o for terminar

# ==========================================
# EXEMPLO 1 - PERSONAGEM ANDANDO
# ==========================================

# Imagine um personagem que precisa dar 5 passos.

# Passo 1
# Passo 2
# Passo 3
# Passo 4
# Passo 5

# Quando terminar todos os passos,
# ele diz:
# "Cheguei ao destino!"

# Código:

# for passo in range(5):
#     print("Andou um passo.")
# else:
#     print("Cheguei ao destino!")

# Resultado:
#
# Andou um passo.
# Andou um passo.
# Andou um passo.
# Andou um passo.
# Andou um passo.
# Cheguei ao destino!

# ==========================================
# EXEMPLO 2 - COLETANDO MOEDAS
# ==========================================

# Imagine um jogo onde existem 3 moedas.

# O personagem pega:
# Moeda 1
# Moeda 2
# Moeda 3

# Depois aparece:
# "Todas as moedas foram coletadas!"

# Código:

# for moeda in range(3):
#     print("Pegou uma moeda.")
# else:
#     print("Todas as moedas foram coletadas!")

# ==========================================
# EXEMPLO 3 - BREAK
# ==========================================

# Agora imagine que apareceu um inimigo.

# O personagem anda...
# Mas encontra um inimigo.
# O laço é interrompido com break.

# Como o for NÃO terminou normalmente,
# o else NÃO será executado.

# Exemplo:

# for passo in range(5):
#     if passo == 2:
#         print("Encontrou um inimigo!")
#         break
#
#     print("Andou um passo.")
#
# else:
#     print("Cheguei ao destino!")

# Resultado:
#
# Andou um passo.
# Andou um passo.
# Encontrou um inimigo!

# Observe que:
# "Cheguei ao destino!"
# NÃO apareceu.

# ==========================================
# RESUMINDO
# ==========================================

# for = para cada

# else = senão / ao terminar normalmente

# break = interrompe imediatamente o laço

# Se houver break:
# O else NÃO é executado.

# Se NÃO houver break:
# O else É executado.

# Uma forma fácil de lembrar é:

# "O else do for significa:
# terminei todas as repetições com sucesso."


# ==========================================
# CONTAGEM CRESCENTE
# ==========================================

# Contando de 1 até 6.

# range(1, 7)
# Começa no número 1.
# Para antes do 7.
# Resultado: 1, 2, 3, 4, 5, 6

# Código:

# for numero in range(1, 7):
#     print(numero)

# Saída:
# 1
# 2
# 3
# 4
# 5
# 6


# ==========================================
# CONTAGEM DECRESCENTE
# ==========================================

# Contando de 6 até 1.

# range(6, 0, -1)
# Começa no 6.
# Para antes do 0.
# O passo é -1, ou seja, diminui de um em um.

# Código:

# for numero in range(6, 0, -1):
#     print(numero)

# Saída:
# 6
# 5
# 4
# 3
# 2
# 1


# ==========================================
# COMO FUNCIONA O RANGE()
# ==========================================

# range(início, fim, passo)

# início = onde começa.
# fim = onde termina (o último número NÃO é incluído).
# passo = de quanto em quanto vai aumentar ou diminuir.

# Exemplos:

# range(1, 7)
# Resultado: 1, 2, 3, 4, 5, 6

# range(6, 0, -1)
# Resultado: 6, 5, 4, 3, 2, 1

# range(0, 11, 2)
# Resultado: 0, 2, 4, 6, 8, 10

# range(10, 0, -2)
# Resultado: 10, 8, 6, 4, 2


# ==========================================
# DICA PARA MEMORIZAR
# ==========================================

# Para subir:
# Começa menor.
# Termina maior.
# Passo positivo (+1, +2, +3...)

# Para descer:
# Começa maior.
# Termina menor.
# Passo negativo (-1, -2, -3...)


# ==========================================
# O QUE É O "n"?
# ==========================================

# O "n" é uma variável.

# Ela serve para guardar o número digitado pelo usuário.

# Exemplo:

# n = int(input("Digite um número: "))

# Se o usuário digitar 3,
# a variável n passa a valer 3.

# Ou seja:

# n = 3

# ==========================================
# POR QUE FOI USADO "n + 1"?
# ==========================================

# A função range() NÃO inclui o último número.

# Ela sempre para antes do valor final.

# Exemplo:

# range(0, 3)

# Resultado:
# 0
# 1
# 2

# Observe que o 3 NÃO aparece.

# Agora veja:

# range(0, 4)

# Resultado:
# 0
# 1
# 2
# 3

# Como queremos mostrar o número digitado pelo usuário,
# precisamos acrescentar +1.

# ==========================================
# EXEMPLO COMPLETO
# ==========================================

# n = int(input("Digite um número: "))
#
# for c in range(0, n + 1):
#     print(c)
#
# print("Fim")

# ==========================================
# SE O USUÁRIO DIGITAR 3
# ==========================================

# n = 3

# O Python transforma:

# range(0, n + 1)

# em

# range(0, 4)

# Então o laço faz:

# 0
# 1
# 2
# 3

# Depois imprime:

# Fim

# ==========================================
# O QUE É O "c"?
# ==========================================

# O "c" é a variável de controle do for.

# Ela recebe um valor diferente a cada repetição.

# Primeira repetição:
# c = 0

# Segunda repetição:
# c = 1

# Terceira repetição:
# c = 2

# Quarta repetição:
# c = 3

# ==========================================
# RESUMINDO
# ==========================================

# n = número digitado pelo usuário.

# c = variável de controle do laço.

# n + 1 = faz com que o último número digitado
# também seja mostrado.

# Sem o +1:
# range(0, 3)
# Resultado: 0, 1, 2

# Com o +1:
# range(0, 3 + 1)
# Resultado: 0, 1, 2, 3

# DICA PARA MEMORIZAR:

# Sempre que usar range(início, fim),
# lembre-se:
# O "fim" nunca é incluído.

# Se quiser incluir o último número,
# use +1.


# ==========================================
# COMO SOMAR VÁRIOS NÚMEROS
# ==========================================

# Antes de começar a repetição,
# criamos uma variável para guardar a soma.

# Essa variável normalmente se chama:
# soma
# s
# total

# Ela começa com o valor 0.

# Exemplo:

# soma = 0

# Por que começa em 0?

# Porque ainda não somamos nenhum número.

# ==========================================
# O OPERADOR +=
# ==========================================

# O símbolo += significa:

# "Pegue o valor que já existe
# e some com o novo valor."

# Exemplo:

# soma += numero

# É exatamente a mesma coisa que escrever:

# soma = soma + numero

# As duas linhas fazem a mesma operação.

# ==========================================
# EXEMPLO PASSO A PASSO
# ==========================================

# O usuário vai digitar 4 números.

# Primeiro número: 5

# soma = 0

# soma += 5

# Agora:

# soma = 5

# --------------------------

# Segundo número: 8

# soma += 8

# É o mesmo que:

# soma = 5 + 8

# Resultado:

# soma = 13

# --------------------------

# Terceiro número: 2

# soma += 2

# Resultado:

# soma = 15

# --------------------------

# Quarto número: 10

# soma += 10

# Resultado:

# soma = 25

# No final:

# A soma de todos os números é 25.

# ==========================================
# CÓDIGO COMPLETO
# ==========================================

# soma = 0

# for c in range(4):
#     numero = int(input("Digite um número: "))
#     soma += numero

# print("A soma de todos os valores é:", soma)

# ==========================================
# O QUE ACONTECE DENTRO DO FOR?
# ==========================================

# Repetição 1:
# Digita 5
# soma = 0 + 5 = 5

# Repetição 2:
# Digita 8
# soma = 5 + 8 = 13

# Repetição 3:
# Digita 2
# soma = 13 + 2 = 15

# Repetição 4:
# Digita 10
# soma = 15 + 10 = 25

# Resultado final:
# A soma de todos os valores é: 25

# ==========================================
# DICA PARA MEMORIZAR
# ==========================================

# Sempre que precisar somar vários números:

# 1. Crie uma variável com valor 0.
# 2. Faça a repetição.
# 3. Use:

# soma += numero

# Isso significa:

# soma = soma + numero

# Pense assim:

# "A variável soma é uma caixinha."

# Cada número novo é colocado dentro dela.

# A cada repetição, a caixinha fica com um valor maior.

# No final, ela guarda a soma de todos os números.




