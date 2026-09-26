import heapq
import os

CAMINHO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cidades_vizinhas.csv")


def ler_arestas(caminho=CAMINHO_CSV):
    arestas = []
    with open(caminho, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            cidade1, cidade2, distancia = linha.split(";")
            arestas.append((cidade1.strip(), cidade2.strip(), int(distancia)))
    return arestas


def ler_cidades(caminho=CAMINHO_CSV):
    cidades = []
    vistas = set()
    for cidade1, cidade2, _ in ler_arestas(caminho):
        for cidade in (cidade1, cidade2):
            if cidade not in vistas:
                vistas.add(cidade)
                cidades.append(cidade)
    return cidades


class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, origem, destino, distancia):
        self.adjacencias.setdefault(origem, {})
        self.adjacencias.setdefault(destino, {})
        # o arquivo repete alguns pares nos dois sentidos, entao guarda so o menor peso
        if destino not in self.adjacencias[origem] or distancia < self.adjacencias[origem][destino]:
            self.adjacencias[origem][destino] = distancia
            self.adjacencias[destino][origem] = distancia

    def tem_cidade(self, cidade):
        return cidade in self.adjacencias

    def dijkstra(self, origem):
        distancias = {origem: 0}
        anteriores = {}
        fila = [(0, origem)]
        while fila:
            dist_atual, cidade = heapq.heappop(fila)
            if dist_atual > distancias[cidade]:
                continue
            for vizinha, peso in self.adjacencias[cidade].items():
                nova = dist_atual + peso
                if vizinha not in distancias or nova < distancias[vizinha]:
                    distancias[vizinha] = nova
                    anteriores[vizinha] = cidade
                    heapq.heappush(fila, (nova, vizinha))
        return distancias, anteriores

    def menor_caminho(self, origem, destino):
        if not self.tem_cidade(origem) or not self.tem_cidade(destino):
            return None, None
        distancias, anteriores = self.dijkstra(origem)
        if destino not in distancias:
            return None, None
        caminho = [destino]
        while caminho[-1] != origem:
            caminho.append(anteriores[caminho[-1]])
        caminho.reverse()
        return caminho, distancias[destino]


def carregar_grafo(caminho=CAMINHO_CSV):
    grafo = Grafo()
    for cidade1, cidade2, distancia in ler_arestas(caminho):
        grafo.adicionar_aresta(cidade1, cidade2, distancia)
    return grafo
