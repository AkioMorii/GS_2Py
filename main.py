import os

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    hospital_destino = input("Digite o hospital de destino: ")

    paciente = {'nome': nome, 'idade': idade, 'hospital_destino': hospital_destino}

    with open('pacientes.txt', 'a') as file:
        file.write(f"{nome},{idade},{hospital_destino}\n")

    print(f"Paciente {nome} cadastrado com sucesso!")

def listar_pacientes():
    print("Lista de Pacientes:")
    with open('pacientes.txt', 'r') as file:
        for line in file:
            nome, idade, hospital_destino = line.strip().split(',')
            print(f"Nome: {nome}, Idade: {idade}, Hospital de Destino: {hospital_destino}")

def encaminhar_pacientes():
    hospital = input("Digite o nome do hospital para encaminhar pacientes: ")

    pacientes_encaminhados = 0
    with open('pacientes.txt', 'r') as file:
        linhas = file.readlines()

    with open('pacientes.txt', 'w') as file:
        for linha in linhas:
            nome, idade, hospital_destino = linha.strip().split(',')
            if hospital_destino == hospital:
                pacientes_encaminhados += 1
            else:
                file.write(linha)

    print(f"Foram encaminhados {pacientes_encaminhados} pacientes para o hospital {hospital}.")

def menu():
    while True:
        print("\n----- Sistema de Encaminhamento de Pacientes -----")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Encaminhar Pacientes para Hospital")
        print("4. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            encaminhar_pacientes()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
