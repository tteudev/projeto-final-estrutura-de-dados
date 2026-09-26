import random

from grafo import ler_cidades
from lista_encadeada import ListaEncadeada
from pessoa import Pessoa

_lista = None
_cidades = []


def iniciar():
    global _lista, _cidades
    _lista = ListaEncadeada()
    _cidades = ler_cidades()


def cadastrar_pessoa(nome, idade, telefone, cidade=None):
    """Cadastra a pessoa com uma cidade sorteada. Retorna o texto da pessoa,
    ou None se ja existir alguem com esse nome."""
    if _lista.buscar(nome) is not None:
        return None
    if cidade is None:
        cidade = random.choice(_cidades)
    pessoa = Pessoa(nome.strip(), idade, telefone.strip(), cidade)
    _lista.inserir_final(pessoa)
    return str(pessoa)


def consultar_pessoa(nome):
    pessoa = _lista.buscar(nome)
    if pessoa is None:
        return None
    return str(pessoa)


def obter_quantidade():
    return _lista.quantidade()


def obter_lista_encadeada():
    return _lista
