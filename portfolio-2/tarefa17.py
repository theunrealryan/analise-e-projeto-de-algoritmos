class Grafo:
    def __init__(self):
        # Inicializa o dicionário de adjacência
        self.adjacencia = {}
            
    def adicionar_vertice(self, vertice):
        # Adiciona um vértice ao grafo se ainda não existir
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []
        
    def adicionar_arco(self, origem, destino, identificador):
        # Adiciona um arco ao grafo com identificador
        if origem in self.adjacencia:
            self.adjacencia[origem].append((destino, identificador))
        else:
            self.adjacencia[origem] = [(destino, identificador)]
        
    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência ordenada
        for vertice in sorted(self.adjacencia.keys()):
            adjacentes = self.adjacencia[vertice]
            if adjacentes:
                arestas = ', '.join([f"{destino}(arco {identificador})" for destino, identificador in adjacentes])
                print(f"{vertice}: {arestas}")
            else:
                print(f"{vertice}: ")

# Inicializando o grafo
grafo = Grafo()

# Adicionando vértices individualmente
grafo.adicionar_vertice(0)  # Vértice 0
grafo.adicionar_vertice(1)  # Vértice 1
grafo.adicionar_vertice(2)  # Vértice 2
grafo.adicionar_vertice(3)  # Vértice 3
grafo.adicionar_vertice(4)  # Vértice 4
grafo.adicionar_vertice(5)  # Vértice 5
grafo.adicionar_vertice(6)  # Vértice 6
grafo.adicionar_vertice(7)  # Vértice 7
grafo.adicionar_vertice(8)  # Vértice 8

# Adicionando arcos individualmente com identificação
grafo.adicionar_arco(0, 0, "a")  # Arco "a" de 0 para 0
grafo.adicionar_arco(0, 2, "b")  # Arco "b" de 0 para 2
grafo.adicionar_arco(2, 6, "c")  # Arco "c" de 2 para 6
grafo.adicionar_arco(0, 4, "d")  # Arco "d" de 0 para 4
grafo.adicionar_arco(6, 6, "e")  # Arco "e" de 6 para 6
grafo.adicionar_arco(6, 8, "f")  # Arco "f" de 6 para 8
grafo.adicionar_arco(1, 3, "g")  # Arco "g" de 1 para 3
grafo.adicionar_arco(3, 3, "h")  # Arco "h" de 3 para 3
grafo.adicionar_arco(3, 7, "i")  # Arco "i" de 3 para 7
grafo.adicionar_arco(8, 5, "j")  # Arco "j" de 8 para 5

# Exibindo a lista de adjacência
grafo.exibir_lista_adjacencia()
