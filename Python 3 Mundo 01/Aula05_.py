# MANIPULANDO CADEIAS DE TEXTOS

# Nova frase 💪
frase = "Eu sou a melhor programadora que conheço"

# Índices (posição de cada letra)
# 'E'(0) 'u'(1) ' '(2) 's'(3) 'o'(4) 'u'(5) ' '(6) 'a'(7) ' '(8)
# 'm'(9) 'e'(10) 'l'(11) 'h'(12) 'o'(13) 'r'(14) ' '(15)
# 'p'(16) 'r'(17) 'o'(18) 'g'(19) 'r'(20) 'a'(21) 'm'(22) 'a'(23) 'd'(24) 'o'(25) 'r'(26) 'a'(27) ' '(28)
# 'q'(29) 'u'(30) 'e'(31) ' '(32) 'c'(33) 'o'(34) 'n'(35) 'h'(36) 'e'(37) 'ç'(38) 'o'(39)

# 🔹 Acessando um caractere específico
print(frase[9])
# Resultado: 'm'

# 🔹 Do índice 9 até 13 (14 não entra)
print(frase[9:14])
# Resultado: 'melho'

# 🔹 Do índice 9 até 20 (21 não entra)
print(frase[9:21])
# Resultado: 'melhor progr'

# 🔹 Do índice 9 até 20 pulando de 2 em 2
print(frase[9:21:2])
# Resultado: 'mlo rga'

# 🔹 Do começo até o índice 4
print(frase[:5])
# Resultado: 'Eu so'

# 🔹 Do índice 9 até o final
print(frase[9:])
# Resultado: 'melhor programadora que conheço'

# 🔹 Do índice 9 até o final pulando de 3 em 3
print(frase[9::3])
# Resultado: 'mh gmdrq oç'