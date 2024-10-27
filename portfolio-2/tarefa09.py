import time
import matplotlib.pyplot as plt

# Algoritmo Iterativo para encontrar o maior elemento
def max_iterativo(A, n):
    x = A[0]
    for i in range(1, n):
        if A[i] > x:
            x = A[i]
        print(f"Iterativo - Comparando A[{i}] = {A[i]} com max atual = {x}")
    return x

# Algoritmo Recursivo para encontrar o maior elemento
def max_recursivo(A, n):
    if n == 1:
        print(f"Recursivo - Base da recursão, retornando A[0] = {A[0]}")
        return A[0]
    else:
        max_n_1 = max_recursivo(A, n-1)
        print(f"Recursivo - Comparando A[{n-1}] = {A[n-1]} com max_n_1 = {max_n_1}")
        return max(A[n-1], max_n_1)

# Função para medir o tempo e comparar os algoritmos
def medir_tempo_algoritmo():
    # Tamanhos do vetor
    tamanhos = [10, 100]
    
    # Laço para executar os testes
    tempos_iterativo = []
    tempos_recursivo = []
    
    for n in tamanhos:
        A = list(range(1, n+1))  # Vetor A com valores de 1 a n

        # Teste com algoritmo iterativo
        inicio_iterativo = time.time()
        max_iterativo(A, n)
        fim_iterativo = time.time()
        tempo_iterativo = fim_iterativo - inicio_iterativo
        tempos_iterativo.append(tempo_iterativo)

        # Teste com algoritmo recursivo
        inicio_recursivo = time.time()
        max_recursivo(A, n)
        fim_recursivo = time.time()
        tempo_recursivo = fim_recursivo - inicio_recursivo
        tempos_recursivo.append(tempo_recursivo)

        print(f"\nPara n = {n}:")
        print(f"Tempo Iterativo: {tempo_iterativo:.6f} segundos")
        print(f"Tempo Recursivo: {tempo_recursivo:.6f} segundos\n")

    # Plotagem dos resultados
    plt.figure(figsize=(8, 6))
    plt.plot(tamanhos, tempos_iterativo, label='Iterativo', marker='o')
    plt.plot(tamanhos, tempos_recursivo, label='Recursivo', marker='o')
    plt.xlabel('Tamanho do Vetor (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Tempo: Algoritmo Iterativo vs Recursivo')
    plt.legend()
    plt.grid(True)
    plt.show()

# Execução da função de medição de tempo
medir_tempo_algoritmo()
