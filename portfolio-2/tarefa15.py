import sys

# Função para calcular o produto de menor custo entre n matrizes
def matrix_chain_order(b, n):
    # Criando a matriz de custos m
    m = [[0] * n for _ in range(n)]

    # Inicializando as diagonais principais como zero
    for i in range(n):
        m[i][i] = 0

    # h representa o tamanho da subcadeia
    for h in range(1, n):
        for i in range(n - h):
            j = i + h
            m[i][j] = sys.maxsize  # Inicializa com valor infinito

            # Encontrando o ponto k que minimiza o custo
            for k in range(i, j):
                temp = m[i][k] + m[k + 1][j] + b[i] * b[k + 1] * b[j + 1]
                if temp < m[i][j]:
                    m[i][j] = temp

            # Exibindo o custo mínimo para multiplicar de i até j
            print(f"m[{i}][{j}] = {m[i][j]}")

    return m[0][n - 1]  # Retorna o custo mínimo total

# Entrada de dados
n = int(input("Número de matrizes n: "))
b = []

print("Dimensões das matrizes:")
for i in range(n + 1):
    b.append(int(input(f"Dimensão {i}: ")))

# Chamada da função e exibição do resultado
min_cost = matrix_chain_order(b, n)
print(f"O custo mínimo para multiplicar as matrizes é: {min_cost}")
