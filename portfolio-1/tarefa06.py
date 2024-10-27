import time
import matplotlib.pyplot as plt # type: ignore

def soma_quadrados_A(n):
    x = 0
    for i in range(n + 1):
        x += i * i
    return x


def soma_quadrados_B(n):
    return (n * (n + 1) * ( 2*n + 1)) / 6


def calcular_tempo(funcao, n):
    inicio = time.perf_counter()
    funcao(n)
    fim = time.perf_counter()
    return fim - inicio


tempos_A = []
tempos_B = []
nums = []

qtde = int(input('Digite a quantidade de valores: '))

for i in range(qtde):
    nums.append(int(input(f'Digite o valor {i+1}: ')))

for i in range(len(nums)):
    tempos_A.append(calcular_tempo(soma_quadrados_A, nums[i]))
    tempos_B.append(calcular_tempo(soma_quadrados_B, nums[i]))

plt.plot(nums, tempos_A, color='red', linestyle='--', marker='o', label='soma_quadrados_A')
plt.plot(nums, tempos_B, color='blue', linestyle='--', marker='o', label='soma_quadrados_B')
plt.xlabel('n')
plt.ylabel('Tempo de Execução (s)')
plt.title('soma_quadrados_A x soma_quadrados_B')
plt.legend()
plt.show()

soma1 = soma_quadrados_A(10)
soma2 = soma_quadrados_B(10)
print(soma1, soma2)