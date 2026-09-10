# ==========================================
#           TABUADA COLORIDA
# ==========================================

# CORES
azul = "\033[34m"
ciano = "\033[36m"
amarelo = "\033[33m"
verde = "\033[32m"
roxo = "\033[35m"
reset = "\033[0m"

# ------------------------------------------
# TÍTULO
# ------------------------------------------

print(f"{azul}╔══════════════════════════════════╗{reset}")
print(f"{azul}║          📚 TABUADA 📚           ║{reset}")
print(f"{azul}╚══════════════════════════════════╝{reset}")

# ------------------------------------------
# ENTRADA DO USUÁRIO
# ------------------------------------------

n = int(input(f"{amarelo}Digite o número da tabuada que deseja: {reset}"))

# ------------------------------------------
# TABUADA
# ------------------------------------------

print()
print(f"{roxo}✨ TABUADA DO {n} ✨{reset}")
print()

for i in range(1, 11):
    print(f"{ciano}{n} X {i:2} = {n * i}{reset}")

# ------------------------------------------
# FINAL
# ------------------------------------------

print()
print(f"{verde}╔══════════════════════════════════╗{reset}")
print(f"{verde}║       ✨ FIM DA TABUADA ✨       ║{reset}")
print(f"{verde}╚══════════════════════════════════╝{reset}")

