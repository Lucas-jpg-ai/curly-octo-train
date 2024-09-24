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

# Função para validar códigos já existentes (não duplicados)
def validar_codigo_existente(lista, codigo):
    return any(item['codigo'] == codigo for item in lista)

# Função para incluir dados
def incluir(lista, tipo):
    if tipo == "Estudantes":
        codigo = int(input("Informe o código do estudante: "))
        if validar_codigo_existente(lista, codigo):
            print("Código já existente. Tente novamente.")
            return
        nome = input("Informe o nome do estudante: ")
        cpf = input("Informe o CPF do estudante: ")
        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista.append(estudante)
        print("Estudante incluído(a) com sucesso!")
    elif tipo == "Disciplinas":
        codigo = int(input("Informe o código da disciplina: "))
        if validar_codigo_existente(lista, codigo):
            print("Código já existente. Tente novamente.")
            return
        nome = input("Informe o nome da disciplina: ")
        disciplina = {"codigo": codigo, "nome": nome}
        lista.append(disciplina)
        print("Disciplina incluída com sucesso!")
    elif tipo == "Professores":
        codigo = int(input("Informe o código do professor: "))
        if validar_codigo_existente(lista, codigo):
            print("Código já existente. Tente novamente.")
            return
        nome = input("Informe o nome do professor: ")
        cpf = input("Informe o CPF do professor: ")
        professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista.append(professor)
        print("Professor incluído com sucesso!")
    elif tipo == "Turmas":
        codigo = int(input("Informe o código da turma: "))
        if validar_codigo_existente(lista, codigo):
            print("Código já existente. Tente novamente.")
            return
        cod_professor = int(input("Informe o código do professor: "))
        cod_disciplina = int(input("Informe o código da disciplina: "))
        turma = {"codigo": codigo, "cod_professor": cod_professor, "cod_disciplina": cod_disciplina}
        lista.append(turma)
        print("Turma incluída com sucesso!")
    elif tipo == "Matrículas":
        codigo_turma = int(input("Informe o código da turma: "))
        codigo_estudante = int(input("Informe o código do estudante: "))
        matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
        lista.append(matricula)
        print("Matrícula incluída com sucesso!")

# Função para listar dados
def listar(lista, tipo):
    if not lista:
        print(f"Não há {tipo.lower()} cadastrados.")
    else:
        print(f"Lista de {tipo.lower()}:")
        for item in lista:
            print(item)

# Função para atualizar dados
def atualizar(lista, tipo):
    listar(lista, tipo)
    if lista:
        codigo = int(input(f"Informe o código do {tipo[:-1]} que deseja atualizar: "))
        for item in lista:
            if item["codigo"] == codigo:
                for chave in item:
                    if chave != "codigo":
                        item[chave] = input(f"Informe o novo valor para {chave}: ")
                print(f"{tipo[:-1]} atualizado(a) com sucesso!")
                return
        print(f"{tipo[:-1]} não encontrado(a).")

# Função para excluir dados
def excluir(lista, tipo):
    listar(lista, tipo)
    if lista:
        codigo = int(input(f"Informe o código do {tipo[:-1]} que deseja excluir: "))
        for item in lista:
            if item["codigo"] == codigo:
                lista.remove(item)
                print(f"{tipo[:-1]} excluído(a) com sucesso!")
                return
        print(f"{tipo[:-1]} não encontrado(a).")

# Iniciar o programa
if __name__ == "__main__":
    menu_principal()
