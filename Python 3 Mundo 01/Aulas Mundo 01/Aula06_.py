# ==================================================
# AULA: CONDIÇÕES SIMPLES E COMPOSTAS EM PYTHON
# ==================================================

# Condições servem para o programa tomar decisões
# Exemplo da vida real:
# Se estiver chovendo, levo guarda-chuva

# Em Python usamos:
# if, else, elif

# ==================================================
# 1. CONDIÇÃO SIMPLES (if)
# ==================================================

# A condição simples testa apenas uma situação

idade = 18

# Se idade for maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade")

# Se a condição for falsa, nada acontece

# ==================================================
# 2. CONDIÇÃO COMPOSTA (if + else)
# ==================================================

# Aqui temos dois caminhos: verdadeiro ou falso

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# ==================================================
# 3. CONDIÇÃO COMPOSTA COM MÚLTIPLAS OPÇÕES (elif)
# ==================================================

# Usamos quando temos mais de duas possibilidades

nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# O Python verifica de cima para baixo

# ==================================================
# 4. OPERADORES DE COMPARAÇÃO
# ==================================================

# ==  igual
# !=  diferente
# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual

# Exemplo:
numero = 10

if numero == 10:
    print("O número é 10")

# ==================================================
# 5. OPERADORES LÓGICOS
# ==================================================

# Permitem combinar condições

# AND (e) -> tudo precisa ser verdadeiro
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

# OR (ou) -> apenas uma condição precisa ser verdadeira
if idade >= 18 or tem_carteira:
    print("Pode tentar dirigir")

# NOT (não) -> inverte o valor
tem_dinheiro = False

if not tem_dinheiro:
    print("Sem dinheiro")

# ==================================================
# 6. INDENTAÇÃO (MUITO IMPORTANTE)
# ==================================================

# Python usa espaços para definir blocos de código

if True:
    print("Correto")  # está dentro do if

# if True:
# print("Erro")  # errado (sem indentação)

# ==================================================
# 7. EXEMPLO COMPLETO
# ==================================================

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar")
elif idade < 18 or idade > 65:
    print("Voto opcional")
else:
    print("Voto obrigatório")

# ==================================================
# RESUMO
# ==================================================

# if     -> condição simples
# else   -> alternativa
# elif   -> múltiplas condições
# and    -> e
# or     -> ou
# not    -> não

# Sempre prestar atenção na indentação!