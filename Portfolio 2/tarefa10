import time
import matplotlib.pyplot as plt

# Algoritmo Iterativo para verificar se x está no vetor A
def decide_iterativo(A, n, x):
    i = 1
    while i <= n and A[i-1] != x:
        print(f"Iterativo - Comparando A[{i-1}] = {A[i-1]} com x = {x}")
        i += 1
    if i > n:
        print(f"Iterativo - Elemento {x} NÃO encontrado.")
        return "NÃO"
    else:
        print(f"Iterativo - Elemento {x} encontrado.")
        return "SIM"

# Algoritmo Recursivo para verificar se x está no vetor A
def decide_recursivo(A, n, x):
    if n == 0:
        print(f"Recursivo - Chegamos ao caso base, elemento {x} NÃO encontrado.")
        return "NÃO"
    elif A[n-1] == x:
        print(f"Recursivo - Comparando A[{n-1}] = {A[n-1]} com x = {x}. Elemento encontrado.")
        return "SIM"
    else:
        print(f"Recursivo - Comparando A[{n-1}] = {A[n-1]} com x = {x}. Continuando busca.")
        return decide_recursivo(A, n-1, x)

# Função para medir o tempo de execução de cada algoritmo
def medir_tempo(algoritmo, A, n, x):
    inicio = time.time()
    if algoritmo == 'I':
        resultado = decide_iterativo(A, n, x)
    else:
        resultado = decide_recursivo(A, n, x)
    fim = time.time()
    return fim - inicio, resultado

# Função para executar os algoritmos com n = 10 e n = 100 e gerar gráficos
def executar_algoritmos():
    # Tamanhos do vetor
    tamanhos = [10, 100]
    x = int(input("Escolha o valor de x que deseja buscar no vetor (por exemplo, 5): "))
    
    # Laços para executar os testes
    tempos_iterativo = []
    tempos_recursivo = []
    
    for n in tamanhos:
        A = list(range(1, n+1))  # Vetor A com valores de 1 a n

        # Teste com algoritmo iterativo
        print(f"\nExecutando o algoritmo iterativo com n = {n}...")
        tempo_iterativo, resultado_iterativo = medir_tempo('I', A, n, x)
        tempos_iterativo.append(tempo_iterativo)
        print(f"Resultado Iterativo para n = {n}: {resultado_iterativo}")
        print(f"Tempo Iterativo: {tempo_iterativo:.6f} segundos\n")

        # Teste com algoritmo recursivo
        print(f"Executando o algoritmo recursivo com n = {n}...")
        tempo_recursivo, resultado_recursivo = medir_tempo('R', A, n, x)
        tempos_recursivo.append(tempo_recursivo)
        print(f"Resultado Recursivo para n = {n}: {resultado_recursivo}")
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

# Execução da função principal
executar_algoritmos()
