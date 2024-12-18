import itertools
import time
import random

def caixeiro_viajante_guloso(distancias):
    num_cidades = len(distancias)
    visitadas = [0] 
    nao_visitadas = list(range(1, num_cidades))

    rota = [0]
    while nao_visitadas:
        atual = rota[-1]
        proxima = min(nao_visitadas, key=lambda x: distancias[atual][x])
        rota.append(proxima)
        nao_visitadas.remove(proxima)

    return rota

def calcular_distancia_total(rota, distancias):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += distancias[rota[i]][rota[i+1]]
    distancia_total += distancias[rota[-1]][rota[0]] 
    return distancia_total

if __name__ == "__main__":
    num_cidades = int(input("Digite o número de cidades: "))

    distancias = [[random.randint(1, 100) for _ in range(num_cidades)] for _ in range(num_cidades)]

    inicio = time.time()

    todas_rotas = list(itertools.permutations(range(len(distancias))))
    num_rotas = len(todas_rotas)

    rota_gulosa = caixeiro_viajante_guloso(distancias)
    distancia_gulosa = calcular_distancia_total(rota_gulosa, distancias)

    fim = time.time()
    tempo_execucao = fim - inicio

    print("Número de rotas possíveis:", num_rotas)
    print(f"Tempo de execução: {tempo_execucao:.20f} segundos")
    rotas_por_segundo = float(num_rotas) / tempo_execucao
    print("Rotas possíveis por segundo:", rotas_por_segundo)
    print("Rota gulosa:", rota_gulosa)
    print("Distância total da rota gulosa:", distancia_gulosa)