# Listas para armazenar os dados
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")

        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            menu_operacoes("Estudantes", estudantes)
        elif opcao == '2':
            menu_operacoes("Disciplinas", disciplinas)
        elif opcao == '3':
            menu_operacoes("Professores", professores)
        elif opcao == '4':
            menu_operacoes("Turmas", turmas)
        elif opcao == '5':
            menu_operacoes("Matrículas", matriculas)
        elif opcao == '6':
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_operacoes(tipo, lista):
    while True:
        print(f"\n[{tipo}] MENU DE OPERAÇÕES")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Informe a ação desejada: ")

        if opcao == '1':
            incluir(lista, tipo)
        elif opcao == '2':
            listar(lista, tipo)
        elif opcao == '3':
            atualizar(lista, tipo)
        elif opcao == '4':
            excluir(lista, tipo)
        elif opcao == '5':
            break  # Volta ao menu principal
        else:
            print("Opção inválida. Tente novamente.")

def incluir(lista, tipo):
    item = input(f"Informe o novo {tipo[:-1]}: ")
    lista.append(item)
    print(f"{tipo[:-1]} incluído(a) com sucesso!")

def listar(lista, tipo):
    if not lista:
        print(f"Não há {tipo.lower()} cadastrados.")
    else:
        print(f"Lista de {tipo.lower()}:")
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")

def atualizar(lista, tipo):
    listar(lista, tipo)
    if lista:
        indice = int(input("Informe o número do item que deseja atualizar: ")) - 1
        if 0 <= indice < len(lista):
            novo_valor = input(f"Informe o novo valor para {tipo[:-1]}: ")
            lista[indice] = novo_valor
            print(f"{tipo[:-1]} atualizado(a) com sucesso!")
        else:
            print("Número inválido.")

def excluir(lista, tipo):
    listar(lista, tipo)
    if lista:
        indice = int(input("Informe o número do item que deseja excluir: ")) - 1
        if 0 <= indice < len(lista):
            excluido = lista.pop(indice)
            print(f"{tipo[:-1]} '{excluido}' excluído(a) com sucesso!")
        else:
            print("Número inválido.")

# Iniciar o programa
menu_principal()
