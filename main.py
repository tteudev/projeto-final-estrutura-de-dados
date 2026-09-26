import atribuicoes_assistente
import atribuicoes_diretor
import atribuicoes_secretario

MENU_SECRETARIO = [
    "(1) Cadastrar nova pessoa na lista de espera.",
    "(2) Consultar pessoa cadastrada.",
    "(3) Ver quantidade de pessoas cadastradas.",
    "(4) Finalizar execução.",
]

MENU_DIRETOR = [
    "(1) Alterar nome, idade ou telefone de pessoa cadastrada.",
    "(2) Descadastrar pessoa.",
    "(3) Obter informações da primeira pessoa em ordem alfabética de nome.",
    "(4) Obter informações da última pessoa em ordem alfabética de nome.",
    "(5) Confirmar validade da lista de espera e finalizar execução.",
]

MENU_ASSISTENTE = [
    "(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.",
    "(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.",
    "(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).",
    "(4) Finalizar execução.",
]

MSG_NAO_CADASTRADA = "Pessoa não cadastrada. Tem certeza que o nome está certo?"
MSG_NAO_CADASTRADA_OU_VAZIA = ("Pessoa não cadastrada ou lista de espera vazia. "
                               "Tem certeza que o nome da pessoa está certo?")


def cabecalho(titulo):
    print(f"-------------- Olá, {titulo}! --------------")


def ler_opcao(menu):
    while True:
        print("\nVocê deseja:")
        for linha in menu:
            print(linha)
        texto = input("Digite sua opção: ").strip()
        try:
            opcao = int(texto)
        except ValueError:
            continue
        if 1 <= opcao <= len(menu):
            return opcao


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_idade(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            idade = int(texto)
        except ValueError:
            idade = 0
        if idade > 0:
            return idade
        print("Idade inválida. Digite um número inteiro maior que zero.")


def ler_telefone(mensagem):
    while True:
        telefone = input(mensagem).strip()
        if telefone:
            return telefone
        print("O telefone não pode ficar vazio.")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"


def secretario():
    atribuicoes_secretario.iniciar()
    cabecalho("Secretário(a)")
    while True:
        opcao = ler_opcao(MENU_SECRETARIO)
        if opcao == 1:
            nome = ler_nome("Digite o nome da pessoa: ")
            idade = ler_idade("Digite a idade ")
            telefone = ler_telefone("Digite o telefone: ")
            resultado = atribuicoes_secretario.cadastrar_pessoa(nome, idade, telefone)
            if resultado is None:
                print("Já existe uma pessoa cadastrada com esse nome.")
            else:
                print(resultado)
        elif opcao == 2:
            nome = ler_nome("Digite o nome da pessoa: ")
            resultado = atribuicoes_secretario.consultar_pessoa(nome)
            if resultado is None:
                print(MSG_NAO_CADASTRADA)
            else:
                print(resultado)
        elif opcao == 3:
            quantidade = atribuicoes_secretario.obter_quantidade()
            if quantidade == 1:
                print("É 1 pessoa na lista de espera.")
            else:
                print(f"São {quantidade} pessoas na lista de espera.")
        else:
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).")
            print("\n")
            return


def editar_pessoa():
    nome = ler_nome("Digite o nome da pessoa que você quer editar: ")
    resultado = atribuicoes_diretor.buscar_pessoa(nome)
    if resultado is None:
        print(MSG_NAO_CADASTRADA)
        return
    print(resultado)
    while True:
        texto = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ").strip()
        if texto in ("1", "2", "3"):
            campo = int(texto)
            break
    if campo == atribuicoes_diretor.NOME:
        novo_valor = ler_nome("Digite o novo nome: ")
    elif campo == atribuicoes_diretor.IDADE:
        novo_valor = ler_idade("Digite a nova idade: ")
    else:
        novo_valor = ler_telefone("Digite o novo telefone: ")
    situacao = atribuicoes_diretor.alterar_dados(nome, campo, novo_valor)
    if situacao == atribuicoes_diretor.ALTERADO:
        print("Dados atualizados com sucesso.")
    elif situacao == atribuicoes_diretor.NOME_JA_EXISTE:
        print("Já existe uma pessoa cadastrada com esse nome. Nada foi alterado.")
    else:
        print(MSG_NAO_CADASTRADA)


def descadastrar_pessoa():
    nome = ler_nome("Digite o nome da pessoa que você quer descadastrar: ")
    resultado = atribuicoes_diretor.buscar_pessoa(nome)
    if resultado is None:
        print(MSG_NAO_CADASTRADA_OU_VAZIA)
        return
    print(resultado)
    if ler_sim_nao(f"Tem certeza que deseja descadastrar {nome}? Digite S ou N: "):
        atribuicoes_diretor.descadastrar_pessoa(nome)
        print(f"{nome} descadastrado com sucesso.")
    else:
        print("Descadastro cancelado.")


def diretor():
    atribuicoes_diretor.iniciar()
    cabecalho("Diretor(a)")
    while True:
        opcao = ler_opcao(MENU_DIRETOR)
        if opcao == 1:
            editar_pessoa()
        elif opcao == 2:
            descadastrar_pessoa()
        elif opcao == 3:
            resultado = atribuicoes_diretor.obter_primeira_pessoa()
            print(resultado if resultado is not None else "A lista de espera está vazia.")
        elif opcao == 4:
            resultado = atribuicoes_diretor.obter_ultima_pessoa()
            print(resultado if resultado is not None else "A lista de espera está vazia.")
        else:
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).")
            print("\n")
            return


def mostrar_caminho(caminho, custo):
    if caminho is None:
        print("Não existe caminho entre as cidades.")
    else:
        print(f"Menor caminho = {caminho} com custo {custo}")


def assistente():
    atribuicoes_assistente.iniciar()
    cabecalho("Assistente")
    while True:
        opcao = ler_opcao(MENU_ASSISTENTE)
        if opcao == 1 or opcao == 2:
            nome = ler_nome("Digite o nome da pessoa cuja cidade te interessa: ")
            if opcao == 1:
                resultado = atribuicoes_assistente.menor_distancia_escola_pessoa(nome)
            else:
                resultado = atribuicoes_assistente.menor_distancia_via_intermediaria(nome)
            if resultado is None:
                print(MSG_NAO_CADASTRADA_OU_VAZIA)
            else:
                pessoa, caminho, custo = resultado
                print(pessoa)
                mostrar_caminho(caminho, custo)
        elif opcao == 3:
            resultado = atribuicoes_assistente.cidade_mais_proxima_com_moradores()
            if resultado is None:
                print("Não há pessoas cadastradas na lista de espera.")
            else:
                cidade, distancia, moradores = resultado
                print("A cidade mais próxima à cidade da escola que tem moradores na lista de espera "
                      f"(ver abaixo) é {cidade}. Distância = {distancia}")
                for morador in moradores:
                    print(morador)
        else:
            print("Fim das atividades sob responsabilidade do(a) Assistente.")
            return


def main():
    secretario()
    diretor()
    assistente()


if __name__ == "__main__":
    main()
