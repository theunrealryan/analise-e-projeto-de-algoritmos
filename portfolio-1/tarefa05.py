import matplotlib.pyplot as plt
import time

def crivo_eratostenes(n):
  """
  Implementa o Crivo de Eratóstenes para encontrar números primos até n.

  Args:
      n: Limite superior para a busca de números primos.

  Returns:
      Uma lista contendo todos os números primos até n.
  """
  primos = [True] * (n + 1)  # Inicializa lista com todos True (primos)
  primos[0] = primos[1] = False  # 0 e 1 não são primos

  p = 2
  while p * p <= n:
    if primos[p]:
      for i in range(p * p, n + 1, p):
        primos[i] = False
    p += 1

  return [p for p in range(2, n + 1) if primos[p]]  # Filtra primos da lista

# Programa principal
tempo = []
nums = []

qtde = int(input('Defina a quantidade de valores: '))

for i in range(1, qtde + 1):
  valor = int(input(f'Valor {i}: '))
  nums.append(valor)

for i in range(len(nums)):
  inicial = time.perf_counter()
  n = crivo_eratostenes(nums[i])
  final = time.perf_counter()
  t = final - inicial
  tempo.append(t)

# Visualização do gráfico
plt.bar(nums, tempo, color=['tab:purple', 'tab:red', 'tab:blue', 'tab:orange'], width=1000)
plt.title('Tempo de execução para encontrar números primos')
plt.xlabel('Valores')
plt.ylabel('Tempo (s)')
plt.show()