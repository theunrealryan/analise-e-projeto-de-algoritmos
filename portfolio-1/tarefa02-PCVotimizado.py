import random
import time

def calcular_distancia_total(rota, distancias):
    """Calcula a distância total de uma rota."""
    distancia_total = 0
    num_cidades = len(rota)
    for i in range(num_cidades):
        distancia_total += distancias[rota[i]][rota[(i+1) % num_cidades]]
    return distancia_total

def caixeiro_viajante_guloso(distancias):
    """Implementa o algoritmo guloso para o problema do caixeiro viajante."""
    num_cidades = len(distancias)
    visitadas = set([0])
    nao_visitadas = set(range(1, num_cidades))

    rota = [0]
    while nao_visitadas:
        atual = rota[-1]
        proxima = min(nao_visitadas, key=lambda x: distancias[atual][x])
        rota.append(proxima)
        visitadas.add(proxima)
        nao_visitadas.remove(proxima)

    return rota

if __name__ == "__main__":
    num_cidades = int(input("Digite o número de cidades: "))
    
    inicio = time.time()

    # Gera uma matriz de distâncias simétrica com zeros na diagonal
    distancias = [[0]*num_cidades for _ in range(num_cidades)]
    for i in range(num_cidades):
        for j in range(i+1, num_cidades):
            dist = random.randint(1, 100)
            distancias[i][j] = dist
            distancias[j][i] = dist

    rota_gulosa = caixeiro_viajante_guloso(distancias)
    distancia_gulosa = calcular_distancia_total(rota_gulosa, distancias)

    fim = time.time()
    tempo_execucao = fim - inicio

    print("Rota gulosa:", rota_gulosa)
    print("Distância total da rota gulosa:", distancia_gulosa)
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
