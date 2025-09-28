# agendamento.py
from pacientes.cadastro import pacientes

consultas = []

def agendar_consulta(nome_paciente, data, hora):
    # verifica se paciente está cadastrado
    paciente = next((p for p in pacientes if p['nome'].lower() == nome_paciente.lower()), None)
    if paciente:
        consulta = {
            "paciente": nome_paciente,
            "data": data,
            "hora": hora,
            "status": "Agendada"
        }
        consultas.append(consulta)
        print(f"Consulta agendada para {nome_paciente} em {data} às {hora}.")
    else:
        print("Paciente não cadastrado. Cadastre antes de agendar.")

def confirmar_consulta(nome_paciente, data, hora):
    for c in consultas:
        if c['paciente'].lower() == nome_paciente.lower() and c['data'] == data and c['hora'] == hora:
            c['status'] = "Confirmada"
            print(f"Consulta de {nome_paciente} confirmada.")
            return
    print("Consulta não encontrada.")

def cancelar_consulta(nome_paciente, data, hora):
    for c in consultas:
        if c['paciente'].lower() == nome_paciente.lower() and c['data'] == data and c['hora'] == hora:
            consultas.remove(c)
            print(f"Consulta de {nome_paciente} cancelada.")
            return
    print("Consulta não encontrada.")
