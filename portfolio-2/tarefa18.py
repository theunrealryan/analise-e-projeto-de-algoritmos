class Grafo:
    def __init__(self):
        self.adjacencia = {}
        
    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []
            
    def adicionar_aresta(self, vertice1, vertice2, direcionada=False):
        self.adicionar_vertice(vertice1)
        self.adicionar_vertice(vertice2)
        self.adjacencia[vertice1].append(vertice2)
        if not direcionada:
            self.adjacencia[vertice2].append(vertice1)
        
    def GRAPHbfs(self, inicio):
        visitados = set()
        fila = []
        rastreamento = []
        
        fila.append(inicio)
        visitados.add(inicio)
        rastreamento.append(f"Iniciando BFS no vértice {inicio}")
        
        while fila:
            atual = fila.pop(0)
            rastreamento.append(f"Visitando vértice {atual}")
            for vizinho in self.adjacencia[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)
                    rastreamento.append(f"Enfileirando vértice {vizinho}")
        return rastreamento
    
    def GRAPHdfs_util(self, atual, visitados, rastreamento):
        visitados.add(atual)
        rastreamento.append(f"Visitando vértice {atual}")
        for vizinho in self.adjacencia[atual]:
            if vizinho not in visitados:
                rastreamento.append(f"Indo para o vértice {vizinho}")
                self.GRAPHdfs_util(vizinho, visitados, rastreamento)
                rastreamento.append(f"Retornando ao vértice {atual}")
                
    def GRAPHdfs(self, inicio):
        visitados = set()
        rastreamento = []
        rastreamento.append(f"Iniciando DFS no vértice {inicio}")
        self.GRAPHdfs_util(inicio, visitados, rastreamento)
        return rastreamento

# Grafo 1 - Não direcionado
grafo1 = Grafo()

arestas_grafo1 = [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5), (1, 6), (0, 7), (7, 8), (7, 9), (8, 6)]
for v1, v2 in arestas_grafo1:
    grafo1.adicionar_aresta(v1, v2)

rastreamento_bfs1 = grafo1.GRAPHbfs(0)
rastreamento_dfs1 = grafo1.GRAPHdfs(0)

print("Rastreamento da Busca em Largura (Grafo 1):")
for passo in rastreamento_bfs1:
    print(passo)

print("\nRastreamento da Busca em Profundidade (Grafo 1):")
for passo in rastreamento_dfs1:
    print(passo)

# Grafo 2 - Direcionado
grafo2 = Grafo()

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

for vertice, vizinhos in lista_adjacencia.items():
    for vizinho in vizinhos:
        grafo2.adicionar_aresta(vertice, vizinho, direcionada=True)

rastreamento_bfs2 = grafo2.GRAPHbfs(0)
rastreamento_dfs2 = grafo2.GRAPHdfs(0)

print("\nRastreamento da Busca em Largura (Grafo 2):")
for passo in rastreamento_bfs2:
    print(passo)

print("\nRastreamento da Busca em Profundidade (Grafo 2):")
for passo in rastreamento_dfs2:
    print(passo)
