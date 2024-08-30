import matplotlib.pyplot as plt
import time

def crivo_eratostenes(n):

  # Inicializa uma lista com todos os números de 2 até n como primos (True)
  primos = [True for _ in range(n+1)]
  p = 2

  # Mark as composite numbers by iterating over multiples of p
  while (p * p <= n):
    # If p is still consi dered prime, mark all its multiples as composite
    if (primos[p] == True):
      for i in range(p * p, n+1, p):
        primos[i] = False
    p += 1

  # Create a list of prime numbers
  numeros_primos = []
  for p in range(2, n+1):
    if primos[p]:
      numeros_primos.append(p)

  return numeros_primos

# Obtém o número limite do usuário
limite = int(input("Digite um número inteiro: "))

# Chama a função e imprime os números primos
resultado = crivo_eratostenes(limite)
print("Números primos até", limite, ":", resultado)

def plotar_tempo_execucao(limite_maximo):
    tempos = []
    tamanhos = []
    for n in range(2, limite_maximo + 1):
        inicio = time.time()
        crivo_eratostenes(n)
        fim = time.time()
        tempos.append(fim - inicio)
        tamanhos.append(n)

    plt.plot(tamanhos, tempos)
    plt.xlabel("Tamanho da Entrada (n)")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Tempo de Execução do Crivo de Eratóstenes")
    plt.grid(True)
    plt.show()

limite_maximo = 1000

# Chama a função para plotar o gráfico
plotar_tempo_execucao(limite_maximo)