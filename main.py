# main.py

from pacientes import cadastro, estatisticas, busca
from fila import fila_atendimento
from controle_acesso import acesso
from consultas import agendamento

def menu():
    while True:
        print("\n=== CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Estatísticas de pacientes")
        print("3. Buscar paciente")
        print("4. Listar pacientes")
        print("5. Gerenciar fila de atendimento")
        print("6. Agendar consulta")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Idade inválida. Digite um número inteiro.")
                continue
            telefone = input("Telefone: ")
            cadastro.cadastrar_paciente(nome, idade, telefone)

        elif opcao == "2":
            total = estatisticas.numero_total()
            media = estatisticas.idade_media()
            novo = estatisticas.paciente_mais_novo()
            velho = estatisticas.paciente_mais_velho()

            print(f"Número total de pacientes: {total}")
            print(f"Idade média: {media:.2f}")
            if novo and velho:
                print(f"Paciente mais novo: {novo['nome']} ({novo['idade']})")
                print(f"Paciente mais velho: {velho['nome']} ({velho['idade']})")

        elif opcao == "3":
            nome = input("Digite o nome do paciente: ")
            p = busca.buscar_paciente(nome)
            if p:
                print(f"Encontrado: Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
            else:
                print("Paciente não encontrado.")

        elif opcao == "4":
            cadastro.listar_pacientes()

        elif opcao == "5":
            print("\n--- Gerenciar Fila ---")
            print("1. Adicionar paciente à fila")
            print("2. Atender primeiro paciente")
            print("3. Listar fila")
            sub = input("Escolha: ")

            if sub == "1":
                nome = input("Nome do paciente: ")
                cpf = input("CPF: ")
                fila_atendimento.adicionar_paciente(nome, cpf)
            elif sub == "2":
                fila_atendimento.atender_primeiro()
            elif sub == "3":
                fila_atendimento.listar_fila()
            else:
                print("Opção inválida.")

        elif opcao == "6":
            nome = input("Nome do paciente: ")
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            agendamento.agendar_consulta(nome, data, hora)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
1