import json

# Funções para manipulação de arquivos JSON
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo)

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Funções para gerenciar estudantes, disciplinas, professores, turmas e matrículas
def carregar_todos_dados():
    global estudantes, disciplinas, professores, turmas, matriculas
    estudantes = carregar_dados("estudantes.json")
    disciplinas = carregar_dados("disciplinas.json")
    professores = carregar_dados("professores.json")
    turmas = carregar_dados("turmas.json")
    matriculas = carregar_dados("matriculas.json")

def salvar_todos_dados():
    salvar_dados("estudantes.json", estudantes)
    salvar_dados("disciplinas.json", disciplinas)
    salvar_dados("professores.json", professores)
    salvar_dados("turmas.json", turmas)
    salvar_dados("matriculas.json", matriculas)

# Listas para armazenar os dados (agora carregados do arquivo)
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

# Função para apresentar o Menu Principal
def menu_principal():
    carregar_todos_dados()  # Carrega os dados ao iniciar o programa
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
            menu_operacoes("Estudantes", estudantes, "estudantes.json")
        elif opcao == '2':
            menu_operacoes("Disciplinas", disciplinas, "disciplinas.json")
        elif opcao == '3':
            menu_operacoes("Professores", professores, "professores.json")
        elif opcao == '4':
            menu_operacoes("Turmas", turmas, "turmas.json")
        elif opcao == '5':
            menu_operacoes("Matrículas", matriculas, "matriculas.json")
        elif opcao == '6':
            print("Encerrando aplicação...")
            salvar_todos_dados()  # Salva os dados ao sair
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para apresentar o Menu de Operações
def menu_operacoes(tipo, lista, nome_arquivo):
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
            salvar_dados(nome_arquivo, lista)  # Salva ao incluir
        elif opcao == '2':
            listar(lista, tipo)
        elif opcao == '3':
            atualizar(lista, tipo)
            salvar_dados(nome_arquivo, lista)  # Salva ao atualizar
        elif opcao == '4':
            excluir(lista, tipo)
            salvar_dados(nome_arquivo, lista)  # Salva ao excluir
        elif opcao == '5':
            break  # Volta ao menu principal
        else:
            print("Opção inválida. Tente novamente.")

# Função para incluir dados
def incluir(lista, tipo):
    if tipo == "Estudantes":
        codigo = int(input("Informe o código do estudante: "))
        nome = input("Informe o nome do estudante: ")
        cpf = input("Informe o CPF do estudante: ")
        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista.append(estudante)
        print("Estudante incluído(a) com sucesso!")
    else:
        item = input(f"Informe o novo {tipo[:-1]}: ")
        lista.append(item)
        print(f"{tipo[:-1]} incluído(a) com sucesso!")

# Função para listar dados
def listar(lista, tipo):
    if not lista:
        print(f"Não há {tipo.lower()} cadastrados.")
    else:
        if tipo == "Estudantes":
            print(f"Lista de {tipo.lower()}:")
            for estudante in lista:
                print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
        else:
            print(f"Lista de {tipo.lower()}:")
            for i, item in enumerate(lista, 1):
                print(f"{i}. {item}")

# Função para atualizar dados
def atualizar(lista, tipo):
    if tipo == "Estudantes":
        listar(lista, tipo)
        if lista:
            codigo = int(input("Informe o código do estudante que deseja atualizar: "))
            for estudante in lista:
                if estudante["codigo"] == codigo:
                    estudante["nome"] = input("Informe o novo nome do estudante: ")
                    estudante["cpf"] = input("Informe o novo CPF do estudante: ")
                    print("Estudante atualizado(a) com sucesso!")
                    return
            print("Estudante não encontrado.")
    else:
        listar(lista, tipo)
        if lista:
            indice = int(input("Informe o número do item que deseja atualizar: ")) - 1
            if 0 <= indice < len(lista):
                novo_valor = input(f"Informe o novo valor para {tipo[:-1]}: ")
                lista[indice] = novo_valor
                print(f"{tipo[:-1]} atualizado(a) com sucesso!")
            else:
                print("Número inválido.")

# Função para excluir dados
def excluir(lista, tipo):
    if tipo == "Estudantes":
        listar(lista, tipo)
        if lista:
            codigo = int(input("Informe o código do estudante que deseja excluir: "))
            for estudante in lista:
                if estudante["codigo"] == codigo:
                    lista.remove(estudante)
                    print("Estudante excluído(a) com sucesso!")
                    return
            print("Estudante não encontrado.")
    else:
        listar(lista, tipo)
        if lista:
            indice = int(input("Informe o número do item que deseja excluir: ")) - 1
            if 0 <= indice < len(lista):
                excluido = lista.pop(indice)
                print(f"{tipo[:-1]} '{excluido}' excluído(a) com sucesso!")
            else:
                print("Número inválido.")

# Iniciar o programa
if __name__ == "__main__":
    menu_principal()
