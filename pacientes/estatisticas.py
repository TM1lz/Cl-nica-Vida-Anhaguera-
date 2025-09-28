# estatisticas.py
from pacientes.cadastro import pacientes

def numero_total():
    return len(pacientes)

def idade_media():
    if pacientes:
        return sum(p['idade'] for p in pacientes) / len(pacientes)
    return 0

def paciente_mais_novo():
    if pacientes:
        return min(pacientes, key=lambda x: x['idade'])
    return None

def paciente_mais_velho():
    if pacientes:
        return max(pacientes, key=lambda x: x['idade'])
    return None
