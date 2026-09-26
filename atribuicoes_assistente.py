import atribuicoes_diretor
from grafo import carregar_grafo

CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"

_arvore = None
_grafo = None


def iniciar():
    global _arvore, _grafo
    _arvore = atribuicoes_diretor.obter_arvore()
    _grafo = carregar_grafo()


def buscar_pessoa(nome):
    pessoa = _arvore.buscar(nome)
    if pessoa is None:
        return None
    return str(pessoa)


def menor_distancia_escola_pessoa(nome):
    """Retorna (texto da pessoa, caminho, custo) ou None se a pessoa nao existe."""
    pessoa = _arvore.buscar(nome)
    if pessoa is None:
        return None
    caminho, custo = _grafo.menor_caminho(CIDADE_ESCOLA, pessoa.cidade)
    return str(pessoa), caminho, custo


def menor_distancia_via_intermediaria(nome):
    pessoa = _arvore.buscar(nome)
    if pessoa is None:
        return None
    caminho1, custo1 = _grafo.menor_caminho(CIDADE_ESCOLA, CIDADE_INTERMEDIARIA)
    caminho2, custo2 = _grafo.menor_caminho(CIDADE_INTERMEDIARIA, pessoa.cidade)
    if caminho1 is None or caminho2 is None:
        return str(pessoa), None, None
    return str(pessoa), caminho1 + caminho2[1:], custo1 + custo2


def cidade_mais_proxima_com_moradores():
    """Retorna (cidade, distancia, [textos das pessoas]) ou None se nao houver
    ninguem cadastrado com cidade alcancavel."""
    distancias, _ = _grafo.dijkstra(CIDADE_ESCOLA)
    melhor_cidade = None
    melhor_distancia = None
    for pessoa in _arvore.em_ordem():
        if pessoa.cidade not in distancias:
            continue
        distancia = distancias[pessoa.cidade]
        if (melhor_distancia is None or distancia < melhor_distancia
                or (distancia == melhor_distancia and pessoa.cidade < melhor_cidade)):
            melhor_cidade = pessoa.cidade
            melhor_distancia = distancia
    if melhor_cidade is None:
        return None
    moradores = [str(p) for p in _arvore.em_ordem() if p.cidade == melhor_cidade]
    return melhor_cidade, melhor_distancia, moradores
