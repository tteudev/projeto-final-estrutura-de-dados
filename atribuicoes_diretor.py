import atribuicoes_secretario
from arvore_binaria import ArvoreBinariaBusca
from pessoa import chave_nome

_arvore = None

NOME = 1
IDADE = 2
TELEFONE = 3

# resultados de alterar_dados
ALTERADO = 0
NAO_ENCONTRADA = 1
NOME_JA_EXISTE = 2


def converter_lista_para_arvore(lista):
    arvore = ArvoreBinariaBusca()
    for pessoa in lista.pessoas():
        arvore.inserir(pessoa)
    return arvore


def iniciar():
    global _arvore
    _arvore = converter_lista_para_arvore(atribuicoes_secretario.obter_lista_encadeada())


def buscar_pessoa(nome):
    pessoa = _arvore.buscar(nome)
    if pessoa is None:
        return None
    return str(pessoa)


def alterar_dados(nome_atual, campo, novo_valor):
    pessoa = _arvore.buscar(nome_atual)
    if pessoa is None:
        return NAO_ENCONTRADA
    if campo == NOME:
        novo_nome = novo_valor.strip()
        if chave_nome(novo_nome) != chave_nome(pessoa.nome):
            if _arvore.buscar(novo_nome) is not None:
                return NOME_JA_EXISTE
            # o nome e a chave da arvore: remove e reinsere na posicao correta
            _arvore.remover(pessoa.nome)
            pessoa.nome = novo_nome
            _arvore.inserir(pessoa)
        else:
            pessoa.nome = novo_nome
    elif campo == IDADE:
        pessoa.idade = novo_valor
    elif campo == TELEFONE:
        pessoa.telefone = novo_valor.strip()
    return ALTERADO


def descadastrar_pessoa(nome):
    return _arvore.remover(nome) is not None


def obter_primeira_pessoa():
    pessoa = _arvore.minimo()
    if pessoa is None:
        return None
    return str(pessoa)


def obter_ultima_pessoa():
    pessoa = _arvore.maximo()
    if pessoa is None:
        return None
    return str(pessoa)


def obter_arvore():
    return _arvore
