# Definindo o grafo como um dicionário de dicionários com pesos
grafo = {
    'a': {'b': 16, 'f': 21, 'e': 9},
    'b': {'c': 5, 'd': 6, 'f': 11},
    'c': {},
    'd': {'c': 10},
    'e': {'d': 18, 'f': 33},
    'f': {'b': 11, 'd': 14}
}

def caminho_guloso(grafo, origem, destino):
    caminho = [origem]
    custo_total = 0
    atual = origem

    while atual != destino:
        # Seleciona a aresta de menor peso a partir do vértice atual
        vizinhos = grafo[atual]
        if not vizinhos:  # Se não há vizinhos, o destino não é alcançável
            print("Destino não alcançável com este método.")
            return None

        # Encontra o vizinho com a menor aresta
        proximo_vertice = min(vizinhos, key=vizinhos.get)
        peso = vizinhos[proximo_vertice]

        # Atualiza o caminho e o custo total
        caminho.append(proximo_vertice)
        custo_total += peso
        atual = proximo_vertice

    return caminho, custo_total

# Teste do algoritmo guloso simples de 'a' para 'c'
origem = 'a'
destino = 'c'
caminho, custo_total = caminho_guloso(grafo, origem, destino)

# Exibe o caminho e o custo total
print("Caminho encontrado pelo algoritmo guloso simples:")
if caminho:
    print(" -> ".join(caminho))
    print(f"Custo total: {custo_total}")