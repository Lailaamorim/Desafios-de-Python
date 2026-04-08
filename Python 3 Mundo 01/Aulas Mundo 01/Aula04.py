# ============================
# AULA: MÓDULOS EM PYTHON
# ============================

# O que são módulos?
# Módulos são arquivos que contêm códigos prontos (funções, variáveis, classes)
# que você pode reutilizar em seus programas.
# Eles ajudam a evitar repetir código e tornam o programa mais organizado.

# --------------------------------
# IMPORTANDO MÓDULOS (import)
# --------------------------------

# Para usar um módulo, usamos o comando import:

import math  # importa o módulo matemático

# Agora podemos usar funções do módulo usando "nome_do_modulo.função"
print(math.sqrt(25))  # raiz quadrada de 25 → resultado: 5.0

# --------------------------------
# IMPORTANDO PARTES DO MÓDULO (from ... import)
# --------------------------------

# Podemos importar apenas o que queremos usar:

from math import sqrt

print(sqrt(36))  # agora não precisa usar "math."

# Também podemos importar várias funções:

from math import sqrt, ceil

print(sqrt(49))   # 7.0
print(ceil(4.3))  # arredonda para cima → 5

# --------------------------------
# USANDO "as" (apelidos)
# --------------------------------

# Podemos dar apelidos para módulos ou funções:

import math as m

print(m.sqrt(16))  # usamos "m" no lugar de "math"

# --------------------------------
# MÓDULOS BUILT-IN (já vêm com Python)
# --------------------------------

# Exemplos de módulos que já vêm com o Python:
import random
import datetime

print(random.randint(1, 10))  # número aleatório entre 1 e 10

# --------------------------------
# MÓDULOS EXTERNOS
# --------------------------------

# São módulos que NÃO vêm com o Python e precisam ser instalados.
# Exemplo: biblioteca "requests"

# Para instalar (no terminal):
# pip install requests

# Depois de instalado:
# import requests

# --------------------------------
# RESUMO
# --------------------------------

# import modulo → importa tudo
# from modulo import algo → importa só o necessário
# import modulo as apelido → cria um nome curto

# Módulos ajudam a:
# - Reutilizar código
# - Organizar melhor os programas
# - Usar recursos prontos (matemática, datas, internet, etc.)