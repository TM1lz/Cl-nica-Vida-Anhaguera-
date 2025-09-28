# cadastro.py
pacientes = []

def cadastrar_paciente(nome, idade, telefone):
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print(f"Paciente {nome} cadastrado com sucesso!")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        print("\n=== Lista de Pacientes ===")
        for i, p in enumerate(pacientes, 1):
            print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
