import time
import pandas as pd
import sys

# Aumentar o limite de recursão (para valores maiores que 1000)
sys.setrecursionlimit(10000)

# Função Fibonacci Recursiva com exibição de valores parciais
def fibonacci_recursivo(n):
    if n <= 1:
        print(f"fibonacci_recursivo({n}) = {n}")
        return n
    else:
        resultado = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
        print(f"fibonacci_recursivo({n}) = {resultado}")
        return resultado

# Função Fibonacci Iterativa com exibição de valores parciais
def fibonacci_iterativo(n):
    a, b = 0, 1
    print(f"fibonacci_iterativo(0) = {a}")
    for i in range(1, n+1):
        print(f"fibonacci_iterativo({i}) = {b}")
        a, b = b, a + b
    return a

# Valores de n para testar
valores_n = [10, 20, 30, 50, 100]

# Medindo tempo de execução para função recursiva
valores_n_recursivo = [10, 20, 30, 50, 100]
tempos_recursivos = []
print("Execução da função recursiva:")
for n in valores_n_recursivo:
    inicio = time.time()
    fibonacci_recursivo(n)
    fim = time.time()
    tempos_recursivos.append(fim - inicio)
    print("-" * 40)

# Medindo tempo de execução para função iterativa
tempos_iterativos = []
print("Execução da função iterativa:")
for n in valores_n:
    inicio = time.time()
    fibonacci_iterativo(n)
    fim = time.time()
    tempos_iterativos.append(fim - inicio)
    print("-" * 40)

# Criando o DataFrame com os resultados
df_resultados_atualizados = pd.DataFrame({
    "n": valores_n,
    "Tempo Recursivo (s)": tempos_recursivos,
    "Tempo Iterativo (s)": tempos_iterativos
})

# Exibindo os resultados
print("\nResultados finais:")
print(df_resultados_atualizados)