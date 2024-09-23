def formatar_titulo(texto, largura_total=50, simbolo='-'):
    """
    Função que enfeita o menu de acordo com o tamanho da palavra recebida como parâmetro
    """
    largura_texto = len(texto)
    largura_tracos = (largura_total - largura_texto) // 2
    linha_formatada = simbolo * largura_tracos + texto + simbolo * largura_tracos

    if len(linha_formatada) < largura_total:
        linha_formatada += simbolo

    return linha_formatada


def cadastrar_funcionario():
    """
    Função responsável por inserir os dados dos funcionários na lista lista_funcionarios
    Recebe um id pré-definido como parâmetro
    """
    global id_global
    while True:
        menu_cadastro = formatar_titulo(" MENU CADASTRAR FUNCIONARIO ", 50, '-')
        print()
        # Insere traços conforme o tamanho da variável dentro de len()
        print("-" * len(menu_cadastro))
        print(menu_cadastro)
        print(f"Id: {id_global}")

        # Entrada dos dados dos funcionários, com verificação de dados
        while True:
            nome_f = input("Por favor, entre com o nome do Funcionário: ").capitalize()
            if nome_f.strip() and nome_f.replace(" ", "").isalpha():
                break
            else:
                print("Nome inválido. Por favor, digite um nome que contenha apenas letras.")
        while True:
            setor_f = input("Por favor, entre com o setor do Funcionário: ")
            if setor_f.strip() and setor_f.replace(" ", "").isalpha():
                break
            else:
                print("Setor inválido. Por favor, digite um nome que contenha apenas letras.")
        while True:
            try:
                salario_f = float(input("Por favor, entre com o salário do Funcionário: "))
                if salario_f > 0:
                    break
                else:
                    print("O salário deve ser um valor positivo")
                    continue
            except ValueError:
                print("Insira um valor numérico")

        funcionario = {
            "id":  id_global,
            "nome": nome_f,
            "setor": setor_f,
            "salario": salario_f
        }
        lista_funcionarios.append(funcionario.copy())
        id_global += 1
        print("Funcionário cadastrado com sucesso!\n")
        cadastrar_outro = input("Deseja cadastrar outro funcionário? (S/N) ").upper()
        if cadastrar_outro == "S":
            continue
        else:
            return


def consultar_funcionarios():
    """
    Função responsável por fazer a consulta dos funcionários de acordo com a opção desejada
    """
    while True:
        try:
            menu_consulta = formatar_titulo(" MENU CONSULTAR FUNCIONARIO ", 50, '-')
            print()
            # Insere traços conforme o tamanho da variável dentro de len()
            print("-" * len(menu_consulta))
            print(menu_consulta)

            print("Escolha a opção desejada: ")
            print("1 - Consultar todos os Funcionários")
            print("2 - Consultar Funcionário por ID")
            print("3 - Consultar Funcionário(s) por setor")
            print("4 - Retornar ao menu")

            escolha_cons = int(input(">> "))

            print("-" * 50)
            print()
            match escolha_cons:
                # Todos os funcionários
                case 1:
                    for funcionario in lista_funcionarios:
                        for chave, valor in funcionario.items():
                            print(f"{chave.capitalize()}: {valor}")
                        print()
                    print()
                # Por ID
                case 2:
                    id_cons = int(input("Digite o ID do funcionário: "))
                    existencia_funcionario = False
                    for funcionario in lista_funcionarios:
                        if funcionario.get("id") == id_cons:
                            existencia_funcionario = True
                            for chave, valor in funcionario.items():
                                print(f"{chave.capitalize()}:  {valor}")
                            print()
                    if not existencia_funcionario:
                        print("Este funcionário não está cadastrado")
                        continue
                # Por setor
                case 3:
                    setor_cons = input("Digite o setor do(s) funcionário(s): ").upper()
                    existencia_funcionario = False
                    for funcionario in lista_funcionarios:
                        # upper() para comparação com todas em letra maiuscula
                        if funcionario.get("setor") and funcionario.get("setor").upper() == setor_cons:
                            existencia_funcionario = True
                            for chave, valor in funcionario.items():
                                print(f"{chave.capitalize()}: {valor}")
                            print()
                    if not existencia_funcionario:
                        print("Não existem funcionários neste setor")
                        continue
                case 4:
                    return
                case _:
                    # Para tratar números inteiros fora da faixa
                    print("Opção inválida")
                    continue
        # Para que o programa não falhe por entrada diferente de n° inteiro
        except ValueError:
            print("Entrada inválida, tente novamente!")
            continue


def atualizar_funcionario():
    """"
    Função responsável por possibilitar a alteração dos dados de um funcionário, exceto ID
    """
    while True:
        try:
            menu_atualizacao = formatar_titulo(" MENU DE ALTERAÇÃO DE DADOS ", 50, '-')
            print("-" * len(menu_atualizacao))
            print(menu_atualizacao)
            print("Escolha a opção desejada: ")
            print("1 - Alterar nome do funcionário")
            print("2 - Alterar setor do funcionário")
            print("3 - Alterar salário do funcionário")
            print("4 - Voltar")
            escolha_atualizacao = int(input(">> "))

            if escolha_atualizacao == 4:
                return

            id_atualizacao = int(input("Digite o id do funcionário que você deseja alterar: "))
            existencia_funcionario = False

            for funcionario in lista_funcionarios:
                if funcionario.get("id") == id_atualizacao:
                    existencia_funcionario = True

                    match escolha_atualizacao:
                        case 1:
                            while True:
                                nome_atualizado = input(f"Funcionário {funcionario['nome']} localizado."
                                                        " Digite novo nome: ").capitalize()
                                if nome_atualizado.strip() and nome_atualizado.replace(" ", "").isalpha():
                                    funcionario["nome"] = nome_atualizado
                                    print("Nome atualizado com sucesso! \n")
                                    break
                                else:
                                    print("Nome inválido. Por favor, digite um nome que contenha apenas letras.")

                        case 2:
                            while True:
                                setor_atualizado = input(f"Funcionário {funcionario['nome']} localizado."
                                                         " Digite novo setor: ")
                                if setor_atualizado.strip() and setor_atualizado.replace(" ", "").isalpha():
                                    funcionario["setor"] = setor_atualizado
                                    print("Setor atualizado com sucesso! \n")
                                    break
                                else:
                                    print("Setor inválido. Por favor, digite um setor que contenha apenas letras.")

                        case 3:
                            while True:
                                try:
                                    salario_atualizado = float(input(f"Funcionário {funcionario['nome']} localizado."
                                                                     " Digite novo salário: "))
                                    if salario_atualizado>0:
                                        funcionario["salario"] = salario_atualizado
                                        print("Salário atualizado com sucesso! \n")
                                        break
                                    else:
                                        print("O salário precisa ser um valor positivo.")
                                        continue
                                except ValueError:
                                    print("Entrada inválida. Por favor, digite um valor numérico para o salário.")

                        case _:
                            print("Opção inválida! \n")
                    break

            if not existencia_funcionario:
                print("ID inválido. Funcionário não encontrado!\n")

        except ValueError:
            print("Opção inválida! Por favor, escolha uma das opções disponíveis.")


def remover_funcionario():
    """
    Função responsável por fazer a remoção de um funcionário utilizando a ID
    """
    menu_remocao = formatar_titulo(" MENU REMOVER FUNCIONARIO ", 50, '-')
    # Insere traços conforme o tamanho da variável dentro de len()
    print("-" * len(menu_remocao))
    print(menu_remocao)

    while True:
        try:
            id_remocao = int(input("Digite o ID do funcionário: "))
            existencia_funcionario = False
            for funcionario in lista_funcionarios:
                if funcionario.get("id") == id_remocao:
                    confirmacao = input("Esta ação não poderá ser desfeita. Tem certeza? (S/N):").upper()
                    if confirmacao == "N":
                        print()
                        return
                    lista_funcionarios.remove(funcionario)
                    print(f"Funcionário com ID {id_remocao} removido com sucesso.")
                    print("")
                    return
            if not existencia_funcionario:
                print("ID inválido. Funcionário não encontrado!\n")
                continue
        except ValueError:
            print("ID inválido. Digite um número inteiro!\n")
            continue


# Função Principal

# ID inicial é conforme requisitado pela instituição
id_global = 1
lista_funcionarios = []

while True:
    try:
        print("Bem vindo a Empresa da I")
        imprime_menu = formatar_titulo(" MENU PRINCIPAL ", 50, '-')
        # Insere traços conforme o tamanho da variável dentro de len()
        print("-" * len(imprime_menu))
        print(imprime_menu)

        print("Escolha a opção desejada: ")
        print("1 - Cadastrar Funcionários")
        print("2 - Consultar Funcionário(s)")
        print("3 - Atualizar Dados de Funcionário")
        print("4 - Remover Funcionário")
        print("5 - Sair")

        escolha = int(input(">> "))

        match escolha:
            case 1:
                cadastrar_funcionario()
            case 2:
                consultar_funcionarios()
            case 3:
                atualizar_funcionario()
            case 4:
                remover_funcionario()
            case 5:
                print("Encerrando...")
                break
            case _:
                # Trata casos onde o usuario digita um n° inteiro fora da faixa
                print("Opção inválida! \n")
                continue
    except ValueError:
        # Trata casos onde o usuário digita algo diferente de um número inteiro
        print("Opção inválida. Digite um número inteiro!\n")
