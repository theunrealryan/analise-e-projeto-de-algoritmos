import time
import sys

# Aumentar o limite de recursão (para valores maiores que 1000)
sys.setrecursionlimit(2000)


# Implementação recursiva de F(n)
def F_recursivo(n, F0):
    if n == 0:
        return F0
    else:
        return F_recursivo(n-1, F0) + n*(n+1)//2 + n

# Implementação da fórmula fechada para F(n)
def F_solucao_fechada(n, F0):
    return F0 + (n**2 + 3*n + 2*F0)//2 + n

# Função para medir o tempo de execução
def medir_tempo_funcao(func, n, F0):
    inicio = time.time()
    resultado = func(n, F0)
    fim = time.time()
    tempo_execucao = fim - inicio
    return resultado, tempo_execucao

# Função para executar os testes
def executar_testes():
    # Definir os valores de n e F0
    ######################################
    valores_n = [100, 1000] #REVER ESSA PARTE
    #####################################
    valores_F0 = [1, 10]

    # Testar para cada combinação de n e F0
    for n in valores_n:
        for F0 in valores_F0:
            print(f"Testando para n={n}, F0={F0}:")

            # Medir o tempo de execução da função recursiva
            resultado_recursivo, tempo_recursivo = medir_tempo_funcao(F_recursivo, n, F0)
            print(f"Recursivo -> Resultado: {resultado_recursivo}, Tempo: {tempo_recursivo:.6f} segundos")

            # Medir o tempo de execução da solução fechada
            resultado_fechada, tempo_fechada = medir_tempo_funcao(F_solucao_fechada, n, F0)
            print(f"Solução Fechada -> Resultado: {resultado_fechada}, Tempo: {tempo_fechada:.6f} segundos")

            print()

# Executar os testes
executar_testes()