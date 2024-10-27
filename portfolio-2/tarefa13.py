import time
import pandas as pd
import sys

# Aumentar o limite de recursão (para valores maiores que 1000)
sys.setrecursionlimit(10000)

# Função Fibonacci Recursiva
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Função Fibonacci Iterativa
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Valores de n para testar
valores_n = [10, 20, 30, 50, 100]

# Medindo tempo de execução para função recursiva
valores_n_recursivo = [10, 20, 30, 50, 100]  # Limitando os valores de n para a função recursiva
tempos_recursivos = []
for n in valores_n_recursivo:
    inicio = time.time()
    fibonacci_recursivo(n)
    fim = time.time()
    tempos_recursivos.append(fim - inicio)

# Medindo tempo de execução para função iterativa
tempos_iterativos = []
for n in valores_n:
    inicio = time.time()
    fibonacci_iterativo(n)
    fim = time.time()
    tempos_iterativos.append(fim - inicio)

# Criando o DataFrame com os resultados
df_resultados_atualizados = pd.DataFrame({
    "n": valores_n,
    "Tempo Recursivo (s)": tempos_recursivos,
    "Tempo Iterativo (s)": tempos_iterativos
})

# Exibindo os resultados no terminal ou Jupyter Notebook
print(df_resultados_atualizados)
