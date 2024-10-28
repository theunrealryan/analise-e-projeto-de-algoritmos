# Definindo o grafo como uma lista de adjacências
grafo = {
    0: [2],
    1: [3, 3],
    2: [6],
    3: [7],
    4: [],
    5: [],
    6: [0, 4, 2],
    7: [],
    8: [5]
}

# Exibindo a lista de adjacências
print("Lista de Adjacência:")
for vertice, adjacentes in grafo.items():
    print(f"{vertice}: {' '.join(map(str, adjacentes))}")
