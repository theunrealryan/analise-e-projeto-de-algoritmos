import heapq

# Definindo o grafo como um dicionário de dicionários com pesos
grafo = {
    'a': {'b': 16, 'f': 21, 'e': 9},
    'b': {'c': 5, 'd': 6, 'f': 11},
    'c': {},
    'd': {'c': 10},
    'e': {'d': 18, 'f': 33},
    'f': {'b': 11, 'd': 14}
}

# Função para o Algoritmo de Dijkstra
def dijkstra(grafo, origem, destino):
    # Inicializa as distâncias com infinito para todos os vértices exceto o de origem
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    caminho_anterior = {v: None for v in grafo}

    # Fila de prioridade para o próximo nó com a menor distância conhecida
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Se chegamos ao destino, paramos
        if vertice_atual == destino:
            break

        # Verifica todos os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso

            # Se uma distância menor é encontrada, atualiza
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho_anterior[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    # Reconstrói o caminho mínimo a partir do destino
    caminho = []
    atual = destino
    while atual:
        caminho.insert(0, atual)
        atual = caminho_anterior[atual]

    # Retorna o caminho e o custo total do caminho
    custo_total = distancias[destino]
    return caminho, custo_total

# Definindo os vértices de origem e destino
origem = 'a'
destino = 'c'

# Teste do Algoritmo de Dijkstra de 'a' para 'c'
caminho_dijkstra, custo_total_dijkstra = dijkstra(grafo, origem, destino)

# Exibe o caminho e o custo total
print("\nCaminho encontrado pelo Algoritmo de Dijkstra:")
print(" -> ".join(caminho_dijkstra))
print(f"Custo total: {custo_total_dijkstra}")