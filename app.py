# Controlador de nível de reservatório de água

# Importação da biblioteca colorama para exibir cores no terminal
from colorama import Fore, Style

# Lista de níveis e situações do reservatório
niveis_reservatorio = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função para definir a cor do alerta com base no nível do reservatório
def definir_cor_alerta(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibição dos níveis e situações do reservatório com as cores correspondentes
print("CONTROLADOR DE NÍVEL DO RESERVATÓRIO DE ÁGUA\n")

for i in range(len(niveis_reservatorio)):
    cor_alerta = definir_cor_alerta(i + 1)
    print(f"{cor_alerta}{niveis_reservatorio[i]}{Style.RESET_ALL}")