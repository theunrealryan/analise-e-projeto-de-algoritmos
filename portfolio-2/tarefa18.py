from collections import deque

class Grafo:
    def __init__(self):
        # Inicializa o dicionário de adjacência
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        # Adiciona um vértice ao grafo se ainda não existir
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_arco(self, origem, destino):
        # Adiciona um arco do vértice de origem ao vértice de destino
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencia[origem].append(destino)

    def GRAPHbfs(self, inicio):
        # Implementa a busca em largura (BFS)
        visitados = set()
        fila = deque([inicio])
        rastreamento = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                rastreamento.append(vertice)
                for vizinho in self.adjacencia[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)

        print("Ordem de visita (BFS):", ' '.join(map(str, rastreamento)))

    def GRAPHdfs(self, inicio):
        # Implementa a busca em profundidade (DFS)
        visitados = set()
        rastreamento = []

        def dfs(vertice):
            visitados.add(vertice)
            rastreamento.append(vertice)
            for vizinho in self.adjacencia[vertice]:
                if vizinho not in visitados:
                    dfs(vizinho)

        dfs(inicio)
        print("Ordem de visita (DFS):", ' '.join(map(str, rastreamento)))

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência do grafo
        for vertice in sorted(self.adjacencia.keys()):
            adjacentes = self.adjacencia[vertice]
            arestas = ' '.join(map(str, adjacentes))
            print(f"{vertice}: {arestas}")

# Função para criar o primeiro grafo
def criar_primeiro_grafo():
    grafo = Grafo()
    arcos = [(0,1), (1,2), (1,3), (3,4), (3,5), (1,6), (0,7), (7,8), (7,9), (8,6)]
    for origem, destino in arcos:
        grafo.adicionar_arco(origem, destino)
    return grafo

# Função para criar o segundo grafo
def criar_segundo_grafo():
    grafo = Grafo()
    lista_adjacencia = {
        0: [1, 4],
        1: [2, 5],
        2: [3],
        3: [7],
        4: [8],
        5: [4],
        6: [5, 10, 2],
        7: [11, 6],
        8: [9],
        9: [5, 8],
        10: [9],
        11: [10]
    }
    for vertice, adjacentes in lista_adjacencia.items():
        for adj in adjacentes:
            grafo.adicionar_arco(vertice, adj)
    return grafo

# Execução das buscas no primeiro grafo
print("Primeiro Grafo:")
grafo1 = criar_primeiro_grafo()
grafo1.exibir_lista_adjacencia()
grafo1.GRAPHbfs(0)
grafo1.GRAPHdfs(0)
print("\n")

# Execução das buscas no segundo grafo
print("Segundo Grafo:")
grafo2 = criar_segundo_grafo()
grafo2.exibir_lista_adjacencia()
grafo2.GRAPHbfs(0)
grafo2.GRAPHdfs(0)
