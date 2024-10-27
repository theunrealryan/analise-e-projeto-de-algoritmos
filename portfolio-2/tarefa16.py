# Grafo representado como um dicionário
grafo = {
    'a': {'b': 16, 'f': 21, 'e': 9},
    'b': {'c': 5, 'd': 6, 'f': 11},
    'c': {},
    'd': {'c': 10},
    'e': {'d': 14, 'f': 33},
    'f': {'b': 11, 'd': 14}
}

def caminho_guloso(grafo, inicio, destino):
    atual = inicio
    caminho = [atual]
    distancia_total = 0

    # Continuar enquanto não chegarmos ao destino
    while atual != destino:
        # Pegar os vizinhos do nó atual
        vizinhos = grafo[atual]
        
        # Se não houver vizinhos, termina (não há caminho disponível)
        if not vizinhos:
            return None, float('inf')
        
        # Encontrar o vizinho com o menor peso
        proximo, menor_distancia = min(vizinhos.items(), key=lambda x: x[1])
        
        # Adicionar a distância ao total
        distancia_total += menor_distancia
        # Adicionar o próximo nó ao caminho
        caminho.append(proximo)
        
        # Avançar para o próximo nó
        atual = proximo
    
    return caminho, distancia_total

# Testar o algoritmo guloso para o menor caminho de 'a' para 'c'
caminho, distancia = caminho_guloso(grafo, 'a', 'c')
print("Caminho encontrado:", caminho)
print("Distância total:", distancia)
