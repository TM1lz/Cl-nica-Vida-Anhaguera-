# fila_atendimento.py

fila = []

def adicionar_paciente(nome, cpf):
    fila.append({"nome": nome, "cpf": cpf})

def atender_primeiro():
    if fila:
        atendido = fila.pop(0)
        print(f"Paciente atendido: {atendido['nome']}")
        return atendido
    else:
        print("Fila vazia.")
        return None

def listar_fila():
    if fila:
        print("\nPacientes na fila:")
        for p in fila:
            print(f"Nome: {p['nome']} | CPF: {p['cpf']}")
    else:
        print("Fila vazia.")
