# ORDEM DE PRECEDÊNCIA DOS OPERADORES EM PYTHON
# --------------------------------------------
# A ordem de precedência define QUAL operação será feita primeiro
# quando temos várias operações na mesma expressão.

# A ordem correta é:

# 1º -> Parênteses ()
# 2º -> Potenciação **
# 3º -> Multiplicação *, Divisão /, Divisão inteira //, Módulo %
# 4º -> Soma + e Subtração -

# OBS: Colchetes [] e chaves {} não são usados para precedência matemática,
# eles servem para listas e dicionários. O que manda na matemática são os ().

# --------------------------------------------
# EXEMPLOS NA PRÁTICA:

# EXEMPLO 1:
resultado1 = 10 + 5 * 2
print(resultado1)
# Aqui o Python faz primeiro a multiplicação:
# 5 * 2 = 10
# Depois soma:
# 10 + 10 = 20

# EXEMPLO 2:
resultado2 = (10 + 5) * 2
print(resultado2)
# Agora os parênteses vêm primeiro:
# 10 + 5 = 15
# Depois multiplica:
# 15 * 2 = 30

# EXEMPLO 3:
resultado3 = 2 + 3 ** 2
print(resultado3)
# Primeiro potência:
# 3 ** 2 = 9
# Depois soma:
# 2 + 9 = 11

# EXEMPLO 4:
resultado4 = 20 / 5 * 2
print(resultado4)
# Mesma prioridade (/ e *), então resolve da esquerda para a direita:
# 20 / 5 = 4
# 4 * 2 = 8

# EXEMPLO 5:
resultado5 = 10 + 20 % 3
print(resultado5)
# Primeiro o módulo:
# 20 % 3 = 2
# Depois soma:
# 10 + 2 = 12

# --------------------------------------------
# RESUMO SIMPLES:
# ()  -> primeiro
# **  -> depois
# *, /, //, % -> depois (da esquerda para direita)
# +, - -> por último

# --------------------------------------------
# DICA IMPORTANTE:
# Sempre use parênteses () quando quiser deixar o código mais claro
# e evitar erros na ordem das contas.